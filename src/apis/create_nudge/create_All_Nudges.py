import os
import random
import requests
from utils.helpers import Helpers


class Create_nudges:
    def __init__(self, create_nudge_url, token, nudge_type, output_dir):
        print(f"--\nInitializing create all nudge API for message type: {nudge_type}")
        self.create_nudge_url = create_nudge_url
        self.token = token
        self.nudge_type = nudge_type
        self.output_dir = output_dir
        self.helpers = Helpers()

    def create_nudges_from_api(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}'
        }

        payload = self.get_payload()
        if not payload:
            print("No payload found for this nudge type.")
            return None

        response = requests.post(self.create_nudge_url, json=payload, headers=headers)
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
            'Loan_Wallpaper_Block': {
                'title': f'Test LWB Nudge {random_number}',
                'description': 'Test LWB Nudge 2',
                'type': 'nudge',
                'perform_activity': {
                    'action': 'LW',
                    'type': 'nudge',
                    'url': 'https://www.datacultr.com/'
                },
                'language': 'en'
            },
            'Application_Block': {
                'title': f'Test AB {random_number}',
                'description': 'Test AB 2',
                'type': 'nudge',
                'perform_activity': {
                    'action': 'AB',
                    'type': 'nudge',
                    'pkg': [
                        'youtube.apk',
                        'chrome.apk'
                    ]
                },
                'language': 'en'
            },
            'Call_Barring': {
                'title': f'Test CB {random_number}',
                'description': 'Test CB 2',
                'type': 'nudge',
                'perform_activity': {
                    'action': 'OC',
                    'type': 'nudge'
                },
                'language': 'en'
            }
        }
        return payloads.get(self.nudge_type)

    def fetch_and_store_created_allNudges_data(self):
        # print(f"Fetching and storing created notification data for type: {self.notification_type}")
        data = self.create_nudges_from_api()
        if data:
            json_filename = os.path.join(self.output_dir, f'{self.nudge_type}CreateAllNudgeData.json')
            csv_filename = os.path.join(self.output_dir, f'{self.nudge_type}CreateAllNudgeData.csv')
            Helpers.store_data_as_json(data, json_filename)
            Helpers.store_data_as_csv(data, csv_filename)
            print(f"All Nudges created and data stored for type: {self.nudge_type}")
        else:
            print(f"No data fetched for {self.nudge_type}")
