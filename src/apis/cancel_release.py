import requests


class Cancel_release:

    def __init__(self, cancel_release_url, token):
        self.cancel_release_url = cancel_release_url
        self.token = token

    def cancel_release_imei(self):
        headers = {
            'content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}'
        }

        payload = {
            'imei': '352918103315714'
        }

        response = requests.post(self.cancel_release_url, json=payload, headers=headers)
        print(f"sending request to {self.cancel_release_url} with {payload}")
        if response.status_code == 200:
            print("cancel release request")
            return response.json()
        elif response.status_code == 400:
            print(f"request cancel for the cancel release{response.text}")
            return response.json()
        else:
            print(f"Failed to fetch data: {response.status_code}")
            print(f"Response: {response.text}")
