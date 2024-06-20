import json
import pandas as pd
import requests
import os
from utils.token import generate_token
from utils.helpers import ensure_output_directory


def create_sell_notification_from_api(create_url, token, notification_type):
    headers = {
        'content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    payload = {}

    if notification_type == 'Banner_With_Action':
        payload = {
            'title': 'Test Banner With Actions Sell1',
            'description': 'Test Banner With Actions Sell1',
            'banner': 'https://upload.wikimedia.org/wikipedia/commons/9/9a/Gull_portrait_ca_usa.jpg',
            'action_btn': 'Pay Now',
            'url': 'https://www.datacultr.com/',
            'expiry_date': '2024-06-18T18:30:00.000Z',
            'category': 'Sell',
            'version': '6.1'
        }
    elif notification_type == 'in_app_image':
        payload = {
            'image': 'https://upload.wikimedia.org/wikipedia/commons/9/9a/Gull_portrait_ca_usa.jpg',
            'title': 'Test in-app Image Sell1',
            'description': 'Test in-app Image Sell1',
            'btn2_name': 'Pay Now',
            'url': 'https://www.datacultr.com/',
            'show_cancel': True,
            'btn1_name': 'Cancel',
            'hold_for': 5,
            'category': 'Sell',
            'version': '6.1'
        }
    elif notification_type == 'in_app_Transparent_With_Action':
        payload = {
            'title': 'Test In-app transparent with action Sell1',
            'description': 'Test In-app transparent with action Sell1',
            'btn1_txt': 'Pay Now',
            'btn1_action': 'https://www.datacultr.com/',
            'btn3_txt': 'Cancel',
            'url': 'https://www.datacultr.com/',
            'hold_for': 5,
            'show_cancel': True,
            'category': 'Sell',
            'version': '6.1'
        }
    elif notification_type == 'video':
        payload = {
            'title': 'Title Sell Video1',
            'description': 'Title Sell Video1',
            'video': 'https://www.datacultr.com/',
            'image': 'https://upload.wikimedia.org/wikipedia/commons/9/9a/Gull_portrait_ca_usa.jpg',
            'category': 'Sell',
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
    data = create_sell_notification_from_api(api_create_url, token, notification_type)
    if data:
        json_filename = os.path.join(output_dir, f'{notification_type}NotificationData.json')
        csv_filename = os.path.join(output_dir, f'{notification_type}NotificationData.csv')
        store_data_as_json(data, json_filename)
        store_data_as_csv(data, csv_filename)


def main():
    # Configuration variables
    token_url = 'https://betaapi.1984.rocks/api/token/'
    api_create_urls = {
        'Banner_With_Action': 'https://stagefirebase.1984.rocks/notification/banner_with_actions',
        'in_app_image': 'https://stagefirebase.1984.rocks/notification/in_app_image',
        'in_app_Transparent_With_Action': 'https://stagefirebase.1984.rocks/notification/in_app_transparent_with_action',
        'video': 'https://stagefirebase.1984.rocks/notification/video'
    }
    username = 'DATACULTR'
    password = 'DC#DATA%@CULTR$&'
    notification_types = ['Banner_With_Action', 'in_app_image', 'in_app_Transparent_With_Action', 'video']
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
