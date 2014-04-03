from setuptools import setup

version = '0.1.0'

testing_extras = ['nose', 'coverage']

docs_extras = ['Sphinx']

setup(
    name='RedisORM',
    version=version,
    description="Simple little ORM thing for Redis",
    long_description="""\
RedisORM provides a simple ORM, or what I like to call a: Key-Value to Grouped Object Mapper.
Currently it just supports strings and lists but I plan on supporting more later on.

* `Docs <https://pyredisorm.readthedocs.org/en/latest/>`_
* `Bug tracker <https://github.com/JoshAshby/pyRedisORM/issues>`_
* `Browse source code <https://github.com/JoshAshby/pyRedisORM/>`_
""",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='redis orm database',
    author='Joshua P Ashby',
    author_email='joshuaashby@joshashby.com',
    maintainer='Joshua P Ashby',
    url='https://github.com/JoshAshby/pyRedisORM/',
    license='MIT',
    packages=['redisORM'],
    zip_safe=True,
    test_suite='nose.collector',
    tests_require=['nose'],
    extras_require = {
        'testing':testing_extras,
        'docs':docs_extras,
        },
)
