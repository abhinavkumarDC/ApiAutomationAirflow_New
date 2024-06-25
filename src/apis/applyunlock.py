import pandas as pd
import requests
import json
import os
import time
import uuid


class Apply_unlock:
    def __init__(self, apply_unlock_url, token):
        self.apply_unlock_url = apply_unlock_url
        self.token = token

    def send_imei_for_unlock(self):
        headers = {
            'content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}'
        }

        payload = {
            'imei1': '866671068836775',
            'TransactionId': str(uuid.uuid4())
        }

        response = requests.post(self.apply_unlock_url, json=payload, headers=headers)
        print(f"Sending post request to {self.apply_unlock_url} with the payload of Imei and transactionId")
        if response.status_code == 200:
            print("POST request successful")
            return response.json()
        elif response.status_code == 499:
            print(f"Post request failed with status code 499 {response.text}")
            return False
        elif response.status_code == 460:
            print(f"Post request executed successful with status code 460 {response.text}")
            return True
        else:
            print(f"Failed to fetch data: {response.status_code}")
            print(f"Response: {response.text}")
