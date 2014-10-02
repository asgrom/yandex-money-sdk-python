from setuptools import setup
from os import path
here = path.abspath(path.dirname(__file__))

setup(
    name='yandex-money-sdk-python',
    version='0.1.0',
    description='SDK yandex money API',
    license='MIT',
    author="NBCO Yandex.Money LLC",
    maintainer="Anton Ermak",
    maintainer_email='ermak@yamoney.ru',
    packages = ['yandex_money'],
    keywords = "sdk yandex money",
    package_data={'': ['LICENSE', ]},
    install_requires=[
        'requests>2.4.0',
        "future",
        "six"
    ],
    test_suite = 'nose.collector',
    tests_require = [
        "responses",
        "nose"
    ],
    classifiers = [
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 2.7",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha"
    ]
)
