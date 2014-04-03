RedisORM v0.1.0 - DEV
=====================

Build status - Master:

.. image:: https://secure.travis-ci.org/JoshAshby/pyRedisORM.png?branch=master
        :target: http://travis-ci.org/JoshAshby/pyRedisORM

.. image:: https://coveralls.io/repos/JoshAshby/pyRedisORM/badge.png
        :target: https://coveralls.io/r/JoshAshby/pyRedisORM

.. image:: https://pypip.in/v/RedisORM/badge.png
    :target: https://crate.io/packages/RedisORM/
    :alt: Latest PyPI version

.. image:: https://pypip.in/d/RedisORM/badge.png
    :target: https://crate.io/packages/RedisORM/
    :alt: Number of PyPI downloads

Build status - Dev:

.. image:: https://secure.travis-ci.org/JoshAshby/pyRedisORM.png?branch=dev
        :target: http://travis-ci.org/JoshAshby/pyRedisORM

There is a small test suite provided. It requires an actuall Redis install that
is up and running. If you want too change the address then please take a look
in the test directory. The tests are automatically ran each commit,
thanks to `travis-ci.org <http://travis-ci.org>`__ and coverage is provided by
`Coveralls.io <http://coveralls.io>`__ and this documentation
is kindly hosted and automatically rebuilt by `readthedocs.org
<http://readthedocs.org>`__.

If you like the work I do and find this project helpful, please consider a
small donation to help fund me and this project:

.. raw:: html

    <iframe style="border: 0; margin: 0; padding: 0;"
        src="https://www.gittip.com/JoshAshby/widget.html"
        width="48pt" height="22pt"></iframe>

A Few Minor Warnings
--------------------

#. I'm only a second year university student, and software
   isn't even my major; I'm working towards an Electrical and Computer
   Engineering degree, so not only do I have limited time to keep this
   maintained, but I also probably won't write the best code ever.
#. This is a very early release, things might break, and the code is honestly a
   little childish at best. In other words: It'll hopefully get better, but it
   might be a little limited right now.
#. This project follows the semantic versioning specs. All Minor and
   patch versions will not break the major versions API, however an bump of the
   major version signifies that backwards compatibility will most likely be
   broken.

Quick start
-----------

.. automodule:: redisORM.redis_model

Contributing
------------

All code for this can be found online at
`github <https://github.com/JoshAshby/pyRedisORM>`__.
If something is broken, or a feature is missing, please submit a pull request
or open an issue. Most things I probably won't have time to get around to
looking at too deeply, so if you want it fixed, a pull request is the way
to go. In your pull request please provide an explanation as to what your
request is for, and what benefit it provides. Also, please try to match the
style of the code, or make sure your code is nearly all PEP8 compliant just to
maintain code consistency.

Besides that, this project is licensed under the MIT License as found in the
``LICENSE.txt`` file. Enjoy!

Documentation
=============

Exceptions
----------

.. autoclass:: redisORM.redis_model.RedisORMException

Model Class
-----------

.. autoclass:: redisORM.redis_model.RedisModel
    :members:
    :undoc-members:

Helper Classes
--------------

.. autoclass:: redisORM.redis_model.RedisList
    :members:
    :undoc-members:

.. autoclass:: redisORM.redis_model.RedisKeys
    :members:
    :undoc-members:
