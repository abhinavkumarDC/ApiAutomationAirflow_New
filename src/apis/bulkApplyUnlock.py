import os
import requests
import json

from utils.helpers import Helpers


class Bulk_unlock:
    def __init__(self, config, token):
        self.bulk_unlock_url = config.bulk_unlock_url
        self.token = token
        self.input_dir = config.input_dir
        self.input_csv_file_path = os.path.join(self.input_dir, 'Unlock_File_with_sample_2imei.csv')

    def bulk_apply_unlock(self):
        headers = {
            'Authorization': f'Bearer {self.token}'
        }

        # Generate a random TransactionId
        transaction_id = Helpers.generate_random_transaction_id()

        files = {
            'file': open(self.input_csv_file_path, 'rb'),
            'TransactionId': (None, transaction_id)
        }
        # data = {
        #     'TransactionId': transaction_id
        # }
        print(f"Sending PUT request to {self.bulk_unlock_url} with TransactionId: {transaction_id}")
        response = requests.put(self.bulk_unlock_url, headers=headers, files=files)
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
