from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from future.builtins import *

import unittest
from yandex_money.api import WalletPayment
from yandex_money import exceptions
from .base import ResponseMockTestCase
import responses
import json
import urllib.parse


class WalletTestSuite(ResponseMockTestCase):
    def setUp(self):
        super(WalletTestSuite, self).setUp()
        self.api = WalletPayment("TEST TOKEN")

    def assert_auth_header_present(self):
        self.assertEqual("Bearer TEST TOKEN",
                      responses.calls[0].request.headers['Authorization'],
                      )

    def testAccountInfo(self):
        self.addResponse("account-info",
            {"status": "success"}
        )
        response = self.api.account_info()
        self.assertEqual(response['status'], "success")

        self.assert_auth_header_present()

    def testGetAuxToken(self):
        token = "some_aux_token"

        self.addResponse("token-aux", {"aux_token": token})

        response = self.api.get_aux_token(["account-info", "operation-history"])

        self.assertEqual(response['aux_token'], token)
        self.assertEqual(responses.calls[0].request.body,
                "scope=account-info+operation-history")

    def testOperationHistory(self):
        options = {"foo": "bar", "foo2": "bar2"}

        self.addResponse("operation-history", [])

        response = self.api.operation_history(options)
        self.assertEqual(response, [])
        self.assertEqual(responses.calls[0].request.body,
                urllib.parse.urlencode(options)
        )

    def testRequestPayment(self):
        self.addResponse("request-payment", {"status": "success"})
        options = {
            "foo": "bar",
            "foo2": "bar2",
        }

        response = self.api.request(options)
        self.assertEqual(response, {"status": "success"})
        self.assertEqual(responses.calls[0].request.body,
                urllib.parse.urlencode(options)
        )

    def testResponsePayment(self):
        self.addResponse("process-payment", {"status": "success"})
        options = {
            "foo": "bar",
            "foo2": "bar2",
        }

        response = self.api.process(options)
        self.assertEqual(response, {"status": "success"})
        self.assertEqual(responses.calls[0].request.body,
                urllib.parse.urlencode(options)
        )

    def testIncomingTransferAccept(self):
        self.addResponse("incoming-transfer-accept", {"status": "success"})
        options = {
            "foo": "bar",
            "foo2": "bar2",
        }
        operation_id = "some id"
        protection_code = "some code" # TODO: test when it's None

        response = self.api.incoming_transfer_accept(
            operation_id=operation_id,
            protection_code=protection_code
        )
        self.assertEqual(response, {"status": "success"})
        self.assertEqual(
            responses.calls[0].request.body,
            urllib.parse.urlencode({
                "operation_id": operation_id,
                "protection_code": protection_code 
            })
        )

    def testIncomingTransferReject(self):
        self.addResponse("incoming-transfer-reject", {"status": "success"})
        operation_id = "some id"
        response = self.api.incoming_transfer_reject(
            operation_id=operation_id,
        )
        self.assertEqual(response, {"status": "success"})
        self.assertEqual(
            responses.calls[0].request.body,
            urllib.parse.urlencode({
                "operation_id": operation_id,
            })
        )
    def testObtainTokenUrl(self):
        client_id = "client-id"
        url = WalletPayment.build_obtain_token_url(
            "client-id",
            "http://localhost/redirect",
            ["account-info", "operation_history"]
        )
        # TODO: check url

    def testGetAccessToken(self):
        self.addResponse(WalletPayment.SP_MONEY_URL + "/oauth/token",
                         {"status": "success"},
                         is_api_url=False
                         )
        options = {
            "code": "code",
            "client_id": "client_id",
            "grant_type": "authorization_code",
            "redirect_uri": "redirect_uri",
            "client_secret": "client_secret" 
            }
        response = WalletPayment.get_access_token(
            code=options["code"],
            client_id=options["client_id"],
            redirect_uri=options["redirect_uri"],
            client_secret=options["client_secret"]
        )
        self.assertEqual(response, {"status": "success"})
        self.assertEqual(
            responses.calls[0].request.body,
            urllib.parse.urlencode(options)
        )

    def testRevokeToken(self):
        self.addResponse("revoke", {"status": "success"})
        WalletPayment.revoke_token("TEST TOKEN")
        self.assert_auth_header_present()




















