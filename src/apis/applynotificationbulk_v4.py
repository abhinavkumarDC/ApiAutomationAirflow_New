import os
from utils.helpers import Helpers


class ApplyNotificationBulk:
    def __init__(self, config, token):
        self.fetch_api_url = config.api_get_all_notification_url
        self.post_api_url = config.api_applyNotificationBulk_url
        self.token = token
        self.input_dir = config.input_dir
        self.output_dir = config.output_dir
        self.tried_notification_codes = []
        self.helpers = Helpers()
        self.input_csv_file_path = os.path.join(self.input_dir, 'v4.csv')

    def fetch_and_store_get_notification_data(self):
        data = self.helpers.fetch_data_from_api(self.fetch_api_url, self.token)
        if data:
            json_filename = os.path.join(self.output_dir, 'applyNotificationData.json')
            csv_filename = os.path.join(self.output_dir, 'applyNotificationData.csv')
            self.helpers.store_data_as_json(data, json_filename)
            self.helpers.store_data_as_csv(data, csv_filename)
            return self.helpers.get_random_notification_code(data)
        return None

    def ensure_output_directory(self):
        self.helpers.ensure_output_directory(self.output_dir)

    def run(self):
        print("Starting the process...")

        # Ensure output directory exists
        self.ensure_output_directory()

        for attempt in range(4):
            print(f"\nAttempt {attempt + 1}: Fetching and storing notification data...")
            # Fetch and store data, and get random notification code
            random_notification_code = self.fetch_and_store_get_notification_data()
            if random_notification_code:
                self.tried_notification_codes.append(random_notification_code)
                print(f"Attempt {attempt + 1}: Random notification code: {random_notification_code}")

                # Generate a new TransactionId
                transaction_id = self.helpers.generate_random_transaction_id()

                # Send the POST request with CSV file and notification_code
                print(f"Attempt {attempt + 1}: Sending notification with the random code...")
                success = self.helpers.send_notification_with_csv(self.post_api_url, self.token,
                                                                  random_notification_code, self.input_csv_file_path,
                                                                  transaction_id)
                if success:
                    print("Notification sent successfully")
                    break
                else:
                    print("Retrying with a new notification code...")
            else:
                print("Failed to get a valid notification code")
                break

        print("Process completed.")
        print("Notification codes tried:")
        for code in self.tried_notification_codes:
            print(code)
