|Build Status| |Coverage Status|

Python Yandex.Money API SDK
===========================

Requirements
------------

1. Python 2.7 or Python 3.x
2. pip

Links
-----

1. Yandex.Money API page: `Ru <http://api.yandex.ru/money/>`__,
   `En <http://api.yandex.com/money/>`__

Getting started
---------------

Installation
~~~~~~~~~~~~

1. Install it with ``pip install yandex-money-sdk``
2. Paste ``from yandex_money.api import WalletPayment, ExternalPayment``
   to your source code

Payments from the Yandex.Money wallet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using Yandex.Money API requires following steps

1. Obtain token URL and redirect user's browser to Yandex.Money service.
   Note: ``client_id``, ``redirect_uri``, ``client_secret`` are
   constants that you get, when
   `register <https://sp-money.yandex.ru/myservices/new.xml>`__ app in
   Yandex.Money API.

   .. code:: python

       scope = ['account-info', 'operation-history'] # etc..
       auth_url = WalletPayment.buildObtainTokenUrl(client_id,
           redirect_uri, scope, client_secret)

2. After that, user fills Yandex.Money HTML form and user is redirected
   back to ``REDIRECT_URI?code=CODE``.

3. You should immediately exchange ``CODE`` with ``ACCESS_TOKEN``.

   .. code:: python

       access_token = WalletPayment.get_access_token(client_id, code, redirect_uri,
           client_secret=None)

4. Now you can use Yandex.Money API.

   .. code:: python

       account_info = api.account_info()
       balance = account_info['balance'] # and so on

       request_options = {
           "pattern_id": "p2p",
           "to": "410011161616877",
           "amount_due": "0.02",
           "comment": "test payment comment from yandex-money-python",
           "message": "test payment message from yandex-money-python",
           "label": "testPayment",
           "test_payment": true,
           "test_result": "success"
       };
       request_result = api.request(request_options)
       # check status

       process_payment = api.process({
           "request_id": request_result['request_id'],
       })
       # check result
       if process_payment['status'] == "success":
           # show success page
       else:
           # something went wrong

Payments from bank cards without authorization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Fetch instantce-id(ussually only once for every client. You can store
   result in DB).

   .. code:: python

       response = ExternalPayment.get_instance_id(client_id)
       if reponse.status == "success":
           instance_id = response.instance_id;
       else:
           # throw exception with reponse->error message

2. Make request payment

   .. code:: python

       # make instance
       external_payment = ExternalPayment(instance_id);

       payment_options = {
           # pattern_id, etc..
       }
       response = external_payment.request(payment_options)
       if response.status == "success":
           request_id = response.request_id
       else: 
           # throw exception with response->message

3. Process the request with process-payment.

   .. code:: python

       process_options = {
           "request_id": request_id
           # other params..
       }
       result = external_payment.process(process_options)
       # process result according to docs

Running tests
-------------

1. Clone this repo.
2. Create ``tests/constants.python`` file with ``ACCESS_TOKEN`` and
   ``CLIENT_ID`` constants.
3. Install ``tox``
4. Run ``tox`` in repo root directory

.. |Build Status| image:: https://travis-ci.org/yandex-money/yandex-money-sdk-python.svg?branch=master
   :target: https://travis-ci.org/yandex-money/yandex-money-sdk-python
.. |Coverage Status| image:: https://coveralls.io/repos/yandex-money/yandex-money-sdk-python/badge.png?branch=master
   :target: https://coveralls.io/r/yandex-money/yandex-money-sdk-python?branch=master
