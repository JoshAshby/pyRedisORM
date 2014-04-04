from setuptools import setup

version = '0.1.0'

testing_extras = ['nose', 'coverage']

docs_extras = ['Sphinx']

setup(
    name='RedisORM',
    version=version,
    description="Simple little ORM thing for Redis",
    long_description=open("README.rst").read(),
    classifiers=[
        "Development Status :: 3 - Alpha",
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
    install_requires=['redis'],
    zip_safe=True,
    test_suite='nose.collector',
    tests_require=['nose'],
    extras_require = {
        'testing':testing_extras,
        'docs':docs_extras,
        },
)
