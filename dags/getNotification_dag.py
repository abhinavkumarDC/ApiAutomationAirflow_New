from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os
import requests
import json
import pandas as pd


def fetch_data_from_api(url, token):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Data fetched successfully")
        return response.json()
    else:
        print(f"Response: {response.text}")
        raise ValueError(f"Failed to fetch data: {response.status_code}")


def store_data_as_json(data, filename):
    print(f"Storing data as JSON in {filename}")
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def store_data_as_csv(data, filename):
    print(f"Storing data as CSV in {filename}")
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)


# Task function to be called by Airflow
def fetch_and_store_data():
    url = "https://stagefirebase.1984.rocks/notification?page=1&size=30"
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzI" \
            "iwiZXhwIjoxNzE3NjU0MTU0LCJpYXQiOjE3MTc2NDY5NTQsImp0aSI6ImRiNjZhODdlZm" \
            "JiOTRhZDg4ZDg3NDk5MDk0MDIwMTYyIiwidXNlcl9pZCI6MTYsImFjdG9yX25hbWUiOiJEQVRB" \
            "Q1VMVFIiLCJhY3Rvcl9pZCI6MTd9.xPpDLWVHiDFYrxNpJ0_UwdEET0IfFCdArYSZdcft67s"

    output_dir = "/home/abhinavkumar/airflow/output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    data = fetch_data_from_api(url, token)
    json_filepath = os.path.join(output_dir, 'data1.json')
    csv_filepath = os.path.join(output_dir, 'data1.csv')

    store_data_as_json(data, json_filepath)
    store_data_as_csv(data, csv_filepath)
    print("Data successfully fetched and stored.")


def print_message():
    print("This is a message printed by the print_message task.")


# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 6, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'cv3_Stage_Get_Notification',
    default_args=default_args,
    description='A simple data fetch DAG',
    schedule=timedelta(days=1),
)

# Defined the PythonOperator task
fetch_and_store_task = PythonOperator(
    task_id='fetch_and_store_data',
    python_callable=fetch_and_store_data,
    dag=dag,
)

print_message_task = PythonOperator(
    task_id='print_message',
    python_callable=print_message,
    dag=dag,
)

# Set task dependencies
fetch_and_store_task >> print_message_task
