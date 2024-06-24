import random
import requests
from utils.helpers import Helpers
import os


class Get_Passcode:
    def __init__(self, get_passcode_url, token):
        self.get_passcode_url = get_passcode_url
        self.token = token
        #self.output_dir = output_dir

    def send_passkey_for_pin_unlock(self):
        headers = {
            'content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}'
        }

        payload = {
            'pass_key': '99554428243'
        }

        response = requests.post(self.get_passcode_url, json=payload, headers=headers)

        print(f"Sending post request to {self.get_passcode_url} with the payload of passkey{payload}")
        if response.status_code == 200:
            print("passcode request successful")
            return response.json()
        elif response.status_code == 406:
            print(f"Post request failed with status code 406 {response.text}")
            return response.json()
        elif response.status_code == 401:
            print(f"Post request failed with status code 401 {response.text}")
            return response.json()
        elif response.status_code == 404:
            print(f"Post request failed with status code 404 {response.text}")
            return response.json()
        elif response.status_code == 400:
            print(f"Post request failed with status code 400 {response.text}")
            return response.json()
        elif response.status_code == 405:
            print(f"Post request failed with status code 405 {response.text}")
            return response.json()
        elif response.status_code == 461:
            print(f"Post request failed with status code 461 {response.text}")
            return response.json()
        else:
            print(f"Failed to fetch data: {response.status_code}")
            print(f"Response: {response.text}")