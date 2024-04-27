import os
import logging
import pandas as pd
import firebase_admin
from airflow import DAG
from firebase_admin import storage
from firebase_admin import credentials
from datetime import datetime,timedelta
from airflow.utils.decorators import apply_defaults
from airflow.operators.python import PythonOperator


class DataWarehouseLoader:

    @apply_defaults
    def __init__(self, logger):
        self.logger = logger

    def load_data(self, file_path):
        try:
            df = pd.read_parquet(file_path)
            self.logger.info(f"Data successfully read from the specified file: {file_path}")
            return df
        except Exception as e:
            self.logger.error(f"An error occurred while reading data from {file_path}: {str(e)}")
            raise

    def transform_data(self, transactions, tickets, events, customer_feedback, customers) :
        try:
            # Menggabungkan tabel transactions dengan tickets berdasarkan ticket_id
            merged_data = pd.merge(transactions, tickets, on='ticket_id', how='inner')

            # Menggabungkan tabel merged_data dengan events berdasarkan event_id
            merged_data = pd.merge(merged_data, events, on='event_id', how='inner')

            # Menghitung jumlah tiket yang terjual per acara
            Tickets_sold_per_event = merged_data.groupby('event_id')['quantity'].sum().reset_index()

            # Menghitung total pendapatan dari setiap acara
            Revenue_per_event = merged_data.groupby('event_id')['total_amount'].sum().reset_index()

            # Menggabungkan tabel merged data dengan customers berdasarkan customer_id
            transactions_data = pd.merge(merged_data, customers, on='customer_id', how='inner')
            
            # Menggabungkan tabel customer_feedback dengan transactions berdasarkan transaction_id
            feedback_data = pd.merge(customer_feedback, transactions_data, on='transaction_id', how='inner')

            # Analisis rating rata-rata per acara
            Feedback_analysis = feedback_data.groupby('event_id')['rating'].mean().reset_index()
            
            
            self.logger.info(f"Data successfully transformed")
            return Tickets_sold_per_event, Revenue_per_event, Feedback_analysis
        except Exception as e:
            self.logger.error(f"An error occured while transform data: {str(e)}")
            raise

    def save_to_warehouse(self, df, table_name):
        try:
            if not firebase_admin._apps:
                cred = credentials.Certificate("serviceAccountKey.json")
                storage_bucket = "de-cloud-15.appspot.com"
                firebase_admin.initialize_app(cred, {"storageBucket": storage_bucket})
                
            bucket = storage.bucket()
            current_date = datetime.now().strftime("%Y-%m-%d")
            folder_path = os.path.expanduser('~/code-competence/data_source')
            
            for i, name in zip(df, table_name):
                i.to_parquet(f"{folder_path}/{name}.parquet")
            
            for name in table_name:
                blob = bucket.blob(f"{current_date}/{name}.parquet")
                blob.upload_from_filename(f"{folder_path}/{name}.parquet")

            self.logger.info(f"Data has been successfully loaded to the storage")
        except Exception as e:
            self.logger.error(f"An Error Occured while loading data: {str(e)}")
            raise

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

default_args = {
    'owner': 'hikmal',
    'retries': 5,
    'retry_delay': timedelta(minutes=2),
}

with DAG(
    dag_id='data_warehouse_pipeline_dag',
    default_args=default_args,
    start_date=datetime(2024, 4, 21),
    schedule_interval='@daily',
    catchup=False,
    description="A DAG to transform and load data warehouse",
) as dag:
    
    logger = logging.getLogger(__name__)
    loader = DataWarehouseLoader(logger)

    folder_path = os.path.expanduser('~/code-competence/data_source')
    table_name = ["Tickets_sold_per_event", "Revenue_per_event", "Feedback_analysis"]

    # Load data tasks
    load_transactions = PythonOperator(
        task_id="load_transactions",
        python_callable=loader.load_data,
        op_args=[f"{folder_path}/transactions.parquet"],
    )

    load_tickets = PythonOperator(
        task_id="load_tickets",
        python_callable=loader.load_data,
        op_args=[f"{folder_path}/tickets.parquet"],
    )

    load_events = PythonOperator(
        task_id="load_events",
        python_callable=loader.load_data,
        op_args=[f"{folder_path}/events.parquet"],
    )

    load_customer_feedback = PythonOperator(
        task_id="load_customer_feedback",
        python_callable=loader.load_data,
        op_args=[f"{folder_path}/customer_feedback.parquet"],
    )

    load_customers = PythonOperator(
        task_id="load_customers",
        python_callable=loader.load_data,
        op_args=[f"{folder_path}/customers.parquet"],
    )

    transform_data = PythonOperator(
        task_id="transform_data",
        python_callable=loader.transform_data,
        op_args=[load_transactions.output, load_tickets.output, load_events.output,
                 load_customer_feedback.output, load_customers.output],
    )

    save_to_warehouse = PythonOperator(
        task_id="save_to_warehouse",
        python_callable=loader.save_to_warehouse,
        op_args=[transform_data.output, table_name],
    )

    load_transactions.set_downstream(transform_data)
    load_tickets.set_downstream(transform_data)
    load_events.set_downstream(transform_data)
    load_customer_feedback.set_downstream(transform_data)
    load_customers.set_downstream(transform_data)
    transform_data.set_downstream(save_to_warehouse)

