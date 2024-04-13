from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import timedelta, datetime

default_args = {
    "owner" : "hikmal",
    "retries" : 5,
    "retry_delay" : timedelta(minutes=2)
}

with DAG(
    'Airflow_dags_1',
    default_args=default_args,
    description='dag 1 prioritas 1',
    start_date=datetime(2024, 4, 8),
    schedule_interval= "@once"
) as dag:
    
    t1 = BashOperator(
        task_id = 'echo_hello_airflow',
        bash_command='echo Hello Airflow',
    )
    
    t2 = BashOperator(
        task_id = 'mkdir_about_us',
        bash_command= 'mkdir -p /home/hikmal/airflow/about_us'
    )
    
    t3 = BashOperator(
        task_id = 'mkdir_our_works',
        bash_command= 'mkdir -p /home/hikmal/airflow/our_works'
    )
    
    t4 = BashOperator(
        task_id='touch_about_us',
        bash_command='touch /home/hikmal/airflow/about_us/about.txt',
    )
    
    t5 = BashOperator(
        task_id='touch_our_works',
        bash_command='touch /home/hikmal/airflow/our_works/works.txt',
    )
    t6 = BashOperator(
        task_id='echo_done',
        bash_command='echo Done!',
    )

t1 >> [t2, t3]

t2 >> t4
t3 >> t5

[t4, t5] >> t6