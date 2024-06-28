import requests


class Release_device:
    def __init__(self, get_release_url, token):
        print(f"--\nInitializing Release_device api with endpoint: {get_release_url}")
        self.get_release_url = get_release_url
        self.token = token

    def release_device(self):
        headers = {
            'content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}'
        }

        payload = {
            'imei1': '124585312457893'
        }

        response = requests.post(self.get_release_url, json=payload, headers=headers)
        print(f"Sending post request to {self.get_release_url} with the payload of passkey{payload}")
        if response.status_code == 200:
            print("put request successful")
            return response.json()
        elif response.status_code == 400:
            print(f"request failed for the release {response.text}")
            return response.json()
        elif response.status_code == 460:
            print(f"request failed for the release {response.text}")
            return response.json()
        elif response.status_code == 401:
            print(f"invalid token {response.text}")
            return response.json()
        elif response.status_code == 404:
            print(f"request failed for the release {response.text}")
            return response.json()
        elif response.status_code == 405:
            print(f"request failed for the release {response.text}")
            return response.json()
        elif response.status_code == 500:
            print(f"request failed for the release {response.text}")
            return response.json()
        else:
            print(f"Failed to fetch data: {response.status_code}")
            print(f"Response: {response.text}")
