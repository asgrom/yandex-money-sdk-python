from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from future.builtins import *

import unittest
from yandex_money.api import ExternalPayment
from yandex_money import exceptions
from .base import ResponseMockTestCase
import responses
import json
import urllib.parse


class ExernalTestSuite(ResponseMockTestCase):
    def setUp(self):
        super(ExernalTestSuite, self).setUp()
        self.api = ExternalPayment("some instance id")

    def testGetInstanceId(self):
        self.addResponse("instance-id",
                         {"status": "success"}
                         )
        response = ExternalPayment.get_instance_id("client_id")
        self.assertEqual(response['status'], "success")
        self.assertEqual(
            responses.calls[0].request.body,
            urllib.parse.urlencode({"client_id": "client_id"})
        )
    def testRequestExternalPayment(self):
        self.addResponse("request-external-payment",
                         {"status": "success"})
        options = {
            "foo": "bar"
        }
        response = self.api.request(options)
        options['instance_id'] = "some instance id"
        self.assertEqual(response['status'], "success")
        self.assertEqual(
            responses.calls[0].request.body,
            urllib.parse.urlencode(options)
        )
    

    def testProcessExternalPayment(self):
        self.addResponse("process-external-payment",
                         {"status": "success"})
        options = {
            "foo": "bar"
        }
        response = self.api.process(options)
        options['instance_id'] = "some instance id"
        self.assertEqual(response['status'], "success")
        self.assertEqual(
            responses.calls[0].request.body,
            urllib.parse.urlencode(options)
        )


