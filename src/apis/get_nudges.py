import pandas as pd
import requests
import json
import os


class Get_nudges:
    def __init__(self, get_nudge_url, token):
        self.get_nudge_url = get_nudge_url
        self.token = token

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

    def main():
        # Configuration variables
        token_url = 'https://betaapi.1984.rocks/api/token/'
        api_url = 'https://betaapi.1984.rocks/api/v2/lifecycle/dem_DATACULTR/get_nudges/'
        username = 'DATACULTR'
        password = 'DC#DATA%@CULTR$&'
        output_dir = '/home/abhinavkumar/Documents/Automation/Automation_Project/' \
                     'Latest_Copy/Pycharm Proects/New2/ApiAutomationAirflow/Output/Nudges/get_Nudges'

        # Generate token

        # Generate token
        print("Generating token...")
        token = generate_token(token_url, username, password)
        if token is None:
            print("Failed to obtain token. Exiting.")
            return
        print(f"Token generated: {token}")

        # Ensure output directory exists
        print(f"Ensuring output directory exists at {output_dir}...")
        ensure_output_directory(output_dir)

        # Fetch and store data
        print("Fetching and storing notification data...")
        fetch_and_store_get_notification_data(api_url, token, output_dir)

        print("Process completed.")

    if __name__ == '__main__':
        main()
