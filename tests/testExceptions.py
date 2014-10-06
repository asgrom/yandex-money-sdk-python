from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from future.builtins import *
import unittest
from yandex_money import exceptions
from yandex_money.api import Wallet

class ExceptionsTestSuite(unittest.TestCase):
    def setUp(self):
        self.api = Wallet("TEST TOKEN")

    def testRevokeTokenFormatError(self):
        self.assertRaises(exceptions.FormatError, Wallet.revoke_token,
                          "misspelled token")

    def testRevokeTokenScopeError(self):
        self.assertRaises(exceptions.TokenError, Wallet.revoke_token,
                          "someoktoken")

    #@responses.activate
    #def testTokenError(self):
        #self.assertRaises(exceptions.TokenError, self.api.account_info)
