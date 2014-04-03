import redis
from nose.tools import eq_, assert_raises
from redisORM import redis_model

redis_model.redis = redis.StrictRedis("localhost", db=0)

def test_new_model():
    a = redis_model.RedisModel(namespace="test", key="test")
    a.time = "now"

    eq_(a.time, "now", "Model data doesn't match")

    b = redis_model.redis.get("test:test:time")

    eq_(b, "now", "Raw redis data doesn't match")
