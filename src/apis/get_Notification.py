import requests
from utils.helpers import Helpers
import os


class GetNotification:
    def __init__(self, url, token, output_dir):
        print(f"--\nInitializing Get Notification api with endpoint: {url}")
        self.url = url
        self.token = token
        self.output_dir = output_dir

    def fetch_data_from_get_Notification(self):
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        # print(f"Fetching data from {self.url} with token")
        response = requests.get(self.url, headers=headers)
        if response.status_code == 200:
            # print("Data fetched successfully")
            return response.json()
        else:
            print(f"Failed to fetch data: {response.status_code}")
            print(f"Response: {response.text}")
            return None

    def fetch_and_store_get_notification_data(self):
        # print("Fetching and storing get notification data")
        data = self.fetch_data_from_get_Notification()
        if data:
            json_filename = os.path.join(self.output_dir, 'getNotificationData.json')
            csv_filename = os.path.join(self.output_dir, 'getNotificationData.csv')
            Helpers.store_data_as_json(data, json_filename)
            Helpers.store_data_as_csv(data, csv_filename)
            # print("Get notification data stored")
