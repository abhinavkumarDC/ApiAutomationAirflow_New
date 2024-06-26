import json


class Config:
    def __init__(self, config_file):
        print(f"Loading configuration from {config_file}")
        with open(config_file, 'r') as file:
            config_data = json.load(file)

        self.token_url = config_data['token_url']
        self.username = config_data['username']
        self.password = config_data['password']
        self.api_create_urls = config_data['api_create_urls']
        self.api_get_all_notification_url = config_data['api_get_all_notification_url']
        self.api_get_notification_url = config_data['api_get_notification_url']
        self.api_applyNotificationBulk_url = config_data['api_applyNotificationBulk_url']
        self.api_push_bulk_csv_url = config_data['api_push_bulk_csv_url']
        self.api_bulk_custom_notification_v4_url = config_data['api_bulk_custom_notification_v4_url']
        self.input_dir = config_data['input_dir']
        self.output_dir = config_data['output_dir']
        # print("Configuration loaded successfully")
