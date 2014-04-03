import redis
from nose.tools import eq_, ok_, raises
from redisORM import redis_model

redis_model.redis = redis.StrictRedis("localhost", db=0)

def test_new_model():
    redis_model.RedisModel(namespace="test", key="test1")


def test_del_model():
    a = redis_model.RedisModel(namespace="test", key="test2")
    a.delete()


def test_string_only_model():
    a = redis_model.RedisModel(namespace="test", key="test3")
    a.time = "now"

    eq_(a.time, "now", "Model data doesn't match - getattr")
    eq_(a["time"], "now", "Model data doesn't match - getitem")

    b = redis_model.redis.get("test:test:time")

    eq_(b, "now", "Raw redis data doesn't match")


@raises(KeyError)
def test_delitem():
    a = redis_model.RedisModel(namespace="test", key="test3")
    a.time = "now"
    del a["time"]
    assert a.time is not None



def test_list_of_strings_only_model():
    list_fixture = ["one", "two", "three"]
    a = redis_model.RedisModel(namespace="test", key="test4")
    a.things = list_fixture

    for entry in list_fixture:
        ok_(entry in a.things, "Item missing from model list data: {}".format(entry))


def test_list_of_ints_only_model():
    list_fixture = [1, 2, 3]
    a = redis_model.RedisModel(namespace="test", key="test5")
    a.things = list_fixture

    for entry in list_fixture:
        ok_(entry in a.things, "Item missing from model list data: {}".format(entry))


def test_list_of_strings_and_ints_only_model():
    list_fixture = ["one", "two", "three", 1, 2, 3]
    a = redis_model.RedisModel(namespace="test", key="test6")
    a.things = list_fixture

    for entry in list_fixture:
        ok_(entry in a.things, "Item missing from model list data: {}".format(entry))


@raises(redis_model.RedisORMException)
def test_keys_exception():
    redis_model.RedisKeys(key=None)
