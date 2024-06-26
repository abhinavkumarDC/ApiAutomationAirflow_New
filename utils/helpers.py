import os   # Import the os module to interact with the operating system
import json
import random
import string
import requests
import pandas as pd


class Helpers:
    @staticmethod
    def ensure_output_directory(directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
        # print(f"Output directory ensured at: {directory}")

    @staticmethod
    def store_data_as_json(data, filename):
        # print(f"Storing data as JSON in {filename}")
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        # print(f"Data stored as JSON in {filename}")
        print(f"Data stored as JSON in provided directory")

    @staticmethod
    def store_data_as_csv(data, filename):
        # print(f"Storing data as CSV in {filename}")
        if isinstance(data, dict):
            data = [data]
        elif not isinstance(data, list):
            raise ValueError("Data should be a list or dictionary to store as CSV")
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        # print(f"Data stored as CSV in {filename}")
        print(f"Data stored as csv in provided directory")

    @staticmethod
    def get_random_notification_code(data):
        if isinstance(data, list):
            codes = [item["notification_code"] for item in data if "notification_code" in item]
            if codes:
                code = random.choice(codes)
                print(f"Selected random notification code: {code}")
                return code
            else:
                print("No notification codes found in the data")
                return None
        else:
            print("Data is not in the expected list format")
            return None

    @staticmethod
    def generate_random_transaction_id(length=20):
        transaction_id = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        print(f"Generated TransactionId: {transaction_id}")
        return transaction_id

    @staticmethod
    def fetch_data_from_api(url, token):
        headers = {
            'Authorization': f'Bearer {token}'
        }
        print(f"Fetching data from {url} with token: {token}")
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print("Data fetched successfully")
            return response.json()
        else:
            print(f"Failed to fetch data: {response.status_code}")
            print(f"Response: {response.text}")
            return None

    @staticmethod
    def send_notification_with_csv(api_url, token, notification_code, csv_file_path, transaction_id):
        headers = {
            'Authorization': f'Bearer {token}'
        }
        files = {
            'file': open(csv_file_path, 'rb')
        }
        data = {
            # 'notification_code': notification_code # push_bulk_csv.py
            'notification_code': notification_code,
            'TransactionId': transaction_id
        }
        print(f"Sending POST request to {api_url} with TransactionId: {transaction_id} and file: {files}")
        # print(f"Sending POST request to {api_url} with notification_code: {notification_code} and TransactionId: {transaction_id}")
        response = requests.post(api_url, headers=headers, files=files, data=data)
        if response.status_code == 200:
            print("POST request successful")
            try:
                print(f"Response: {response.json()}")
            except json.JSONDecodeError:
                print("Response is not in JSON format")
                print(f"Response text: {response.text}")
            return True
        elif response.status_code == 464:
            print(f"POST request failed with status 464: {response.text}")
            return False
        else:
            print(f"POST request failed: {response.status_code}")
            print(f"Response: {response.text}")
            return False
