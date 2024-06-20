import os
from config import Config
from src.apis.execute_message.get_all_notification import fetch_data_from_api, fetch_and_store_get_notification_data, \
    get_random_code_from_json, post_notification_with_code
from utils.token import generate_token
from utils.helpers import ensure_output_directory, store_data_as_csv, store_data_as_json
from src.apis.create_nudge.create_All_Nudges import create_nudges_from_api


def fetch_and_store_created_notification_data(api_create_function, api_create_url, token, notification_type,
                                              output_dir):
    tag, data = api_create_function(api_create_url, token, notification_type)
    if data:
        json_filename = os.path.join(output_dir, f'{notification_type}_Nudge_Data.json')
        csv_filename = os.path.join(output_dir, f'{notification_type}_Nudge_Data.csv')
        store_data_as_json(data, json_filename)
        store_data_as_csv(data, csv_filename)
        return tag
    return None


def main():
    config = Config('config/config.json')

    # Generate token
    token = generate_token(config.token_url, config.username, config.password)
    if token is None:
        print("Failed to obtain token. Exiting.")
        return

    # Ensure output directory exists
    ensure_output_directory(config.output_dir)

    notification_types_to_functions = {
        'Loan_Wallpaper_Block': create_nudges_from_api,
        'Application_Block': create_nudges_from_api,
        'Call_Barring': create_nudges_from_api,
    }

    # Create and store data for each notification type and collect tags
    tags = []
    for notification_type, api_create_function in notification_types_to_functions.items():
        api_create_url = config.api_create_urls.get(notification_type)
        if api_create_url:
            print(f"Processing {notification_type} with URL {api_create_url}")
            tag = fetch_and_store_created_notification_data(api_create_function, api_create_url, token,
                                                            notification_type, config.output_dir)
            if tag:
                tags.append(tag)
        else:
            print(f"No API URL found for notification type: {notification_type}")

    # Fetch and store data from the get_all_notification API
    get_notification_url = config.api_create_urls.get('get_Notification')
    if get_notification_url:
        print(f"Fetching all notifications from {get_notification_url}")
        notification_data = fetch_and_store_get_notification_data(get_notification_url, token, config.output_dir)
        if notification_data:
            json_file_path = os.path.join(config.output_dir, 'getNotificationData.json')
            random_code = get_random_code_from_json(json_file_path)
            if random_code:
                print(f"Randomly selected code: {random_code}")
                post_url = config.api_create_urls.get('post_notification')
                csv_file_path = '/input_file_csv/Notification_File_with_sample_data.csv'
                if post_url:
                    post_notification_with_code(post_url, token, random_code, csv_file_path)
                else:
                    print("No API URL found for posting notification.")
    else:
        print("No API URL found for getting all notifications.")

    # Print or use the collected tags as needed
    print(f"Collected tags: {tags}")


if __name__ == '__main__':
    main()
