from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from future.builtins import *

import unittest
import json
import responses

class ResponseMockTestCase(unittest.TestCase):
    def setUp(self):
        responses.start()

    def tearDown(self):
        responses.stop()
        responses.reset()

    def addResponse(self, url, json_body, status=200, is_api_url=True):
        if is_api_url:
            full_url = "https://money.yandex.ru/api/{}".format(url)
        else:
            full_url = url
        responses.add(responses.POST,
                      full_url,
                      body=json.dumps(json_body),
                      status=status,
                      content_type="application/json"
                      )
