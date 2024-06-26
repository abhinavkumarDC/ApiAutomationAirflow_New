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
        self.get_passcode_url = config_data['get_passcode_url']
        self.get_release_url = config_data['get_release_url']
        self.bulk_release_url = config_data['bulk_release_url']
        self.release_csv_file_path = config_data['release_csv_file_path']
        self.cancel_release_url = config_data['cancel_release_url']
        self.device_status_url = config_data['device_status_url']
        self.registration_report_url = config_data['registration_report_url']
        self.current_status_url = config_data['current_status_url']
        self.device_logs_url = config_data['device_logs_url']
        self.last_online_status_url = config_data['last_online_status_url']
        self.get_all_nudges_url = config_data['get_all_nudges_url']
        self.create_nudge_url = config_data['create_nudge_url']
        self.apply_unlock_url = config_data['apply_unlock_url']
        self.bulk_unlock_url = config_data['bulk_unlock_url']
        self.unlock_csv_file_path = config_data['unlock_csv_file_path']
        self.bulk_lock_url = config_data['bulk_lock_url']
        self.lock_csv_file = config_data['lock_csv_file']
        self.get_nudge_url = config_data['get_nudge_url']
        self.bulk_apply_nudge_url = config_data['bulk_apply_nudge_url']
        self.nudge_csv_file = config_data['nudge_csv_file']
        self.output_dir = config_data['output_dir']
        print("Configuration loaded successfully")
