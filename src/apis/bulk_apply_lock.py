import pandas as pd
import requests
import json


class Bulk_apply_lock:
    def __init__(self, bulk_lock_url, token, lock_csv_file, transaction_id):
        self.bulk_lock_url = bulk_lock_url
        self.token = token
        self.lock_csv_file = lock_csv_file
        self.transaction_id = transaction_id

    def apply_bulk_lock_v3(self):
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        files = {
            'file': open(self.lock_csv_file, 'rb'),
            'TransactionId': self.transaction_id
        }
        print(f"Sending PUT request to {self.bulk_lock_url} with TransactionId: {self.transaction_id}")
        response = requests.put(self.bulk_lock_url, headers=headers, files=files)
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
