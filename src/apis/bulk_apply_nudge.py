import random
import string
import uuid
import requests
import json
import os
import time



class Apply_bulk_nudge:
    def __init__(self, get_nudge_url, bulk_apply_nudge_url, policy_code, nudge_csv_file, transaction_id, token):
        self.get_nudge_url = get_nudge_url
        self.bulk_apply_nudge_url = bulk_apply_nudge_url
        self.policy_code = policy_code
        self.nudge_csv_file = nudge_csv_file
        self.transaction_id = transaction_id
        self.token = token

    def fetch_data_from_api(self):
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        print(f"Fetching data from {self.get_nudge_url} with token: {self.token}")
        response = requests.get(self.get_nudge_url, headers=headers)
        if response.status_code == 200:
            print("Data fetched successfully")
            return response.json()
        elif response.status_code == 429:
            retry_after = int(response.headers.get("Retry-After", 5))
            print(f"Rate limited. Retrying after {retry_after} seconds...")
            time.sleep(retry_after)
            return self.fetch_data_from_api()  # Recursive call to retry
        else:
            print(f"Failed to fetch data: {response.status_code}")
            print(f"Response: {response.text}")
            return None

    def get_random_code(self, data):
        if isinstance(self.data, dict) and "nudges" in data:  # Check if data is a dictionary with a "nudges" key
            codes = [item["code"] for item in data["nudges"] if "code" in item]
            if codes:
                code = random.choice(codes)
                print(f"Selected random nudge code: {code}")
                return code
            else:
                print("No nudge codes found in the data")
                return None
        else:
            print("Data is not in the expected format")
            return None

    def send_nudge_with_csv(self):
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        files = {
            'file': open(self.nudge_csv_file, 'rb'),
            'policy_code': self.policy_code,
            'TransactionId': str(uuid.uuid4())
        }
        # data = {
        #
        #     # 'policy_code': 'required_policy_code_here'  # Include the policy_code
        # }
        print(f"Sending PUT request to {self.bulk_apply_nudge_url} with code: {self.policy_code} and TransactionId: {self.transaction_id}")
        response = requests.put(self.bulk_apply_nudge_url, headers=headers, files=files)  # Changed to PUT method
        if response.status_code == 200:
            print("PUT request successful")
            try:
                print(f"Response: {response.json()}")
            except json.JSONDecodeError:
                print("Response is not in JSON format")
                print(f"Response text: {response.text}")
            return True  # Success
        elif response.status_code == 464:
            print(f"PUT request failed with status 464: {response.text}")
            return False  # Specific failure
        else:
            print(f"PUT request failed: {response.status_code}")
            print(f"Response: {response.text}")
            return False  # General failure

    # def fetch_and_store_get_nudge_data(url, token, output_dir):
    #     data = fetch_data_from_api(url, token)
    #     if data:
    #         json_filename = os.path.join(output_dir, 'getNudgesData.json')
    #         csv_filename = os.path.join(output_dir, 'getNudgesData.csv')
    #         store_data_as_json(data, json_filename)
    #         store_data_as_csv(data["nudges"], csv_filename)  # Store only the nudges part as CSV
    #         return get_random_code(data)
    #     return None

    # def main():
    #     # Configuration variables
    #     token_url = 'https://betaapi.1984.rocks/api/token/'
    #     fetch_api_url = 'https://betaapi.1984.rocks/api/v2/lifecycle/dem_DATACULTR/get_nudges/'
    #     post_api_url = 'https://betaapi.1984.rocks/api/v2/lifecycle/dem_DATACULTR/bulkapplynudge/'
    #     username = 'DATACULTR'
    #     password = 'DC#DATA%@CULTR$&'
    #     output_dir = '/home/abhinavkumar/Documents/Automation/Automation_Project/Latest_Copy' \
    #                  '/Pycharm Proects/New2/ApiAutomationAirflow/Output/getNudges_bulkapplynudge_V2/'
    #     csv_file_path = '/home/abhinavkumar/Documents/Automation/Automation_Project/Latest_Copy' \
    #                     '/Pycharm Proects/New2/ApiAutomationAirflow/Input_csv_file/Bulk_Apply_Nudge_V2.csv'
    #
    #     print("Starting the process...")
    #
    #     # Generate token
    #     print("Generating token...")
    #     token = generate_token(token_url, username, password)
    #     if token is None:
    #         print("Failed to obtain token. Exiting.")
    #         return
    #     print(f"Token generated: {token}")
    #
    #     # Ensure output directory exists
    #     print(f"Ensuring output directory exists at {output_dir}...")
    #     ensure_output_directory(output_dir)
    #
    #     tried_nudge_codes = []
    #
    #     for attempt in range(4):
    #         print(f"\nAttempt {attempt + 1}: Fetching and storing code data...")
    #         # Fetch and store data, and get random code
    #         random_code = fetch_and_store_get_nudge_data(fetch_api_url, token, output_dir)
    #         if random_code:
    #             tried_nudge_codes.append(random_code)
    #             print(f"Attempt {attempt + 1}: Random code: {random_code}")
    #
    #             # Generate a new TransactionId
    #             transaction_id = generate_random_transaction_id()
    #
    #             # Send the PUT request with CSV file and nudge_code
    #             print(f"Attempt {attempt + 1}: Sending nudge with the random code...")
    #             success = send_nudge_with_csv(post_api_url, token, random_code, csv_file_path, transaction_id)
    #             if success:
    #                 print("Nudge sent successfully")
    #                 break
    #             else:
    #                 print("Retrying with a new code...")
    #         else:
    #             print("Failed to get a valid code")
    #             break
    #
    #     print("Process completed.")
    #     print("policy_code tried:")
    #     for code in tried_nudge_codes:
    #         print(code)
    #
    # if __name__ == '__main__':
    #     main()
