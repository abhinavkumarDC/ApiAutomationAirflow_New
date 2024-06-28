import random
import requests
from utils.helpers import Helpers
import os


class CreateNotification:
    def __init__(self, create_url, token, notification_type, output_dir):
        print(f"--\nInitializing create notification API for message type: {notification_type}")
        self.create_url = create_url
        self.token = token
        self.notification_type = notification_type
        self.output_dir = output_dir
        self.helpers = Helpers()

    def create_engage_notification_from_api(self):
        # print(f"Creating {self.notification_type} type notification for engage")
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}'
        }

        payload = self.get_payload()
        if not payload:
            print("No payload found for this notification type.")
            return None

        response = requests.post(self.create_url, json=payload, headers=headers)
        if response.status_code == 200:
            # print(f"Notification created successfully for type: {self.notification_type}")
            return response.json()
        else:
            print(f"Failed to create notification: {response.status_code}")
            print(f"Response: {response.text}")
            return None

    def get_payload(self):
        # print(f"Generating payload for type: {self.notification_type}")
        random_number = random.randint(1, 1000)
        payloads = {
            'Alert': {
                'title': f'Test_Alert_Message{random_number}',
                'description': 'Test_Alert_Message_Description2',
                'action_btn': 'Okay',
                'category': 'Engage',
                'version': '6.1'
            },
            'Banner': {
                'title': f'Test_Banner_Message{random_number}',
                'description': 'Test_Banner_Message_Description2',
                'banner': 'https://marketplace.whmcs.com/product/2130/images/icon200-b5bf3a12359d3083970d9d241c1ee4e5'
                          '.png',
                'url': 'https://www.datacultr.com/',
                'category': 'Engage',
                'version': '6.1'
            },
            'plain_With_Action': {
                'title': f'Test_Plain_With_Action{random_number}',
                'description': 'Test_Plain_With_Action_Description2',
                'action_btn': 'Pay Now',
                'url': 'https://www.datacultr.com/',
                'expiry_date': '2024-12-01T05:28:47.083Z',
                'category': 'Engage',
                'version': '6.1'
            },
            'plain': {
                'title': f'Test_Plain{random_number}',
                'description': 'Test_Plain_Description2',
                'url': 'https://www.datacultr.com/',
                'expiry_date': '2024-12-01T05:28:47.083Z',
                'category': 'Engage',
                'version': '6.1'
            }
        }
        return payloads.get(self.notification_type)

    def fetch_and_store_created_notification_data(self):
        # print(f"Fetching and storing created notification data for type: {self.notification_type}")
        data = self.create_engage_notification_from_api()
        if data:
            json_filename = os.path.join(self.output_dir, f'{self.notification_type}CreateNotificationData.json')
            csv_filename = os.path.join(self.output_dir, f'{self.notification_type}CreateNotificationData.csv')
            Helpers.store_data_as_json(data, json_filename)
            Helpers.store_data_as_csv(data, csv_filename)
            print(f"Engage notification created and data stored for type: {self.notification_type}")
        else:
            print(f"No data fetched for {self.notification_type}")