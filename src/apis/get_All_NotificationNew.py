import requests
from utils.helpers import Helpers
import os


class GetAllNotification:
    def __init__(self, url, token, output_dir):
        print(f"---\nInitializing Get AllNotification api with endpoint: {url}")
        self.url = url
        self.token = token
        self.output_dir = output_dir

    def fetch_data_from_api(self):
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

    def fetch_and_store_get_all_notification_data(self):
        # print("Fetching and storing get all notification data")
        data = self.fetch_data_from_api()
        if data:
            json_filename = os.path.join(self.output_dir, 'getAllNotificationData.json')
            csv_filename = os.path.join(self.output_dir, 'getAllNotificationData.csv')
            Helpers.store_data_as_json(data, json_filename)
            Helpers.store_data_as_csv(data, csv_filename)
            # print("Get all notification data stored")
