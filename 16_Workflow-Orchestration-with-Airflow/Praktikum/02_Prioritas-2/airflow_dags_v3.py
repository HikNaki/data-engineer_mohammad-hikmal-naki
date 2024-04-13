from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import timedelta, datetime
import requests
import pandas as pd

def fetch_api():
    url = "https://fakestoreapi.com/products"
    
    response = requests.get(url).json()
    
    df = pd.json_normalize(response)
    
    return df

def write_csv(ti):
    df = ti.xcom_pull(task_ids="fetch_data")
    df.to_csv("data-source/products.csv", index=False)

def write_txt(ti):
    df = ti.xcom_pull(task_ids="fetch_data")
    df.to_csv("data-source/products.txt", sep="\t", index=False)

default_args = {
    "owner" : "hikmal",
    "retries" : 5,
    "retry_delay" : timedelta(minutes=2)
}

with DAG(
    "Airflow_dags_3",
    default_args=default_args,
    description="dag 3 prioritas 2",
    start_date=datetime(2024, 4, 8),
    schedule_interval="@once"
) as dag:
    t1 = PythonOperator(
        task_id = "fetch_data",
        python_callable = fetch_api,
    )
    t2 = PythonOperator(
        task_id = "write_to_csv",
        python_callable = write_csv,
    )
    t3 = PythonOperator(
        task_id = "write_to_txt",
        python_callable = write_txt,
    )
    t4 = BashOperator(
        task_id = "echo_done",
        bash_command= "echo Done!"
    )

t1 >> [t2, t3]

t4 << [t2, t3]