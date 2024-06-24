import pandas as pd
import requests
import json
import os
import time
import uuid


class Bulk_release_devices:
    def __init__(self, bulk_release_url, token, release_csv_file_path, transaction_id):
        self.bulk_release_url = bulk_release_url
        self.token = token
        self.release_csv_file_path = release_csv_file_path
        self.transaction_id = transaction_id

    def send_device_data_in_csv(self):
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        files = {
            'file': open(self.release_csv_file_path, 'rb'),
            'TransactionId': self.transaction_id
        }
        # data = {
        #     'TransactionId': self.transaction_id
        # }
        print(f"Sending PUT request to {self.bulk_release_url} with TransactionId: {self.transaction_id}")
        response = requests.put(self.bulk_release_url, headers=headers, files=files)
        if response.status_code == 200:
            print("PUT request successful")
            try:
                print(f"Response: {response.json()}")
            except json.JSONDecodeError:
                print("Response is not in JSON format")
                print(f"Response text: {response.text}")
            return True  # Success
        elif response.status_code == 464:
            print(f"PUT request failed with status 464: {response.text}")
            return False  # Specific failure
        else:
            print(f"PUT request failed: {response.status_code}")
            print(f"Response: {response.text}")
            return False  # General failure
