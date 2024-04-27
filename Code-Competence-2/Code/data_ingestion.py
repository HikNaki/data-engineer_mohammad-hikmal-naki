import os
import logging
import pandas as pd
from airflow import DAG
from datetime import timedelta, datetime
from airflow.utils.decorators import apply_defaults
from airflow.operators.python import PythonOperator


class DatalakeBuilder:

    @apply_defaults
    def __init__(self, logger):
        self.logger = logger

    def read_csv_data(self, file_path):
        try:
            df = pd.read_csv(file_path)
            self.logger.info(f"Data successfully read from the specified file: {file_path}")
            return df
        except Exception as e:
            self.logger.error(f"An error occurred while reading data from {file_path}: {str(e)}")
            raise

    def handle_missing_values(self, df):
        df.fillna(df.mode(), inplace=True)
        return df

    def handle_outliers(self, df, column):
        if column not in df.columns:
            self.logger.warning(f"Column '{column}' not found in data. Skipping outlier handling.")
            return df

        df = df[df[column] != 0]
        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
        return df

    def save_to_parquet(self, df, file_name):
        try:
            df.to_parquet(file_name)
            self.logger.info(f"Data successfully saved in Parquet format: {file_name}")
        except Exception as e:
            self.logger.error(f"An error occurred while saving data to {file_name}: {str(e)}")
            raise

    def validate_data(self, file_path):
        try:
            df = pd.read_parquet(file_path)
            self.logger.info(f"Data successfully displayed from {file_path}:\n{df.head()}")
        except Exception as e:
            self.logger.error(f"An error occurred while validating data from {file_path}: {str(e)}")
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
    dag_id='data_lake_pipeline_dag',
    default_args=default_args,
    start_date=datetime(2024, 4, 20),
    schedule_interval='@daily',
    catchup=False,
    description="A DAG to build and validate data lake",
) as dag:

    logger = logging.getLogger(__name__)
    datalake_builder = DatalakeBuilder(logger)

    folder_path = os.path.expanduser('~/code-competence/data_source')

    file_types = ['customers', 'tickets', 'transactions', 'customer_feedback', 'events']

    read_tasks = {}
    handle_missing_tasks = {}
    handle_outliers_tasks = {}
    save_tasks = {}
    validate_tasks = {}

    for file_type in file_types:
        file_path = f"{folder_path}/{file_type}.csv"

        read_tasks[file_type] = PythonOperator(
            task_id=f"read_{file_type}",
            python_callable=datalake_builder.read_csv_data,
            op_args=[file_path],
        )

        handle_missing_tasks[file_type] = PythonOperator(
            task_id=f"handle_missing_{file_type}",
            python_callable=datalake_builder.handle_missing_values,
            op_args=[read_tasks[file_type].output],
        )

        if file_type == "transactions":
            handle_outliers_tasks[file_type] = PythonOperator(
                task_id=f"handle_outliers_{file_type}",
                python_callable=datalake_builder.handle_outliers,
                op_args=[handle_missing_tasks[file_type].output, "total_amount"],
            )
            save_tasks[file_type] = PythonOperator(
                task_id=f"save_{file_type}",
                python_callable=datalake_builder.save_to_parquet,
                op_args=[handle_outliers_tasks[file_type].output, f"{folder_path}/{file_type}.parquet"],
            )
        else:
            save_tasks[file_type] = PythonOperator(
                task_id=f"save_{file_type}",
                python_callable=datalake_builder.save_to_parquet,
                op_args=[handle_missing_tasks[file_type].output, f"{folder_path}/{file_type}.parquet"],
            )

        validate_tasks[file_type] = PythonOperator(
            task_id=f"validate_{file_type}",
            python_callable=datalake_builder.validate_data,
            op_args=[f"{folder_path}/{file_type}.parquet"],
        )

        read_tasks[file_type].set_downstream(handle_missing_tasks[file_type])
        handle_missing_tasks[file_type].set_downstream(save_tasks[file_type])

        if file_type == "transactions":
            handle_missing_tasks[file_type].set_downstream(handle_outliers_tasks[file_type])
            handle_outliers_tasks[file_type].set_downstream(save_tasks[file_type])

        save_tasks[file_type].set_downstream(validate_tasks[file_type])