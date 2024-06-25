import requests
import json


class Get_all_Nudges:
    def __init__(self, get_all_nudges_url, token):
        self.get_all_nudges_url = get_all_nudges_url
        self.token = token
        #self.output_dir = output_dir

    def fetch_data_from_api(self):
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        print(f"Fetching data from {self.get_all_nudges_url} with token: {self.token}")
        response = requests.get(self.get_all_nudges_url, headers=headers)
        if response.status_code == 200:
            print("Data fetched successfully")
            return response.json()
        else:
            print(f"Failed to fetch data: {response.status_code}")
            print(f"Response: {response.text}")
            return None



