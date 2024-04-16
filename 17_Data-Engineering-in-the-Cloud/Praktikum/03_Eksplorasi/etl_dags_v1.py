from airflow.decorators import dag, task 
from datetime import datetime, timedelta
from firebase_admin import credentials
from firebase_admin import storage
import firebase_admin
import logging
import pandas as pd
import requests
import os

default_args = {
    'owner': 'hikmal',
    'retries': 5,
    'retry_delay': timedelta(minutes=2),
}

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
logger.addHandler(ch)

@dag(
    'etl_pipeline', 
    default_args=default_args,
    start_date=datetime(2024, 4, 15),
    schedule_interval='@once',
    catchup=False
)
def etl_pipeline():
    @task()
    def extract_data():
        try :
            url = "https://fakestoreapi.com/products"
            response = requests.get(url)
            data = response.json()
            logger.info(f"Data has been successfully extracted")
            return data
        except Exception as e:
            logger.error(f"An error occured: {str(e)}")
            raise

    @task()
    def transform_data(data) :
        df = pd.json_normalize(data)
        filtered_df = df[df['price'] > 100]
        selected_columns = ['title', 'price', 'description', 'category']
        result_df = filtered_df[selected_columns]
        return result_df
    
    @task()
    def load_data(data) :
        try:
            cred = credentials.Certificate("/home/hikmal/airflow/serviceAccountKey.json")
            storage_bucket = "project-1-418609.appspot.com"
            firebase_admin.initialize_app(cred, {"storageBucket": storage_bucket})
            bucket = storage.bucket()
            
            data_folder = os.path.expanduser('~/airflow/data-source')
            file_path = os.path.join(data_folder, 'products.parquet')
            file_name = "products.parquet"
            data.to_parquet(file_path)
            blob = bucket.blob(file_name)
            blob.upload_from_filename(file_path)
            logger.info(f"Data has been successfully loaded to the storage")
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            raise



    #Execute Task
    extract = extract_data()
    transform = transform_data(extract)
    load_data(transform)

etl_pipeline_dag = etl_pipeline()