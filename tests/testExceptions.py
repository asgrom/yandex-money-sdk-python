from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from future.builtins import *
import unittest
from yandex_money import exceptions
from yandex_money.api import Wallet
import responses

class ExceptionsTestSuite(unittest.TestCase):
    def setUp(self):
        self.api = Wallet("TEST TOKEN")

    @responses.activate
    def testFormatError(self):
        responses.add(responses.POST,
                "https://money.yandex.ru/api/account-info",
                body='',
                status=400,
                content_type="application/json"
        )
        self.assertRaises(exceptions.FormatError, self.api.account_info)

    @responses.activate
    def testScopeError(self):
        responses.add(responses.POST,
                "https://money.yandex.ru/api/account-info",
                body='',
                status=401,
                content_type="application/json"
        )
        self.assertRaises(exceptions.ScopeError, self.api.account_info)

    @responses.activate
    def testTokenError(self):
        responses.add(responses.POST,
                "https://money.yandex.ru/api/account-info",
                body='',
                status=403,
                content_type="application/json"
        )
        self.assertRaises(exceptions.TokenError, self.api.account_info)
