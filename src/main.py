from src.apis.cancel_release import Cancel_release
from utils.token import TokenManager
from utils.helpers import Helpers
from apis.get_All_NotificationNew import GetAllNotification
from apis.get_Notification import GetNotification
from apis.create_Notification import CreateNotification
from apis.get_passcode import Get_Passcode
from apis.release_device import Release_device
from apis.bulk_release import Bulk_release_devices
from apis.device_status import Device_status
from apis.registeration_report import Registration_report
from apis.current_status import Current_status_report
from apis.device_logs import Device_logs
from apis.last_online import Last_online_status
from src.apis.create_nudge.get_all_nudges import Get_all_Nudges
from src.apis.create_nudge.create_All_Nudges import Create_nudges
from src.apis.applyunlock import Apply_unlock
from config import Config


class OdysseyManager:
    def __init__(self, config):
        print("Initializing OdysseyManager")
        self.token_url = config.token_url
        self.api_create_urls = config.api_create_urls
        self.api_get_all_notification_url = config.api_get_all_notification_url
        self.api_get_notification_url = config.api_get_notification_url
        self.username = config.username
        self.password = config.password
        self.get_passcode_url = config.get_passcode_url
        self.get_release_url = config.get_release_url
        self.bulk_release_url = config.bulk_release_url
        self.release_csv_file_path = config.release_csv_file_path
        self.cancel_release_url = config.cancel_release_url
        self.device_status_url = config.device_status_url
        self.registration_report_url = config.registration_report_url
        self.current_status_url = config.current_status_url
        self.device_logs_url = config.device_logs_url
        self.last_online_status_url = config.last_online_status_url
        self.get_all_nudges_url = config.get_all_nudges_url
        self.create_nudge_url = config.create_nudge_url
        self.apply_unlock_url = config.apply_unlock_url
        self.output_dir = config.output_dir
        self.token = None
        self.transaction_id = None
        self.nudge_type = None
        print("OdysseyManager initialized")

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

    def run_get_all_nudges(self):
        print("get the details of all nudges")
        get_all_nudge = Get_all_Nudges(self.get_all_nudges_url, self.token)
        get_all_nudge.fetch_data_from_api()
        print("received details of all nudges")

    def run_create_nudges(self):
        print("create nudges")
        create_nudges = Create_nudges(self.create_nudge_url, self.token, self.nudge_type)
        create_nudges.create_nudges_from_api()
        print("created nudges successfully")

    def run_apply_unlock(self):
        print("apply unlock on device")
        apply_unlock = Apply_unlock(self.apply_unlock_url, self.token)
        apply_unlock.send_imei_for_unlock()
        print("device is unlocked successfully")

    def run_create_notification(self):
        print("Running create notification")
        for notification_type, api_create_url in self.api_create_urls.items():
            print(f"Creating notification for type: {notification_type}")
            create_notification = CreateNotification(api_create_url, self.token, notification_type, self.output_dir)
            create_notification.fetch_and_store_created_notification_data()
            print(f"Notification created for type: {notification_type}")

    def run_get_passcode(self):
        print("receive passcode api")
        get_passcode = Get_Passcode(self.get_passcode_url, self.token)
        get_passcode.send_passkey_for_pin_unlock()
        print("received passcode for passkey")

    def run_release_device(self):
        print("running release device")
        release_device = Release_device(self.get_release_url, self.token)
        release_device.release_device()
        print("imei is released")

    def run_bulk_release_devices(self):
        print("release the devices in bulk")
        bulk_release = Bulk_release_devices(self.bulk_release_url, self.token, self.release_csv_file_path,
                                            self.transaction_id)
        bulk_release.send_device_data_in_csv()
        print("release all the imei's")

    def run_cancel_release(self):
        print("cancel the release devices")
        cancel_release = Cancel_release(self.cancel_release_url, self.token)
        cancel_release.cancel_release_imei()
        print("imei is canceled")

    def run_device_status(self):
        print("get the details of apply action on device.")
        device_status = Device_status(self.device_status_url)
        device_status.device_Status_of_imei()
        print("received the details of last action on device.")

    def run_registeration_file(self):
        print("get the details of registered device.")
        registeration_report = Registration_report(self.registration_report_url)
        registeration_report.registration_report_imei()
        print("details of registered device.")

    def run_current_status(self):
        print("get the details of current status.")
        current_status = Current_status_report(self.current_status_url)
        current_status.current_Status()
        print("get the details of current status.")

    def run_device_log(self):
        print("get the device history")
        device_logs = Device_logs(self.device_logs_url)
        device_logs.device_log_history()
        print("received the device history")

    def run_last_online(self):
        print("get the last online status")
        last_online = Last_online_status(self.last_online_status_url)
        last_online.get_last_online()
        print("receive the last online status")

    def ensure_output_directory(self):
        print("Ensuring output directory")
        Helpers.ensure_output_directory(self.output_dir)
        print("Output directory ensured")


def main():
    print("Starting main function")
    # Load configuration
    config = Config('config/config.json')

    manager = OdysseyManager(config)

    if not manager.generate_token():
        return

    manager.ensure_output_directory()

    # Run desired operations
    # manager.run_get_notification()
    # manager.run_get_all_notification()
    # manager.run_create_notification()
    #manager.run_get_passcode()
    #manager.run_release_device()
    #manager.run_bulk_release_devices()
    #manager.run_cancel_release()
    #manager.run_device_status()
    #manager.run_registeration_file()
    #manager.run_current_status()
    #manager.run_device_log()
    #manager.run_get_all_nudges()
    #manager.run_create_nudges()
    manager.run_apply_unlock()
    #manager.run_last_online()
    print("All operations completed")


if __name__ == '__main__':
    main()
