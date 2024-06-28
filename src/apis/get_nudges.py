import os

import requests

from utils.helpers import Helpers


class Get_nudges:
    def __init__(self, get_nudge_url, token, output_dir):
        self.get_nudge_url = get_nudge_url
        self.token = token
        self.output_dir = output_dir

    def get_nudges(self):
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        print(f"Fetching data from {self.get_nudge_url} with token: {self.token}")
        response = requests.get(self.get_nudge_url, headers=headers)
        if response.status_code == 200:
            print("Data fetched successfully")
            return response.json()
        else:
            print(f"Failed to fetch data: {response.status_code}")
            print(f"Response: {response.text}")
            return None

    def fetch_and_store_get_nudge_data(self):
        # print("Fetching and storing get all nudge data")
        data = self.get_nudges()
        if data:
            json_filename = os.path.join(self.output_dir, 'getNudgeData.json')
            csv_filename = os.path.join(self.output_dir, 'getNudgeData.csv')
            Helpers.store_data_as_json(data, json_filename)
            #Helpers.store_data_as_csv(data["data"], csv_filename)  # Store only the 'data' part
            # print("Get all nudge data stored")

            # # Extract and print top 3 action codes and titles
            # print("\nTop 3 Nudges:")
            # top_nudge_codes = data["data"][:3]
            # for item in top_nudge_codes:
            #     action_code = item.get('action_code')
            #     title = item.get('title')
            #     description = item.get('description')
            #     print(f"Action Code: {action_code}, Title: {title}")
            #     # print(f"Action Code: {action_code}, Title: {title}, description: {description}")
