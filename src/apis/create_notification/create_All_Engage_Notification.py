import json
import pandas as pd
import requests
import os
from utils.token import generate_token
from utils.helpers import ensure_output_directory


def create_engage_notification_from_api(create_url, token, notification_type):
    headers = {
        'content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    payload = {}

    if notification_type == 'Alert':
        payload = {
            'title': 'Test_Alert_Message2',
            'description': 'Test_Alert_Message_Description2',
            'action_btn': 'Okay',
            'category': 'Engage',
            'version': '6.1'
        }
    elif notification_type == 'Banner':
        payload = {
            'title': 'Test_Banner_Message2',
            'description': 'Test_Banner_Message_Description2',
            'banner': 'https://marketplace.whmcs.com/product/2130/images/icon200-b5bf3a12359d3083970d9d241c1ee4e5.png',
            'url': 'https://www.datacultr.com/',
            'category': 'Engage',
            'version': '6.1'
        }
    elif notification_type == 'plain_With_Action':
        payload = {
            'title': 'Test_Plain_With_Action2',
            'description': 'Test_Plain_With_Action_Description2',
            'action_btn': 'Pay Now',
            'url': 'https://www.datacultr.com/',
            'expiry_date': '2024-12-01T05:28:47.083Z',
            'category': 'Engage',
            'version': '6.1'
        }
    elif notification_type == 'plain':
        payload = {
            'title': 'Test_Plain2',
            'description': 'Test_Plain_Description2',
            'url': 'https://www.datacultr.com/',
            'expiry_date': '2024-12-01T05:28:47.083Z',
            'category': 'Engage',
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
    data = create_engage_notification_from_api(api_create_url, token, notification_type)
    if data:
        json_filename = os.path.join(output_dir, f'{notification_type}NotificationData.json')
        csv_filename = os.path.join(output_dir, f'{notification_type}NotificationData.csv')
        store_data_as_json(data, json_filename)
        store_data_as_csv(data, csv_filename)


def main():
    # Configuration variables
    token_url = 'https://betaapi.1984.rocks/api/token/'
    api_create_urls = {
        'Alert': 'https://stagefirebase.1984.rocks/notification/alert',
        'Banner': 'https://stagefirebase.1984.rocks/notification/banner',
        'plain_With_Action': 'https://stagefirebase.1984.rocks/notification/plain_with_action',
        'plain': 'https://stagefirebase.1984.rocks/notification/plain'
    }
    username = 'DATACULTR'
    password = 'DC#DATA%@CULTR$&'
    notification_types = ['Alert', 'Banner', 'plain_With_Action', 'plain']
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
