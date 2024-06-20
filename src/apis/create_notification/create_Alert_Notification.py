import json
import pandas as pd
import requests
import os
from utils.token import generate_token
from utils.helpers import ensure_output_directory


def create_alert_notification_from_api(create_url, token):
    payload = {
        'title': 'Test9999',
        'description': 'Test9999',
        'action_btn': 'Okay',
        'category': 'Engage',
        'version': '6.1'
    }
    headers = {
        'content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    resposne = requests.post(create_url, json=payload, headers=headers)

    if resposne.status_code == 200:
        return resposne.json()
    else:
        print(f"Failed to fetch data: {resposne.status_code}")
        print(f"Response: {resposne.text}")


def store_data_as_json(data, filename):
    print(f"Storing data ss JSON in{filename}")
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def store_data_as_csv(data, filename):
    print(f"Storing data as CSV in {filename}")
    df = pd.DataFrame([data])
    df.to_csv(filename, index=False)


def fetch_and_store_created_notification_data(api_create_url, token, output_dir):
    data = create_alert_notification_from_api(api_create_url, token)
    if data:
        json_filename = os.path.join(output_dir, 'createdNotificationData.json')
        csv_filename = os.path.join(output_dir, 'createdNotificationData.csv')
        store_data_as_json(data, json_filename)
        store_data_as_csv(data, csv_filename)


def main():
    # Configurataion variables
    token_url = 'https://betaapi.1984.rocks/api/token/'
    api_create_url = 'https://stagefirebase.1984.rocks/notification/alert'
    username = 'DATACULTR'
    password = 'DC#DATA%@CULTR$&'
    output_dir = '/Output'

    # Generate token
    token = generate_token(token_url, username, password)
    if token is None:
        print("Failed to obtain token. Exiting.")
        return

    # Ensure output directory exists
    ensure_output_directory(output_dir)

    # Create and store data
    fetch_and_store_created_notification_data(api_create_url, token, output_dir)


if __name__ == '__main__':
    main()
