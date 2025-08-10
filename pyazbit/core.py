# -*- coding:utf-8 -*-
import hashlib
import hmac
import json
from pprint import pprint
# from urllib.parse import quote
from typing import Text
from urllib.parse import urlencode

import requests


class PyAzBit:
    """API Wrapper"""

    _api_url = 'https://data.azbit.com/api'

    def __init__(self, apikey, secret):
        self._headers = {
            'Content-Type': 'application/json',
            'API-PublicKey': apikey,
            'API-Signature': '',
        }
        self.secret = secret

    def _signature(self, end_point=None, **params):
        params = dict(params)
        _request_args = {
            'timeout': 60,
            'url': f'{self._api_url}/{end_point}',
            'method': params.pop('method', 'GET'),
            'headers': self._headers
        }

        if _request_args['method'].casefold() == 'get':
            _request_args['params'] = params
            message = self.apikey + end_point + urlencode(params or {})
        elif _request_args['method'].casefold() in ('post',):
            _request_args['json'] = params
            message = self.apikey + end_point + json.dumps(params or {})

        else:
            raise ValueError(f'Invalid HTTP method {_request_args.get("method")}')

        signature = hmac.new(self.secret.encode('utf-8'), message.encode('utf-8'), hashlib.sha256)
        self._headers['API-Signature'] = signature.hexdigest()
        _request_args['headers'] = self._headers
        pprint(_request_args)
        resp = requests.request(**_request_args, timeout=60)
        if resp.ok:
            return resp.json()
        else:
            resp.raise_for_status()

    @property
    def apikey(self) -> Text:
        """API key getter.

        :return:
        """
        return self._headers.get('API-PublicKey', '')

    @apikey.setter
    def apikey(self, value: Text):
        self._headers['API-PublicKey'] = value or ''

    def get_currencies(self):
        """Get supported currencies by exchange.

        :return: supported currencies by exchange.
        """
        return self._signature('currencies')
