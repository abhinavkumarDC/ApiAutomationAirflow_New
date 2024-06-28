import requests


class Last_online_status:
    def __init__(self, last_online_status_url):
        print(f"---\nInitializing Last_online_status api with endpoint: {last_online_status_url}")
        self.last_online_status_url = last_online_status_url

    def get_last_online(self):
        headers = {
            'content-Type': 'application/json',
            'apikey': 'HELLOWORLD'
        }
        payload = {
            "actor": "DATACULTR",
            "seen": "6h"
        }

        response = requests.post(self.last_online_status_url, json=payload, headers=headers)
        print(f"Sending post request to {self.last_online_status_url} with the payload of IMEI{payload}")
        print(f"imei{payload}")
        if response.status_code == 200:
            print("POST request successful")
            print(f"Response: {response.text}")
            return response.json()
        elif response.status_code == 400:
            print(f"Post request failed with status code 400 {response.text}")
            return response.json()
        elif response.status_code == 404:
            print(f"post request failed with status code 404 {response.text}")
            return response.json()
        elif response.status_code == 405:
            print(f"post request failed with status code 405 {response.text}")
            return response.json()
        elif response.status_code == 500:
            print(f"post request failed with status code 500 {response.text}")
            return response.json()
        else:
            print(f"Failed to fetch data: {response.status_code}")
            print(f"Response: {response.text}")
