import os
import json
import pandas as pd


class Helpers:
    @staticmethod
    def ensure_output_directory(directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
        print(f"Output directory ensured at: {directory}")

    @staticmethod
    def store_data_as_json(data, filename):
        print(f"Storing data as JSON in {filename}")
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Data stored as JSON in {filename}")

    @staticmethod
    def store_data_as_csv(data, filename):
        print(f"Storing data as CSV in {filename}")
        df = pd.DataFrame([data])
        df.to_csv(filename, index=False)
        print(f"Data stored as CSV in {filename}")
