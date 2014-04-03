import redis
from nose.tools import eq_, ok_, raises
from redisORM import redis_model

r = redis.StrictRedis("localhost", db=0)
redis_model.redis = r


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


def test_existing_data():
    redis_model.redis.set("test:test10:fname", "Josh")
    redis_model.redis.set("test:test10:lname", "Ashby")
    redis_model.redis.set("test:test10:major", "ECE - Computer Engineer")
    redis_model.redis.rpush("test:test10:hobbies", "Programming", "Electronics", "Photography")

    a = redis_model.RedisModel(namespace="test", key="test10")
    eq_(a.fname, "Josh")
    eq_(a.lname, "Ashby")
    eq_(a.major, "ECE - Computer Engineer")
    eq_(a.hobbies, ["Programming", "Electronics", "Photography"])


@raises(redis_model.RedisORMException)
def test_existing_data_other_types():
    redis_model.redis.sadd("test:test11:wat", "this")
    redis_model.RedisModel(namespace="test", key="test11")


def test_delete_with_keys():
    a = redis_model.RedisModel(namespace="test", key="test12")
    a.name = "Fred"
    a.who = "Fred?"
    a.nickname = "fred"
    a.delete()


def test_none_attribute():
    a = redis_model.RedisModel(namespace="test", key="test13")
    a.ship = None
    eq_(a.ship, "")


@raises(redis_model.RedisORMException)
def test_no_key():
    redis_model.RedisModel(namespace="test")


def teardown_module(module):
    for key in module.r.keys("test:*"):
        module.r.delete(key)
