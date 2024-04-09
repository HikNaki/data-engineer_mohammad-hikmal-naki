from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import logging
import os
import pandas as pd
import matplotlib.pyplot as plt

default_args = {
    'owner': 'hikmal',
    'retries': 5,
    'retry_delay': timedelta(minutes=2),
}

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Tambahkan formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Tambahkan handler ke logger
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
logger.addHandler(ch)

def extract_data():
    try:
        url = "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/inst/extdata/penguins.csv"
        df = pd.read_csv(url)
        logger.info("Data berhasil diekstrak.")
        return df
    except Exception as e:
        logger.error(f"Terjadi kesalahan saat mengekstrak data: {str(e)}")
        raise

def transform_data(ti):    
    try:
        df = ti.xcom_pull(task_ids='extract_data')
        kolom_null = df.columns[df.isnull().any()].tolist()
        df.dropna(subset=kolom_null, inplace=True)
        logger.info("Data berhasil ditransformasi.")
        return df
    except Exception as e:
        logger.error(f"Terjadi kesalahan saat mentransformasi data: {str(e)}")
        raise

def export_to_excel(ti):
    try:
        df = ti.xcom_pull(task_ids='transform_data')
        airflow_data_folder = os.path.expanduser('~/airflow/data-source')
        if not os.path.exists(airflow_data_folder):
            os.makedirs(airflow_data_folder)
        filepath = os.path.join(airflow_data_folder, 'penguins_data.xlsx')
        df.to_excel(filepath, index=False)
        logger.info("Data berhasil diekspor ke Excel.")
    except Exception as e:
        logger.error(f"Terjadi kesalahan saat mengekspor data ke Excel: {str(e)}")
        raise

def visualize_data():
    try:
        airflow_data_folder = os.path.expanduser('~/airflow/data-source')
        filepath = os.path.join(airflow_data_folder, 'penguins_data.xlsx')
        df = pd.read_excel(filepath)
        
        species_count = df['species'].value_counts()

        plt.figure(figsize=(8, 6))
        plt.pie(species_count, labels=species_count.index, autopct='%1.2f%%')
        plt.axis('equal')
        plt.title('Persentase Jumlah Spesies')
        output_filepath = os.path.join(airflow_data_folder, 'species.png')
        plt.savefig(output_filepath)
        logger.info("Visualisasi data berhasil dibuat.")
    except Exception as e:
        logger.error(f"Terjadi kesalahan saat membuat visualisasi data: {str(e)}")
        raise


with DAG(
    'data_analysis_workflow', 
    default_args=default_args,
    start_date=datetime(2024, 4, 4),
    schedule_interval='@daily',
    catchup=False
) as dag:
    extract_task = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data,
    )

    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data,
        provide_context=True,
    )

    export_task = PythonOperator(
        task_id='export_to_excel',
        python_callable=export_to_excel,
        provide_context=True,
    )

    visualize_task = PythonOperator(
        task_id='visualize_data',
        python_callable=visualize_data,
    )

extract_task >> transform_task 

transform_task >> export_task

export_task >> visualize_task
