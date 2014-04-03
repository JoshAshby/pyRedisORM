import redis
from nose.tools import eq_, ok_, raises
from redisORM import redis_model

redis_model.redis = redis.StrictRedis("localhost", db=0)


def test_new_model():
    a = redis_model.RedisModel(namespace="test", key="test1", month="April")
    ok_(a.month, "Kwarg didn't make it into model data")
    eq_(a.month, "April", "Model data doesn't match")


def test_model_property():
    a = redis_model.RedisModel(namespace="test", key="test2")
    eq_(a.key, "test2", "Model key doesn't match")


def test_in_model():
    a = redis_model.RedisModel(namespace="test", key="test3")
    a.time = "five o'clock"
    ok_("time" in a, "__contains__ doesn't work")


def test_del_model():
    a = redis_model.RedisModel(namespace="test", key="test4")
    a.delete()


def test_string_only_model():
    a = redis_model.RedisModel(namespace="test", key="test5")

    a.time = "now"
    eq_(a.time, "now", "setattr - Model data doesn't match - getattr")
    eq_(a["time"], "now", "setattr - Model data doesn't match - getitem")
    b = redis_model.redis.get("test:test5:time")
    eq_(b, "now", "Raw redis data doesn't match")

    a["date"] = "then"
    eq_(a.date, "then", "setitem - Model data doesn't match - getattr")
    eq_(a["date"], "then", "setitem - Model data doesn't match - getitem")
    b = redis_model.redis.get("test:test5:date")
    eq_(b, "then", "Raw redis data doesn't match")


@raises(KeyError)
def test_delitem():
    a = redis_model.RedisModel(namespace="test", key="test6")
    a.time = "now"
    del a["time"]
    assert a.time is not None


def test_list_of_strings_only_model():
    list_fixture = ["one", "two", "three"]
    a = redis_model.RedisModel(namespace="test", key="test7")
    a.things = list_fixture

    for entry in list_fixture:
        ok_(entry in a.things, "Item missing from model list data: {}".format(entry))


def test_list_of_ints_only_model():
    list_fixture = [1, 2, 3]
    a = redis_model.RedisModel(namespace="test", key="test8")
    a.things = list_fixture

    for entry in list_fixture:
        ok_(entry in a.things, "Item missing from model list data: {}".format(entry))


def test_list_of_strings_and_ints_only_model():
    list_fixture = ["one", "two", "three", 1, 2, 3]
    a = redis_model.RedisModel(namespace="test", key="test9")
    a.things = list_fixture

    for entry in list_fixture:
        ok_(entry in a.things, "Item missing from model list data: {}".format(entry))


@raises(redis_model.RedisORMException)
def test_keys_exception():
    redis_model.RedisKeys(key=None)
