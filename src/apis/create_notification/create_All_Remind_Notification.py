import json
import pandas as pd
import requests
import os
from utils.token import generate_token
from utils.helpers import ensure_output_directory


def create_remind_notification_from_api(create_url, token, notification_type):
    headers = {
        'content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    payload = {}

    if notification_type == 'eNach':
        payload = {
            'image': 'https://upload.wikimedia.org/wikipedia/commons/9/9a/Gull_portrait_ca_usa.jpg',
            'title': 'Test eNACH2',
            'description': 'Test eNACH Description2',
            'btn1_name': 'OKAY',
            'category': 'Remind',
            'version': '6.1'
        }
    elif notification_type == 'in_App':
        payload = {
            'title': 'Test in-app1',
            'description': 'Test in-app Description1',
            'url': 'https://www.datacultr.com/',
            'btn1_name': 'Cancel',
            'btn2_name': 'Pay',
            'hold_for': 5,
            'show_cancel': True,
            'category': 'Remind',
            'version': '6.1'
        }
    elif notification_type == 'in_App_Image':
        payload = {
            'image': 'https://www.datacultr.com/',
            'title': 'Test in-app Image1',
            'description': 'Test in-app Image Description1',
            'btn2_name': 'Pay Now',
            'url': 'https://www.datacultr.com/',
            'show_cancel': True,
            'btn1_name': 'Cancel',
            'hold_for': 5,
            'category': 'Remind',
            'version': '6.1'
        }
    elif notification_type == 'alert_With_Action':
        payload = {
            'title': 'Test Alert With Action1',
            'description': 'Test Alert With Action1',
            'action_btn': 'Pay Now',
            'url': 'https://www.datacultr.com/',
            'action_btn2': 'Cancel',
            'hold_for': 5,
            'show_cancel': True,
            'category': 'Remind',
            'version': '6.1'
        }
    elif notification_type == 'banner_With_Action':
        payload = {
            'title': 'Test Banner With Action1',
            'description': 'Test Banner With Action Description1',
            'banner': 'https://upload.wikimedia.org/wikipedia/commons/9/9a/Gull_portrait_ca_usa.jpg',
            'action_btn': 'Pay Now',
            'url': 'https://www.datacultr.com/',
            'expiry_date': '2024-06-18T18:30:00.000Z',
            'category': 'Remind',
            'version': '6.1'
        }
    elif notification_type == 'in_App_Full_Action':
        payload = {
            'title': 'Test In-App full screen1',
            'description': 'Test In-App full screen description1',
            'btn2_name': 'Pay Now',
            'btn1_name': 'Cancel',
            'url': 'https://www.datacultr.com/',
            'image': 'https://upload.wikimedia.org/wikipedia/commons/9/9a/Gull_portrait_ca_usa.jpg',
            'hold_for': 5,
            'show_cancel': True,
            'category': 'Remind',
            'version': '6.1'
        }
    elif notification_type == 'In_App_Transparent_With_Action':
        payload = {
            'title': 'Test In-app transparent with action1',
            'description': 'Test In-app transparent with action Description1',
            'btn1_txt': 'Pay Now',
            'btn1_action': 'https://www.datacultr.com/',
            'btn3_txt': 'Cancel',
            'url': 'https://www.datacultr.com/',
            'hold_for': 5,
            'show_cancel': True,
            'category': 'Remind',
            'version': '6.1'
        }
    elif notification_type == 'pay_Now':
        payload = {
            'title': 'Test Pay Now1',
            'description': 'Test Pay Now1',
            'url': 'https://www.datacultr.com/',
            'category': 'Remind',
            'version': '6.1'
        }
    elif notification_type == 'in_App_Transparent':
        payload = {
            'title': 'Test in-app transparent1',
            'description': 'Test in-app transparent Description1',
            'txt': 'Pay Now',
            'category': 'Remind',
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
    data = create_remind_notification_from_api(api_create_url, token, notification_type)
    if data:
        json_filename = os.path.join(output_dir, f'{notification_type}NotificationData.json')
        csv_filename = os.path.join(output_dir, f'{notification_type}NotificationData.csv')
        store_data_as_json(data, json_filename)
        store_data_as_csv(data, csv_filename)


def main():
    # Configuration variables
    token_url = 'https://betaapi.1984.rocks/api/token/'
    api_create_urls = {
        'eNach': 'https://stagefirebase.1984.rocks/notification/enach',
        'in_App': 'https://stagefirebase.1984.rocks/notification/in_app',
        'in_App_Image': 'https://stagefirebase.1984.rocks/notification/in_app_image',
        'alert_With_Action': 'https://stagefirebase.1984.rocks/notification/alert_with_actions',
        'banner_With_Action': 'https://stagefirebase.1984.rocks/notification/banner_with_actions',
        'in_App_Full_Action': 'https://stagefirebase.1984.rocks/notification/in_app_fullscreen',
        'In_App_Transparent_With_Action': 'https://stagefirebase.1984.rocks/notification/in_app_transparent_with_action',
        'pay_Now': 'https://stagefirebase.1984.rocks/notification/pay_now',
        'in_App_Transparent': 'https://stagefirebase.1984.rocks/notification/in_app_transparent'
    }
    username = 'DATACULTR'
    password = 'DC#DATA%@CULTR$&'
    notification_types = ['eNach', 'in_App', 'in_App_Image', 'alert_With_Action', 'banner_With_Action',
                          'in_App_Full_Action', 'In_App_Transparent_With_Action', 'pay_Now', 'in_App_Transparent']
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
