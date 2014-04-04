RedisORM v0.1.0
===============

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


RedisORM is just a quick and simple little Key-Value group to Python Object
mapper that makes it easier to have somewhat more complex structures in Redis.
While a similar structure could be achieved by using a Redis hash, this module
also allows for lists and future support for Redis data
structures is hopefully planed, making this more helpful than basic hashs.

There is a small test suite provided. It requires an actual Redis install that
is up and running. If you want too change the address then please take a look
in the test directory. The tests are automatically ran each commit,
thanks to `travis-ci.org <http://travis-ci.org>`__ and coverage is provided by
`Coveralls.io <http://coveralls.io>`__ and this documentation
is kindly hosted and automatically rebuilt by `readthedocs.org
<http://readthedocs.org>`__.


A Few Minor Warnings
--------------------
#. This is a very early release, and although I've been using a large part of
   this code for about a year now, things are still going to break and not
   function well. Don't be afraid to submit a bug report or a patch on Github
   to fix something.
#. I'm only a second year university student, and software
   isn't even my major; I'm working towards an Electrical and Computer
   Engineering degree, so not only do I have limited time to keep this
   maintained, but I also probably won't write the best code ever.
#. This project follows the semantic versioning specs. All Minor and
   patch versions will not break the major versions API, however a bump of the
   major version signifies that backwards compatibility will most likely be
   broken in some way.

Documentation
=============
For more information, a short quick start, and information about running the
test suit, please `read the documentation
<https://pyredisorm.readthedocs.org/en/latest/>`__ kindly hosted
on `readthedocs.org <http://readthedocs.org>`__

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
