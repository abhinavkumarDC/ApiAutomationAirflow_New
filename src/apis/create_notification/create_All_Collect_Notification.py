import json
import pandas as pd
import requests
import os
from utils.token import generate_token
from utils.helpers import ensure_output_directory


def create_educate_notification_from_api(create_url, token, notification_type):
    headers = {
        'content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    payload = {}

    if notification_type == 'full_Screen_Image':
        payload = {
            'image': 'https://upload.wikimedia.org/wikipedia/commons/9/9a/Gull_portrait_ca_usa.jpg',
            'url': 'https://www.datacultr.com/',
            'hold_for': 5,
            'show_cancel': True,
            'category': 'Collect',
            'version': '6.1'
        }
    elif notification_type == 'simulated_Call':
        payload = {
            'title': 'Test Simulated call 1',
            'description': 'Test Simulated call 1',
            'ringtime': 5,
            'callduration': 10,
            'voiceaudio': 'https://www.datacultr.com/',
            'disconnectbtn': True,
            'category': 'Collect',
            'version': '6.1'
        }

    else:
        print("No payload is present to execute for this create_notification type.")
        return None

    response = requests.post(create_url, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to create create_notification: {response.status_code}")
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


def fetch_and_store_created_notification_data(api_create_url, token, notification_type, output_dir):
    data = create_educate_notification_from_api(api_create_url, token, notification_type)
    if data:
        json_filename = os.path.join(output_dir, f'{notification_type}NotificationData.json')
        csv_filename = os.path.join(output_dir, f'{notification_type}NotificationData.csv')
        store_data_as_json(data, json_filename)
        store_data_as_csv(data, csv_filename)


def main():
    # Configuration variables
    token_url = 'https://betaapi.1984.rocks/api/token/'
    api_create_urls = {
        'full_Screen_Image': 'https://stagefirebase.1984.rocks/notification/flasher_image',
        'simulated_Call': 'https://stagefirebase.1984.rocks/notification/vcn',

    }
    username = 'DATACULTR'
    password = 'DC#DATA%@CULTR$&'
    notification_types = ['full_Screen_Image', 'simulated_Call']
    output_dir = '/Output'

    # Generate token
    token = generate_token(token_url, username, password)
    if token is None:
        print("Failed to obtain token. Exiting.")
        return

    # Ensure output directory exists
    ensure_output_directory(output_dir)

    # Create and store data for each create_notification type
    for notification_type in notification_types:
        api_create_url = api_create_urls.get(notification_type)
        if api_create_url:
            fetch_and_store_created_notification_data(api_create_url, token, notification_type, output_dir)
        else:
            print(f"No API URL found for create_notification type: {notification_type}")


if __name__ == '__main__':
    main()
