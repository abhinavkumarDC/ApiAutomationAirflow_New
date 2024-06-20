import os
from utils.token import TokenManager
from utils.helpers import Helpers
from apis.get_All_NotificationNew import GetAllNotification
from apis.get_Notification import GetNotification
from apis.create_Notification import CreateNotification
from config import Config


class NotificationManager:
    def __init__(self, config):
        print("Initializing NotificationManager")
        self.token_url = config.token_url
        self.api_create_urls = config.api_create_urls
        self.api_get_all_notification_url = config.api_get_all_notification_url
        self.api_get_notification_url = config.api_get_notification_url
        self.username = config.username
        self.password = config.password
        self.output_dir = config.output_dir
        self.token = None
        print("NotificationManager initialized")

    def generate_token(self):
        if self.token is None:
            print("Generating token")
            self.token = TokenManager.generate_token(self.token_url, self.username, self.password)
            if self.token is None:
                print("Failed to obtain token. Exiting.")
                return False
            print("Token generated successfully")
        return True

    def run_get_all_notification(self):
        print("Running get all notification")
        get_all_notification = GetAllNotification(self.api_get_all_notification_url, self.token, self.output_dir)
        get_all_notification.fetch_and_store_get_all_notification_data()
        print("Get all notification completed")

    def run_get_notification(self):
        print("Running get notification")
        get_notification = GetNotification(self.api_get_notification_url, self.token, self.output_dir)
        get_notification.fetch_and_store_get_notification_data()
        print("Get notification completed")

    def run_create_notification(self):
        print("Running create notification")
        for notification_type, api_create_url in self.api_create_urls.items():
            print(f"Creating notification for type: {notification_type}")
            create_notification = CreateNotification(api_create_url, self.token, notification_type, self.output_dir)
            create_notification.fetch_and_store_created_notification_data()
            print(f"Notification created for type: {notification_type}")

    def ensure_output_directory(self):
        print("Ensuring output directory")
        Helpers.ensure_output_directory(self.output_dir)
        print("Output directory ensured")


def main():
    print("Starting main function")
    # Load configuration
    config = Config('config/config.json')

    manager = NotificationManager(config)

    if not manager.generate_token():
        return

    manager.ensure_output_directory()

    # Run desired operations
    manager.run_get_notification()
    manager.run_get_all_notification()
    manager.run_create_notification()
    print("All operations completed")


if __name__ == '__main__':
    main()
