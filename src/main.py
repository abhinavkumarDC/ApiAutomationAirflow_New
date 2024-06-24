from src.apis.push_bulk_csv import PushBulkCsv
from utils.token import TokenManager
from utils.helpers import Helpers
from apis.get_All_NotificationNew import GetAllNotification
from apis.get_Notification import GetNotification
from apis.create_Engage_Notification import CreateNotification
from apis.applynotificationbulk_v4 import ApplyNotificationBulk
from apis.bulk_custom_notification_v4 import BulkCustomNotification
from config import Config


class NotificationManager:
    def __init__(self, config):
        print("Initializing NotificationManager")
        self.config = config
        self.token_url = config.token_url
        self.api_create_urls = config.api_create_urls
        self.api_get_all_notification_url = config.api_get_all_notification_url
        self.api_get_notification_url = config.api_get_notification_url
        self.api_apply_notification_bulk_url = config.api_applyNotificationBulk_url
        self.api_push_bulk_csv_url = config.api_push_bulk_csv_url
        self.api_bulk_custom_notification_v4_url = config.api_bulk_custom_notification_v4_url
        self.username = config.username
        self.password = config.password
        self.input_dir = config.input_dir
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

    def run_apply_notification_bulk(self):
        print("Running apply notification bulk")
        apply_notification_bulk = ApplyNotificationBulk(self.config, self.token)
        apply_notification_bulk.run()

    def run_push_bulk_csv(self):
        print("Running push bulk csv")
        push_bulk_csv = PushBulkCsv(self.config, self.token)
        push_bulk_csv.run()

    def run_api_bulk_custom_notification_v4(self):
        print("Running api bulk custom notification v4")
        bulk_custom_notification_v4 = BulkCustomNotification(self.config, self.token)
        bulk_custom_notification_v4.run()

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
    manager.run_apply_notification_bulk()
    manager.run_push_bulk_csv()
    manager.run_api_bulk_custom_notification_v4()
    print("All operations completed")


if __name__ == '__main__':
    main()
