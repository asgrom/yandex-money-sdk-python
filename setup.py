from setuptools import setup
from os import path
from codecs import open
import sys
import os
here = path.abspath(path.dirname(__file__))

with open("README.rst", "r", "utf-8") as f:
    readme = f.read()

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name='yandex-money-sdk',
    version='0.1.3',
    description='SDK yandex money API',
    license='MIT',
    author="NBCO Yandex.Money LLC",
    long_description=readme,
    maintainer="Anton Ermak",
    maintainer_email='ermak@yamoney.ru',
    packages=['yandex_money'],
    keywords="sdk yandex money",
    package_data={'': ['LICENSE', ]},
    install_requires=[
        'requests>2.4.0',
        "future",
        "six"
    ],
    test_suite='nose.collector',
    tests_require=[
        "nose"
    ],
    classifiers=[
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 2.7",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha"
    ]
)
