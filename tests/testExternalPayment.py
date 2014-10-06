from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from future.builtins import *
from future.moves.urllib.parse import urlencode

import unittest

from yandex_money.api import ExternalPayment
from yandex_money import exceptions

from .constants import CLIENT_ID, ACCESS_TOKEN


class ExternalTestSuite(unittest.TestCase):
    def setUp(self):
        super(ExternalTestSuite, self).setUp()

    def makeRequest(self):
        instance_id = ExternalPayment.get_instance_id(CLIENT_ID)['instance_id']

        api = ExternalPayment(instance_id)
        options = {
            "instance_id": instance_id,
            "pattern_id": "p2p",
            "to": "410011161616877",
            "amount_due": "0.02",
            "comment": "test payment comment from yandex-money-python",
            "message": "test payment message from yandex-money-python",
            "label": "testPayment",
            "test_payment": True,
            "test_result": "success"
        }
        return api.request(options), api

    def testGetInstanceId(self):
        response = ExternalPayment.get_instance_id(CLIENT_ID)
        self.assertEqual(response['status'], "success")

    def testRequestExternalPayment(self):
        response, _ = self.makeRequest()
        self.assertIn('request_id', response)
    
    def testProcessExternalPayment(self):
        response, api = self.makeRequest()

        options = {
            "request_id": response['request_id'],
            "ext_auth_success_uri": "http://lcoalhost:8000",
            "ext_auth_fail_uri": "http://localhost:8000"
        }

        response = api.process(options)
        options['instance_id'] = "some instance id"
        self.assertEqual(response['status'], "ext_auth_required")


