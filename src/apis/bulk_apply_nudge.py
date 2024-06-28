import os
from utils.helpers import Helpers


class Apply_bulk_nudge:
    def __init__(self, config, token):
        print(f"--\nInitializing Apply_bulk_nudge api with endpoint: {config.bulk_apply_nudge_url}")
        self.fetch_api_url = config.get_nudge_url
        self.post_api_url = config.bulk_apply_nudge_url
        self.token = token
        self.input_dir = config.input_dir
        self.input_csv_file_path = os.path.join(self.input_dir, 'bulkapplynudge_v2.csv')
        self.output_dir = config.output_dir
        self.tried_nudge_codes = []
        self.helpers = Helpers()

    def fetch_and_store_get_nudges_data(self):
        data = self.helpers.fetch_nudges_data_from_api(self.fetch_api_url, self.token)
        if data:
            json_filename = os.path.join(self.output_dir, 'applyNudgeData.json')
            csv_filename = os.path.join(self.output_dir, 'applyNudgeData.csv')
            self.helpers.store_data_as_json(data, json_filename)
            self.helpers.store_data_as_csv(data, csv_filename)
            return self.helpers.get_random_nudges_code(data)
        return None

    def ensure_output_directory(self):
        self.helpers.ensure_output_directory(self.output_dir)

    def run(self):
        print("Starting the process...")

        # Ensure output directory exists
        self.ensure_output_directory()

        for attempt in range(4):
            print(f"\nAttempt {attempt + 1}: Fetching and storing code data...")
            # Fetch and store data, and get random code
            random_nudge_code = self.fetch_and_store_get_nudges_data()
            if random_nudge_code:
                self.tried_nudge_codes.append(random_nudge_code)
                print(f"Attempt {attempt + 1}: Random code: {random_nudge_code}")

                # Generate a new TransactionId
                transaction_id = self.helpers.generate_random_transaction_id()

                # Send the PUT request with CSV file and nudge_code
                print(f"Attempt {attempt + 1}: Sending nudge with the random code...")
                success = self.helpers.send_nudge_with_csv(self.post_api_url, self.token,
                                                           random_nudge_code, self.input_csv_file_path, transaction_id)
                if success:
                    print("Nudge sent successfully")
                    break
                else:
                    print("Retrying with a new code...")
            else:
                print("Failed to get a valid code")
                break

        print("Process completed.")
        print("policy_code tried:")
        for code in self.tried_nudge_codes:
            print(code)
