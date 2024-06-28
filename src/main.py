from src.apis.push_bulk_csv import PushBulkCsv
from src.apis.cancel_release import Cancel_release
from utils.token import TokenManager
from utils.helpers import Helpers
from apis.get_All_NotificationNew import GetAllNotification
from apis.get_Notification import GetNotification
from apis.create_Engage_Notification import CreateNotification
from apis.applynotificationbulk_v4 import ApplyNotificationBulk
from apis.bulk_custom_notification_v4 import BulkCustomNotification
# from apis.create_Notification import CreateNotification
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
from apis.bulkApplyUnlock import Bulk_unlock
from apis.bulk_apply_lock import Bulk_apply_lock
from apis.get_nudges import Get_nudges
from apis.bulk_apply_nudge import Apply_bulk_nudge
from config import Config


class OdysseyManager:
    def __init__(self, config):
        print("Initializing Main File- NotificationManager")
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
        # print("NotificationManager initialized")
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
        self.bulk_unlock_url = config.bulk_unlock_url
        self.bulk_lock_url = config.bulk_lock_url
        self.lock_csv_file = config.lock_csv_file
        self.get_nudge_url = config.get_nudge_url
        self.bulk_apply_nudge_url = config.bulk_apply_nudge_url
        self.token = None
        self.transaction_id = None
        self.nudge_types = []
        self.policy_code = None
        # print("OdysseyManager initialized")

    def generate_token(self):
        if self.token is None:
            # print("Generating token")
            self.token = TokenManager.generate_token(self.token_url, self.username, self.password)
            if self.token is None:
                print("Failed to obtain token. Exiting.")
                return False
            print("Token generated successfully\n--")
        return True

    def run_get_all_notification(self):
        # print("Running get all notification")
        get_all_notification = GetAllNotification(self.api_get_all_notification_url, self.token, self.output_dir)
        get_all_notification.fetch_and_store_get_all_notification_data()
        print("Get All notification api executed and data stored in provided directory")

    def run_get_notification(self):
        # print("Running get notification")
        get_notification = GetNotification(self.api_get_notification_url, self.token, self.output_dir)
        get_notification.fetch_and_store_get_notification_data()
        print("Get notification api executed and data stored in provided directory")

    def run_get_all_nudges(self):
        print("get the details of all nudges")
        get_all_nudge = Get_all_Nudges(self.get_all_nudges_url, self.token, self.output_dir)
        get_all_nudge.fetch_and_store_get_all_nudge_data()
        print("Get All nudge api executed and data stored in provided directory")

    def run_get_nudges(self):
        print("Get nudges request")
        get_nudge = Get_nudges(self.get_nudge_url, self.token, self.output_dir)
        get_nudge.fetch_and_store_get_nudge_data()
        print("received nudges")

    def run_apply_bulk_nudge(self):
        print("apply bulk nudges on imei")
        apply_bulk_nudge = Apply_bulk_nudge(self.config, self.token)
        apply_bulk_nudge.run()
        print("applied nudges on devices")

    def set_nudge_types(self, *nudge_types):
        self.nudge_types = nudge_types

    def run_create_nudges(self):
        for nudge_type in self.nudge_types:
            print(f"--\nCreating nudges for type: {nudge_type}")
            create_nudges = Create_nudges(self.create_nudge_url, self.token, nudge_type, self.output_dir)
            create_nudges.fetch_and_store_created_allNudges_data()
            print(f"Created nudges for type: {nudge_type} successfully")

    def run_apply_unlock(self):
        print("apply unlock on device")
        apply_unlock = Apply_unlock(self.apply_unlock_url, self.token)
        apply_unlock.send_imei_for_unlock()
        print("device is unlocked successfully")

    def run_bulk_unlock_devices(self):
        print("unlock the devices in bulk")
        bulk_unlock = Bulk_unlock(self.config, self.token)
        bulk_unlock.bulk_apply_unlock()
        print("unlock all the imei")

    def run_bulk_lock_devices(self):
        print("bulk lock has been triggered on devices")
        bulk_lock = Bulk_apply_lock(self.config, self.token)
        bulk_lock.apply_bulk_lock_v3()
        print("bulk lock has been applied on device")

    def run_create_notification(self):
        # print("Running create notification")
        for notification_type, api_create_url in self.api_create_urls.items():
            # print(f"Creating notification for type: {notification_type}")
            create_notification = CreateNotification(api_create_url, self.token, notification_type, self.output_dir)
            create_notification.fetch_and_store_created_notification_data()
            # print(f"Notification created for type: {notification_type}")

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
        bulk_release = Bulk_release_devices(self.config, self.token)
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
        # print("Ensuring output directory")
        Helpers.ensure_output_directory(self.output_dir)
        # print("Output directory ensured")


def main():
    print("Starting main function")
    # Load configuration
    config = Config('config/config.json')

    manager = OdysseyManager(config)

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
    manager.run_get_nudges()
    manager.run_get_all_nudges()
    # Set the nudge type
    manager.set_nudge_types('Loan_Wallpaper_Block', 'Application_Block', 'Call_Barring')
    manager.run_create_nudges()
    manager.run_apply_bulk_nudge()
    manager.run_bulk_lock_devices()
    manager.run_get_passcode()  # offline unlock
    manager.run_apply_unlock()
    manager.run_bulk_unlock_devices()
    manager.run_release_device()
    manager.run_bulk_release_devices()
    manager.run_cancel_release()
    manager.run_device_status()
    manager.run_registeration_file()
    manager.run_current_status()  # Getting status code 400 {"message":"imei_list is required"}
    manager.run_device_log()
    manager.run_last_online()
    print(f"--\nAll operations completed")


if __name__ == '__main__':
    main()
