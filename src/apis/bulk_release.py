import os
import requests
import json
import uuid
from utils.helpers import Helpers


class Bulk_release_devices:
    def __init__(self, config, token):
        self.bulk_release_url = config.bulk_release_url
        self.token = token
        self.input_dir = config.input_dir
        self.input_csv_file_path = os.path.join(self.input_dir, 'Release_File.csv')

    def send_device_data_in_csv(self):
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        files = {
            'file': open(self.input_dir, 'rb'),
            'TransactionId': str(uuid.uuid4())
        }
        # data = {
        #     'TransactionId': self.transaction_id
        # }
        print(f"Sending PUT request to {self.bulk_release_url} with TransactionId: {self.TransactionId}")
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
