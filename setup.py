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
    test_suite = 'tests',
    tests_requires = [
        "responses"
    ]
    # author = 'Peter Downs',
    # author_email = 'peterldowns@gmail.com',
    # url = 'https://github.com/peterldowns/mypackage', # use the URL to the github repo
    # download_url = 'https://github.com/peterldowns/mypackage/tarball/0.1', # I'll explain this in a second
    # keywords = ['testing', 'logging', 'example'], # arbitrary keywords
    # classifiers = [],
)
