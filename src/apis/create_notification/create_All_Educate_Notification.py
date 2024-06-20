import json
import pandas as pd
import requests
import os
from utils.token import generate_token
from utils.helpers import ensure_output_directory


def create_educate_notification_from_api(create_url, token, notification_type):
    headers = {
        'content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    payload = {}

    if notification_type == 'Carousel':
        payload = {
            'screen1_title': 'Test Carousel1',
            'screen1_description': 'Test Carousel1',
            'screen1_img': 'https://upload.wikimedia.org/wikipedia/commons/9/9a/Gull_portrait_ca_usa.jpg',
            'screen2_title': 'https://upload.wikimedia.org/wikipedia/commons/9/9a/Gull_portrait_ca_usa.jpg',
            'screen2_description': 'Test',
            'screen2_img': 'https://upload.wikimedia.org/wikipedia/commons/9/9a/Gull_portrait_ca_usa.jpg',
            'screen3_title': 'https://upload.wikimedia.org/wikipedia/commons/9/9a/Gull_portrait_ca_usa.jpg',
            'screen3_description': 'Test',
            'screen3_img': 'https://upload.wikimedia.org/wikipedia/commons/9/9a/Gull_portrait_ca_usa.jpg',
            'screen4_title': 'Test',
            'screen4_description': 'Test',
            'screen4_img': 'https://upload.wikimedia.org/wikipedia/commons/9/9a/Gull_portrait_ca_usa.jpg',
            'skip_btn_name': 'Skip',
            'next_btn_name': 'Next',
            'action_btn_name': 'Pay Now',
            'hold_for': 5,
            'show_cancel': True,
            'category': 'Educate',
            'version': '6.1'
        }
    elif notification_type == 'Poll_MP3':
        payload = {
            'question': 'Have you paid yet 1?',
            'audio_url': 'https://www.datacultr.com/',
            'btn1_text': 'Pay 1',
            'btn1_click_url': 'https://www.datacultr.com/',
            'btn2_text': 'Pay 2',
            'btn2_click_url': 'https://www.datacultr.com/',
            'btn3_text': 'Pay 3',
            'btn3_click_url': 'https://www.datacultr.com/',
            'btn4_text': 'Pay 4',
            'btn4_click_url': 'https://www.datacultr.com/',
            'action_btn': 'Skip',
            'cancel_btn': 'Cancel',
            'hold_for': 5,
            'expiry_date': '2024-06-18T18:30:00.000Z',
            'show_cancel': True,
            'category': 'Educate',
            'version': '6.1'
        }
    elif notification_type == 'Poll_video':
        payload = {
            'question': 'Have you paid yet 1?',
            'video_url': 'https://www.datacultr.com/',
            'btn1_text': 'Pay 1',
            'btn1_click_url': 'https://www.datacultr.com/',
            'btn2_text': 'Pay 2',
            'btn2_click_url': 'https://www.datacultr.com/',
            'btn3_text': 'Pay 3',
            'btn3_click_url': 'https://www.datacultr.com/',
            'btn4_text': 'Pay 4',
            'btn4_click_url': 'https://www.datacultr.com/',
            'action_btn': 'Pay Now',
            'cancel_btn': 'Cancel',
            'hold_for': 5,
            'expiry_date': '2024-06-19T18:30:00.000Z',
            'show_cancel': True,
            'category': 'Educate',
            'version': '6.1'
        }
    elif notification_type == 'Poll_Image':
        payload = {
            'question': 'Have you paid yet 1 ?',
            'image_url': 'https://www.datacultr.com/',
            'btn1_text': 'Pay 1',
            'btn1_click_url': 'https://www.datacultr.com/',
            'btn2_text': 'Pay 2',
            'btn2_click_url': 'https://www.datacultr.com/',
            'btn3_text': 'Pay 3',
            'btn3_click_url': 'https://www.datacultr.com/',
            'btn4_text': 'Pay 4',
            'btn4_click_url': 'https://www.datacultr.com/',
            'action_btn': 'Pay Now',
            'cancel_btn': 'Cancel',
            'hold_for': 5,
            'expiry_date': '2024-06-12T18:30:00.000Z',
            'show_cancel': True,
            'category': 'Educate',
            'version': '6.1'
        }

    elif notification_type == 'Simulated_Call':
        payload = {
            'title': 'Test Simulated Call 2',
            'description': 'Test Simulated call description 2',
            'ringtime': 2,
            'callduration': 10,
            'voiceaudio': 'https://www.datacultr.com/',
            'disconnectbtn': True,
            'category': 'Educate',
            'version': '6.1'
        }

    elif notification_type == 'Video':
        payload = {
            'title': 'Test Video Call 2',
            'description': 'Test Video Call 2',
            'video': 'https://www.datacultr.com/',
            'image': 'https://upload.wikimedia.org/wikipedia/commons/9/9a/Gull_portrait_ca_usa.jpg',
            'category': 'Educate',
            'version': '6.1'
        }
    else:
        print("No payload is present to execute for this create_notification type.")
        return None

    response = requests.post(create_url, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to create create_notification: {response.status_code}")
        print(f"Response: {response.text}")
        return None


def store_data_as_json(data, filename):
    print(f"Storing data as JSON in {filename}")
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def store_data_as_csv(data, filename):
    print(f"Storing data as CSV in {filename}")
    df = pd.DataFrame([data])
    df.to_csv(filename, index=False)


def fetch_and_store_created_notification_data(api_create_url, token, notification_type, output_dir):
    data = create_educate_notification_from_api(api_create_url, token, notification_type)
    if data:
        json_filename = os.path.join(output_dir, f'{notification_type}NotificationData.json')
        csv_filename = os.path.join(output_dir, f'{notification_type}NotificationData.csv')
        store_data_as_json(data, json_filename)
        store_data_as_csv(data, csv_filename)


def main():
    # Configuration variables
    token_url = 'https://betaapi.1984.rocks/api/token/'
    api_create_urls = {
        'Carousel': 'https://stagefirebase.1984.rocks/notification/carousal',
        'Poll_MP3': 'https://stagefirebase.1984.rocks/notification/poll_mp3',
        'Poll_video': 'https://stagefirebase.1984.rocks/notification/poll_video',
        'Poll_Image': 'https://stagefirebase.1984.rocks/notification/poll_image',
        'Simulated_Call': 'https://stagefirebase.1984.rocks/notification/reminder',
        'Video': 'https://stagefirebase.1984.rocks/notification/video'
    }
    username = 'DATACULTR'
    password = 'DC#DATA%@CULTR$&'
    notification_types = ['Carousel', 'Poll_MP3', 'Poll_video', 'Poll_Image', 'Simulated_Call', 'Video']
    output_dir = '/Output'

    # Generate token
    token = generate_token(token_url, username, password)
    if token is None:
        print("Failed to obtain token. Exiting.")
        return

    # Ensure output directory exists
    ensure_output_directory(output_dir)

    # Create and store data for each create_notification type
    for notification_type in notification_types:
        api_create_url = api_create_urls.get(notification_type)
        if api_create_url:
            fetch_and_store_created_notification_data(api_create_url, token, notification_type, output_dir)
        else:
            print(f"No API URL found for create_notification type: {notification_type}")


if __name__ == '__main__':
    main()
