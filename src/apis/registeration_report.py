import requests


class Registration_report:
    def __init__(self, registration_report_url):
        print(f"--\nInitializing Registration_report api with endpoint: {registration_report_url}")
        self.registration_report_url = registration_report_url

    def registration_report_imei(self):
        headers = {
            'content-Type': 'application/json',
            'apikey': 'HELLOWORLD'
        }
        payload = {
            "imei1": "864412063794319"
        }

        response = requests.post(self.registration_report_url, json=payload, headers=headers)
        print(f"Sending post request to {self.registration_report_url} with the payload of IMEI{payload}")
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
        elif response.status_code == 500:
            print(f"post request failed with status code 500 {response.text}")
            return response.json()
        else:
            print(f"Failed to fetch data: {response.status_code}")
            print(f"Response: {response.text}")
