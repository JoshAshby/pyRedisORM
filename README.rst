RedisORM v0.1.0 - DEV
=====================

Build status - Master:


.. image:: https://secure.travis-ci.org/JoshAshby/pyRedisORM.png?branch=master
        :target: http://travis-ci.org/JoshAshby/pyRedisORM

.. image:: https://pypip.in/v/RedisORM/badge.png
    :target: https://crate.io/packages/RedisORM/
    :alt: Latest PyPI version

.. image:: https://pypip.in/d/RedisORM/badge.png
    :target: https://crate.io/packages/RedisORM/
    :alt: Number of PyPI downloads


Build status - Dev:


.. image:: https://secure.travis-ci.org/JoshAshby/pyRedisORM.png?branch=dev
        :target: http://travis-ci.org/JoshAshby/pyRedisORM

TODO: What is this?

A Few Minor Warnings
--------------------

#. I'm only a second year university student, and software
   isn't even my major; I'm working towards an Electrical and Computer
   Engineering degree, so not only do I have limited time to keep this
   maintained, but I also probably won't write the best code ever.
#. This takes some influence from the `Python Django RedisDB 
   ORM <https://github.com/dparlevliet/rwrapper>`__ and other ORM systems,
   however I haven't really followed a standard pattern for the interface
   for this module. If someone wants to make this more standardized feel
   free to, and just submit a pull request, I'll look it over and probably
   will give it the go ahead. For more information see below.
#. This is a very early release, things might break, and the code is honestly a
   little childish at best. In other words: It'll hopefully get better, but it
   might be a little limited right now.
#. This project follows the semantic versioning specs. All Minor and
   patch versions will not break the major versions API, however an bump of the
   major version signifies that backwards compatibility will most likely be
   broken.


Documentation
=============

Installation:
-------------

::

    pip install RedisORM

For more information, a short quick start, and information about running the
test suit, please `read the documentation
<https://redisorm.readthedocs.org/en/latest/>`__ kindly hosted
on `readthedocs.org <http://readthedocs.org>`__

Contributing
------------

All code for this can be found online at
`github <https://github.com/JoshAshby/pyRedisORM>`__.
If something is broken, or a feature is missing, please submit a pull request
or open an issue. Most things I probably won't have time to get around to
looking at too deeply, so if you want it fixed, a pull request is the way
to go. In your pull request please provide an explaniation as to what your
request is for, and what benefit it provides.

Besides that, I'm releasing this under the MIT License as found in the
``LICENSE.txt`` file. Enjoy!
