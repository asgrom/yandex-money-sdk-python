from setuptools import setup
from os import path
here = path.abspath(path.dirname(__file__))

setup(
    name='yandex-money-sdk-python',
    version='0.0.1',
    description='SDK yandex money API',
    license='MIT',
    packages = ['yandex_money'], # this must be the same as the name above
    install_requires=[
        'requests>2.4.0',
        "future",
        "six"
    ],
    test_suite = 'nose.collector',
    tests_require = [
        "responses",
        "nose"
    ]
)
