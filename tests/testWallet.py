from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from future.builtins import *
from future.moves.urllib.parse import urlencode

import unittest
import json

from yandex_money.api import Wallet
from yandex_money import exceptions
from .constants import CLIENT_ID, ACCESS_TOKEN


class WalletTestSuite(unittest.TestCase):
    def setUp(self):
        super(WalletTestSuite, self).setUp()
        self.api = Wallet(ACCESS_TOKEN)

    def assert_auth_header_present(self):
        pass

    def testAccountInfo(self):
        response = self.api.account_info()
        self.assert_auth_header_present()

    def testGetAuxToken(self):
        token = "some_aux_token"

        response = self.api.get_aux_token(["account-info", "operation-history"])

        self.assertIn('aux_token', response)

    def testOperationHistory(self):
        options = {"records": 3}
        response = self.api.operation_history(options)

    def testOperationDetails(self):
        pass

    def testRequestPayment(self):
        options = {
            "pattern_id": "p2p",
            "to": "410011161616877",
            "amount_due": "0.02",
            "comment": "test payment comment from yandex-money-python",
            "message": "test payment message from yandex-money-python",
            "label": "testPayment",
            "test_payment": True,
            "test_result": "success"
        };

        response = self.api.request_payment(options)
        self.assertEqual(response['status'], 'success')

    def testResponsePayment(self):
        options = {
            "request_id": "test-p2p",
            "test_payment": True,
            "test_result": "success"
        }

        response = self.api.process_payment(options)
        self.assertEqual(response['status'], 'success')

    def testIncomingTransferAccept(self):
        #self.addResponse("incoming-transfer-accept", {"status": "success"})
        operation_id = "some id"
        protection_code = "some code" # TODO: test when it's None

        response = self.api.incoming_transfer_accept(
            operation_id=operation_id,
            protection_code=protection_code
        )
        self.assertEqual(response['status'], "refused")

    def testIncomingTransferReject(self):
        #self.addResponse("incoming-transfer-reject", {"status": "success"})
        operation_id = "some operatoin id"
        response = self.api.incoming_transfer_reject(
            operation_id=operation_id,
        )

    def testObtainTokenUrl(self):
        client_id = "client-id"
        url = Wallet.build_obtain_token_url(
            "client-id",
            "http://localhost/redirect",
            ["account-info", "operation_history"]
        )
        # TODO: check url

    def testGetAccessToken(self):
        options = {
            "code": "code",
            "client_id": "client_id",
            "grant_type": "authorization_code",
            "redirect_uri": "redirect_uri",
            "client_secret": "client_secret" 
            }
        response = Wallet.get_access_token(
            code=options["code"],
            client_id=options["client_id"],
            redirect_uri=options["redirect_uri"],
            client_secret=options["client_secret"]
        )
        self.assertEqual(response['error'], 'unauthorized_client')

