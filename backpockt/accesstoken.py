import json

import requests


class AccessToken(object):

    def __init__(self, customer_key, request_token):
        self.customer_key = customer_key
        self.request_token = request_token

    def retrieve(self):
        url = 'https://getpocket.com/v3/oauth/authorize'
        headers = {
            'X-Accept': 'application/json',
            'Content-Type': 'application/json; charset=UTF8'}
        payload = {
            'consumer_key': self.customer_key,
            'code': self.request_token}
        r = requests.post(url, headers=headers, data=json.dumps(payload))

        j = r.json()

        return j['access_token']
