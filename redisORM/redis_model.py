#!/usr/bin/env python
"""
TODO: DOC THIS. Yes this. All of this. Everything. DOC IT! DOC IT NOAW!

.. note::
    The model stores all its data with a redis key structure like so:
    namespace:key:part

    Where namespace is the key prefix, key is the actual name or id of this
    object and part is the specific part of the model which that whole key
    stores.
"""

redis = None
"""
Global RedisModel connection which can be set before hand to avoid passing a
redis instance around everywhere all the time.
"""


class RedisORMException(Exception):
    """
    The general exception class which is raised by this module. Nothing special.
    """


class RedisKeys(object):
    """
    Where the realtime syncing and updating takes place.

    A `dict` like object which is used as the backing data store for
    :py:class:`.RedisModel`.

    Aka: The Source of Magic
    """
    def __init__(self, key, namespace="", conn=None):
        """
        Creates a new `dict` like object which is used to actually store data in
        redis. Under all normal circumstances, you should not need to use this
        class in any way shape or form, as it is the backing datastore for the
        model.

        :param key: The key section of the redis key.
        :param namespace: The key namespace.
        :param conn: The redis connection to use.

        :raises RedisORMException: If no key was provided.
        """
        self._data = dict()
        self.conn = conn or redis
        self.namespace = namespace # Key prefix
        self.key = key

        if not self.key:
            raise RedisORMException("RedisKeys needs a key, which means something went terribly wrong.")

        redis_search_key = ":".join([self.namespace, self.key, "*"])
        keys = self.conn.keys(redis_search_key)
        if keys:
            for key in keys:
                part = key.split(":")[-1]
                self.get(part)

    def delete(self):
        """
        Deletes all the keys from redis along with emptying the objects
        internal `_data` dict, then deleting itself at the end of it all.
        """
        redis_search_key = ":".join([self.namespace, self.key, "*"])
        keys = self.conn.keys(redis_search_key)
        if keys:
            for key in keys:
                part = key.split(":")[-1]
                self._data.pop(part)
                self.conn.delete(part)

        del self

    def get(self, part):
        """
        Retrieves a part of the model from redis and stores it.

        :param part: The part of the model to retrieve.
        :raises RedisORMException: If the redis type is different from string
            or list (the only two supported types at this time.)
        """
        redis_key = ':'.join([self.namespace, self.key, part])

        objectType = self.conn.type(redis_key)
        if objectType == "string":
            self._data[part] = self.conn.get(redis_key)

        elif objectType == "list":
            self._data[part] = RedisList(redis_key, self.conn)

        else:
            raise RedisORMException("Other types besides string and list are unsupported at this time.")

    def __repr__(self):
        return str(self._data)

    def __getitem__(self, part):
        return self._data[part]

    def __setitem__(self, part, value):
        key = ':'.join([self.namespace, self.key, part])

        if isinstance(value, list):
            self._data[part] = RedisList(key, self.conn, start=value)

        else:
            if value == None:
                value = ""

            self._data[part] = value
            self.conn.set(key, value)

    def __delitem__(self, part):
        key = ':'.join([self.namespace, self.key, part])
        self._data.pop(part)
        self.conn.delete(key)

    def __contains__(self, part):
        return part in self._data


class RedisList(object):
    """
    Attempts to emulate a python `list`, while backing the list in redis. This
    supports most of the common `list` functions, except as noted.

    Generally speaking, you won't have to create an instance of this class,
    however if you are working with a `list` then this is the class you'll get
    back, not a `list` class.

    .. note::
        Most notably, this is currently missing the sort and reverse functions.

    """
    def __init__(self, key, conn, start=[], reset=False):
        self._list = []
        self.conn = conn
        self.key = key
        self.sync()

        # Haxs I say...
        if start and not reset:
            self.extend(start)
        if start and reset:
            self.reset()
            self.extend(start)

    def __repr__(self):
        return repr(self._list)

    def __str__(self):
        return str(self._list)

    def sync(self):
        self._list = self.conn.lrange(self.key, 0, -1)
        self.listToInt()

    def listToInt(self):
        for elem in range(len(self._list)):
            try:
                self._list[elem] = int(self._list[elem])
            except:
                pass

    def append(self, other):
        self._list.append(other)
        self.conn.rpush(self.key, other)
        return self._list

    def prepend(self, other):
        self._list.insert(0, other)
        self.conn.lpush(self.key, other)

    def extend(self, other):
        assert type(other) == list
        self._list.extend(other)
        for key in other:
            self.conn.rpush(self.key, key)
        return self._list

    def insert(self, index, elem):
        self._list.insert(index, elem)
        self.conn.linsert(self.key, 'AFTER', index, elem)
        return self._list

    def remove(self, elem):
        self._list.remove(elem)
        self.conn.lrem(self.key, 1, elem)
        return self._list

    def pop(self):
        value = self._list.pop()
        self.conn.rpop(self.key)
        return value

    def lpop(self):
        value = self._list.pop(0)
        self.conn.lpop(self.key)
        return value

    def index(self, elem):
        return self._list.index(elem)

    def count(self):
        return self._list.count()

    def reset(self):
        self._list = []
        self.conn.delete(self.key)

    def __len__(self):
        return len(self._list)

    def __getitem__(self, index):
        return self._list[index]

    def __setitem__(self, index, value):
        self._list[index] = value
        self.conn.lset(self.key, index, value)

    def __iter__(self):
        for item in self._list:
            yield item

    def __contains__(self, item):
        return item in self._list


class RedisModel(object):
    """
    Emulates a python `object` for the data stored in the collection of keys which
    match this models, in Redis. Raw data from the redis is stored in
    `_data` which is a :py:class:`.RedisKeys` instance. This allows for the
    black magic which makes this class store changes in realtime to redis.

    This object has a `__repr__` method which can be used with print or logging
    statements. It will give the id and a representation of the internal `_data`
    :py:class:`.RedisKeys` for debugging purposes.
    """
    _data = None
    key = None
    conn = None #: The redis connection which this should use.
    _protected_items = [] #: Object properties which shouldn't be stored in redis.

    namespace = ""  #: The prefix which should be used for all keys in this model

    def __init__(self, namespace=None, key=None, conn=None, **kwargs):
        """
        TODO: Me

        :param namespace: The key prefix which should be used.
        :param key: The key or id of this object.
        :param conn: The redis connection to use. This can also be set on the
            class instance, or on the module level.
        :param kwargs: Any additional data which should be stored. This is used
            for creating a new object in redis.
        :raised RedisORMException: If no connection was supplied, or if there
            was a problem while creating the :py:class:`.RedisKeys` instance for
            the interal `_data`
        """
        self.namespace = self.namespace or namespace
        self.key = key

        self.conn = conn or redis
        if not self.conn:
            raise RedisORMException("No connection supplied.")

        self._data = RedisKeys(conn=self.conn, namespace=self.namespace, key=self.key)

        if kwargs:
            for item in kwargs:
                if item not in self._protected_items and item[0] != "_":
                    setattr(self, item, kwargs[item])

        # Hook to run any inherited class code, if needed
        self.finish_init()

    def finish_init(self):
        """
        A hook called at the end of the main `__init__` to allow for
        custom inherited classes to customize their init process without having
        to redo all of the existing int.
        This should accept nothing besides `self` and nothing should be
        returned.
        """
        pass

    def _get(self, attr):
        pro_its = object.__getattribute__(self, "_protected_items")
        if attr[0] == "_" or attr in pro_its:
            return object.__getattribute__(self, attr)

        elif attr in dir(self):
            return object.__getattribute__(self, attr)

        else:
            data = object.__getattribute__(self, "_data")
            return data[attr]

    def _set(self, attr, val):
        pro_its = object.__getattribute__(self, "_protected_items")
        if attr[0] == "_" or attr in pro_its:
            return object.__setattr__(self, attr, val)

        elif hasattr(val, "__call__") or attr in dir(self):
            return object.__setattr__(self, attr, val)

        else:
            data = object.__getattribute__(self, "_data")
            data[attr] = val
            return val

    def __getattr__(self, item):
        return object.__getattribute__(self, "_get")(item)

    def __getitem__(self, item):
        return object.__getattribute__(self, "_get")(item)

    def __setattr__(self, item, value):
        return object.__getattribute__(self, "_set")(item, value)

    def __setitem__(self, item, value):
        return object.__getattribute__(self, "_set")(item, value)

    def __delitem__(self, item):
        """
        Deletes the given item from the objects _data dict, or if from the
        objects namespace, if it does not exist in _data.
        """
        keys = object.__getattribute__(self, "_data")
        if item in keys:
            del(keys[item])
        else:
            object.__delitem__(self, item)

    def __contains__(self, item):
        """
        Allows for the use of syntax similar to::

            if "blah" in model:

        This only works with the internal _data, and does not include other
        properties in the objects namepsace, simply due to the mess that would
        create, and my lazyness.
        """
        keys = object.__getattribute__(self, "_data")
        if item in keys:
            return True
        return False

    @classmethod
    def new(cls, id=None, **kwargs):
        """
        Creates a new instance, filling out the models data with the keyword
        arguments passed, so long as those keywords are not in the protected
        items array.
        """
        return cls(id=id, **kwargs)

    @classmethod
    def create(cls, id=None, **kwargs):
        """
        Similar to new() however this calls save() on the object before
        returning it, to ensure that it is already in the database.
        Good for make and forget style calls.
        """
        what = cls(id=id, **kwargs)
        what.save()
        return what

    def delete(self):
        """
        Deletes the current instance, if its in the database (or try).
        """
        self._data.delete()
        del self

    def __repr__(self):
        """
        Allows for the representation of the object, for debugging purposes
        """
        return "<RedisModel.%s at %s with data: %s >" % (self.__class__.__name__,
                                                         id(self),
                                                         self._data)

    @property
    def protected_items(self):
        """
        Provides a cleaner interface to dynamically add items to the models
        list of protected functions to not store in the database
        """
        return self._protected_items

    @protected_items.setter
    def protected_items(self, value):
        if type(value) is list:
            self._protected_items.extend(value)
        else:
            assert type(value) is str
            self._protected_items.append(value)
        return self._protected_items
