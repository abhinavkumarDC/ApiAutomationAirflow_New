import pandas as pd
import requests
import json
import os
from utils.token import generate_token
from utils.helpers import ensure_output_directory


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


def store_data_as_json(data, filename):
    print(f"Storing data as JSON in {filename}")
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def store_data_as_csv(data, filename):
    print(f"Storing data as CSV in {filename}")
    df = pd.DataFrame([data])
    df.to_csv(filename, index=False)


def fetch_and_store_get_notification_data(url, token, output_dir):
    data = fetch_data_from_api(url, token)
    if data:
        json_filename = os.path.join(output_dir, 'getNotificationData.json')
        csv_filename = os.path.join(output_dir, 'getNotificationData.csv')
        store_data_as_json(data, json_filename)
        store_data_as_csv(data, csv_filename)


def main():
    # Configuration variables
    token_url = 'https://betaapi.1984.rocks/api/token/'
    api_url = 'https://betaapi.1984.rocks/api/v3/lifecycle/dem_DATACULTR/get_all_nudges/'
    username = 'DATACULTR'
    password = 'DC#DATA%@CULTR$&'
    output_dir = '/Output/Nudges'

    # Generate token
    token = generate_token(token_url, username, password)
    if token is None:
        print("Failed to obtain token. Exiting.")
        return

    # Ensure output directory exists
    ensure_output_directory(output_dir)

    # Fetch and store data
    fetch_and_store_get_notification_data(api_url, token, output_dir)


if __name__ == '__main__':
    main()
