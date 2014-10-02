.. figure:: https://travis-ci.org/raymank26/yandex-money-sdk-python.svg?branch=master
   :alt: 

Requirements
------------

1. Python 2.7 or Python 3.x
2. pip

Links
-----

1. Yandex.Money API page: `Ru <http://api.yandex.ru/money/>`_,
   `En <http://api.yandex.com/money/>`_

Getting started
---------------

Installation
~~~~~~~~~~~~

1. Install it with ``pip install yandex-money-sdk-python``
2. Paste ``from yandex_money.api import WalletPayment, ExternalPayment``
   to your source code

Payments from the Yandex.Money wallet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Call ``WalletPayment.build_obtain_token_url`` and point user browser
   to resulted url. Where ``client_id``, ``redirect_uri``,
   ``client_secret`` are parameters that you get, when
   `register <https://sp-money.yandex.ru/myservices/new.xml>`__ your app
   in Yandex.Money API.

    .. code:: python

        auth_url = WalletPayment.buildObtainTokenUrl(client_id,
            redirect_uri, scope, client_secret)

2. After that, user fills Yandex.Money form and Yandex.Money service
   redirects browser to ``redirect_uri`` on your server with ``code``
   GET param.

3. You should immediately exchange ``code`` with ``access_token`` using
   ``getAccessToken``

   .. code:: python

       access_token = WalletPayment.get_access_token(client_id, code, redirect_uri,
               client_secret=None)

   Feel free to save ``access_token`` in your database. But don't show
   ``access_token`` to anybody.

4. Now you can use Yandex.Money API

.. code:: python

    api = WalletPayment(access_token)

get account info
================

.. code:: python

    acount_info = api.account_info()

get operation history with last 3 records
=========================================

.. code:: python

    operation_history = api.operation_history({"records": 3})
    # check status

make request payment
====================

.. code:: python

    request_payment = api.request({ "pattern_id": "p2p", "to":
    money_wallet, "amount_due": amount_due, "comment": comment,
    "message": message, "label": label, })
    # check status

call process payment to finish payment
======================================

.. code:: python

    process_payment = api.process({ "request_id":
    request_payment.request_id, }) # Payments from bank cards
    without authorization

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
2. Install ``tox``
3. Run ``tox`` in repo root directory

