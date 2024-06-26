import requests


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
