from distutils.core import setup
import redisORM

setup(
    name='RedisORM',
    version=redisORM.__version__,
    author='Joshua P Ashby',
    author_email='joshuaashby@joshashby.com',
    packages=['redisORM', 'redisORM.tests'],
    url='https://github.com/JoshAshby/pyRedisORM',
    license='MIT (See LICENSE.txt for more info)',
    description='Simple little ORM for working with Redis',
    long_description=open('README.rst').read(),
    install_requires=[
        "nose >= 1.3.0"
    ],
)
