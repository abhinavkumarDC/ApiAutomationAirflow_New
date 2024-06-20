import requests


class TokenManager:
    @staticmethod
    def generate_token(token_url, username, password):
        print("Generating token inside TokenManager")
        payload = {
            'username': username,
            'password': password
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(token_url, json=payload, headers=headers)

        if response.status_code == 200:
            token_data = response.json()
            print("Token generated successfully inside TokenManager.")
            return token_data['access']
        else:
            print(f"Failed to fetch token: {response.status_code}")
            print(f"Response: {response.text}")
            return None
