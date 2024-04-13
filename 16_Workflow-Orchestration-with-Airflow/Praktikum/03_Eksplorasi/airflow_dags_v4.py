from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.operators.python_operator import PythonOperator
from datetime import timedelta, datetime
import requests
import pandas as pd

create_table_sql = """
CREATE TABLE IF NOT EXISTS fruits (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(255),
    calories DECIMAL,
    fat DECIMAL,
    sugar DECIMAL,
    carbohydrates DECIMAL,
    protein DECIMAL
);
"""

def fetch_api():
    url = "https://www.fruityvice.com/api/fruit/family/Rosaceae"
    
    response = requests.get(url).json()
    
    df = pd.json_normalize(response)
    
    return df

def insert_data(ti):
    df = ti.xcom_pull(task_ids="get_fruits_data")

    postgres_hook = PostgresHook(postgres_conn_id="my_postgres")
    conn = postgres_hook.get_conn()

    try:
        cursor = conn.cursor()

        for i, row in df.iterrows():
            sql = """
                INSERT INTO fruits (name, calories, fat, sugar, carbohydrates, protein)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            values = (row['name'], row['nutritions.calories'], row['nutritions.fat'], 
                        row['nutritions.sugar'], row['nutritions.carbohydrates'], row['nutritions.protein'])
            cursor.execute(sql, values)

        conn.commit()
    finally:
        if cursor:
            cursor.close()
        conn.close()





default_args = {
    "owner" : "hikmal",
    "retries" : 5,
    "retry_delay" : timedelta(minutes=2)
}

with DAG(
    "Airflow_dags_4",
    default_args=default_args,
    description="dag 4 eksplorasi",
    start_date=datetime(2024, 4, 8),
    schedule_interval="@once"
) as dag:
    t1 = PostgresOperator(
        task_id = "create_fruits_table",
        postgres_conn_id= "my_postgres",
        sql = create_table_sql,
    )
    t2 = PythonOperator(
        task_id = "get_fruits_data",
        python_callable = fetch_api,
    )
    t3 = PythonOperator(
        task_id = "insert_fruits_data",
        python_callable = insert_data,
    )


t1 >> t2 >> t3