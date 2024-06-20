import requests


def create_nudges_from_api(create_url, token, notification_type):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    payload = {}

    if notification_type == 'Loan_Wallpaper_Block':
        payload = {
            'title': 'Test LWB Nudge 6',
            'description': 'Test LWB Nudge 6',
            'type': 'nudge',
            'perform_activity': {
                'action': 'LW',
                'type': 'nudge',
                'url': 'https://www.datacultr.com/'
            },
            'language': 'en'
        }
    elif notification_type == 'Application_Block':
        payload = {
            'title': 'Test AB 6',
            'description': 'Test AB 6',
            'type': 'nudge',
            'perform_activity': {
                'action': 'AB',
                'type': 'nudge',
                'pkg': [
                    'youtube.apk',
                    'chrome.apk'
                ]
            },
            'language': 'en'
        }
    elif notification_type == 'Call_Barring':
        payload = {
            'title': 'Test CB 6',
            'description': 'Test CB 6',
            'type': 'nudge',
            'perform_activity': {
                'action': 'OC',
                'type': 'nudge'
            },
            'language': 'en'
        }
    else:
        print("No payload is present to execute for this nudges type.")
        return None, None

    response = requests.post(create_url, json=payload, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        tag = response_data.get('tag')
        print(f"Notification created successfully for {notification_type}, tag: {tag}")
        return tag, response_data
    else:
        print(f"Failed to create notification: {response.status_code}")
        print(f"Response: {response.text}")
        return None, None
