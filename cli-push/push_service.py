import json
import requests


class Service(object):
    def __init__(self, post_data):
        self.post_data = post_data
        self.url = 'https://y49o5tutu1.execute-api.us-west-2.amazonaws.com/dev/notify/device'
        self.headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    # send POST method request to backend service with provided data
    def post(self):
        return requests.post(self.url, headers=self.headers, data=json.dumps(self.post_data))
