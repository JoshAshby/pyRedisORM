#!/usr/bin/env python
from .redis_model import RedisModel, RedisList, RedisORMException, RedisKeys

__version__ = '0.2.0'
VERSION = tuple(map(int, __version__.split('.')))

__all__ = ["RedisModel", "RedisList", "RedisORMException", "RedisKeys"]
