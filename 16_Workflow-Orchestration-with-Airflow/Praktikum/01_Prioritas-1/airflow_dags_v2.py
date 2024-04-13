from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import timedelta, datetime
import random

def generate_number():
    random_num = []
    
    for i in range(25):
        random_num.append(random.randint(1,50))
    
    return random_num

def sum_number(ti):
    
    random_num = ti.xcom_pull(task_ids="generate_number")
    total = sum(random_num)
    
    return total

def check_num(ti):
    
    total_num = ti.xcom_pull(task_ids="sum_number")
    if total_num % 2 == 0 :
        print(f"Even Sum")
    else :
        print(f"Odd Sum")


default_args = {
    "owner" : "hikmal",
    "retries" : 5,
    "retry_delay" : timedelta(minutes=2)
}

with DAG(
    'Airflow_dags_2',
    default_args=default_args,
    description='dag 2 prioritas 1',
    start_date=datetime(2024, 4, 8),
    schedule_interval= "@once"
) as dag:
    t1 = PythonOperator(
        task_id = "generate_number",
        python_callable = generate_number
    )
    t2 = PythonOperator(
        task_id = "sum_number",
        python_callable = sum_number
    )
    t3 = PythonOperator(
        task_id = "check_num",
        python_callable = check_num
    )

t1 >> t2 >> t3