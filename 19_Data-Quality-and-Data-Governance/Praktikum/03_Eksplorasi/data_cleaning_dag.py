from airflow.decorators import dag, task
from datetime import datetime, timedelta
import pandas as pd
import requests
import os
import logging

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
    'data_cleaning_pipeline_v1', 
    default_args=default_args,
    description="simple data cleaning pipeline",
    start_date=datetime(2024, 4, 20),
    schedule_interval='@daily',
    catchup=False
)
def simple_pipeline():
    
    @task()
    def extract_data():
        try :
            url = "https://gist.githubusercontent.com/nadirbslmh/b50406d5579e875e6435896c9ff6c80c/raw/cac8007653b6145e9ad0ec69b1e4fd6c1be718e7/transactions.json"   
            response = requests.get(url)
            data = response.json()
            logger.info(f"Data has been successfully extracted")
            return data
        except Exception as e:
            logger.error(f"An error occured: {str(e)}")
            raise

    @task()
    def data_cleaning(data) -> pd.DataFrame:
        try:
            def format_to_rp(amount):
                return 'Rp {:,.0f}'.format(amount).replace(',', '.')
            
            df = pd.json_normalize(data)
            df["phone_number"] = df["phone_number"].apply(lambda x: str('+62' + str(x)))
            df["transaction_amount"] = df["transaction_amount"].map(format_to_rp)
            filtered_df = df[(df['transaction_status'] == 'success')]
            
            data_folder = os.path.expanduser('~/airflow/data-source')
            file_path = os.path.join(data_folder, 'transactions.csv')
            filtered_df.to_csv(file_path, index=False)
            logger.info(f"Data has been successfully loaded to the storage")
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            raise

    data = extract_data()
    data_cleaning(data)

data_cleaning_dag = simple_pipeline()