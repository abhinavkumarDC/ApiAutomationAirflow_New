import requests


class Device_logs:
    def __init__(self, device_logs_url):
        self.device_logs_url = device_logs_url

    def device_log_history(self):
        headers = {
            'content-Type': 'application/json',
            'apikey': 'HELLOWORLD'
        }
        payload = {
            "report": "devicehistory",
            "actor": "DATACULTR",
            "imei": "654543456000000"
        }

        response = requests.post(self.device_logs_url, json=payload, headers=headers)
        print(f"Sending post request to {self.device_logs_url} with the payload of IMEI{payload}")
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
        elif response.status_code == 460:
            print(f"post request failed with status code 460 {response.text}")
            return response.json()
        else:
            print(f"Failed to fetch data: {response.status_code}")
            print(f"Response: {response.text}")


