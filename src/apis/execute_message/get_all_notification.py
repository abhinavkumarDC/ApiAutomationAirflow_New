import requests
import os
import json
import random
import uuid
from utils.helpers import store_data_as_json, store_data_as_csv


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


def fetch_and_store_get_notification_data(url, token, output_dir):
    data = fetch_data_from_api(url, token)
    if data:
        json_filename = os.path.join(output_dir, 'getNotificationData.json')
        csv_filename = os.path.join(output_dir, 'getNotificationData.csv')
        store_data_as_json(data, json_filename)
        store_data_as_csv(data, csv_filename)
        return data
    return None


def get_random_code_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        if "results" in data:
            codes = [result["code"] for result in data["results"]]
            return random.choice(codes)
        else:
            print("No results found in JSON file")
            return None


def post_notification_with_code(url, token, code, csv_file_path):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    files = {
        'file': ('Notification_File_with_sample_data.csv', open(csv_file_path, 'rb'), 'text/csv'),
        'notification_code': (None, code),
        'transactionId': (None, str(uuid.uuid4())),
        'reason': (None, 'Payment Reminder')
    }

    # Log the request details
    print(f"Posting notification with code {code} to {url}")
    print(f"Headers: {headers}")
    print(f"Files: {files}")

    response = requests.post(url, headers=headers, files=files)

    # Log the response details
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

    if response.status_code == 200:
        print("POST request successful")
        return response.json()
    else:
        print(f"Failed to send POST request: {response.status_code}")
        print(f"Response: {response.text}")
        return None
