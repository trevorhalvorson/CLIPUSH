import os
import json
import requests


class PushyAPI:
    @staticmethod
    def send_push_notification(data):
        # TODO: store using AWS KMS or S3
        api_key = os.environ.get("PUSHY_API_KEY")
        url = 'https://api.pushy.me/push?api_key=' + api_key
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response
