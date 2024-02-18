from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from airflow.operators.bash_operator import BashOperator
from airflow.hooks.S3_hook import S3Hook
from airflow.hooks.base_hook import BaseHook
from datetime import datetime, timedelta
import os

current_date = datetime.utcnow().strftime('%Y%m%d%H')
dag_directory = os.path.dirname(os.path.realpath(__file__))
script_path = os.path.join(dag_directory, '../src/data_generator/denormalized_data.py')
PATH_TO_DBT_PROJECT = os.path.join(dag_directory, '../dbt/dogspipeline')

s3_bucket_name = 'dogspipeline-personal'
s3_key_pattern = f'data/output_data_{current_date}.csv'
snowflake_conn_id = 'snowflake_conn'

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 2, 10),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    dag_id='dog_data_generation',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
)

def run_denormalized_data_script(**kwargs):
    aws_conn_id = 'aws_conn'
    aws_hook = BaseHook.get_hook(aws_conn_id)
    
    aws_access_key_id = aws_hook.get_connection(aws_conn_id).login
    aws_secret_access_key = aws_hook.get_connection(aws_conn_id).password

    os.environ['AWS_ACCESS_KEY_ID'] = aws_access_key_id
    os.environ['AWS_SECRET_ACCESS_KEY'] = aws_secret_access_key

    os.system(f'python {script_path}')

def check_s3_file(**kwargs):
    try:
        s3_hook = S3Hook(aws_conn_id='aws_conn')
        bucket_name = 'dogspipeline-personal'
        s3_key = f'data/output_data_{current_date}.csv'

        # Use list_keys() to get a list of keys in the bucket
        keys = s3_hook.list_keys(bucket_name=bucket_name)

        print("List of S3 keys:")
        for key in keys:
            print(key.encode('utf-8'))

        # Check if the specific key exists
        if s3_key in keys:
            print('File added to S3')
            print(s3_key)
            kwargs['ti'].xcom_push(key='s3_key', value=s3_key)
            return s3_key
        else:
            print('No file has been added')
            return None
    except Exception as e:
        print(f'Error checking S3: {str(e)}')
        return None


run_denormalized_data_task = PythonOperator(
    task_id='run_denormalized_data',
    python_callable=run_denormalized_data_script,
    provide_context=True,
    dag=dag,
)

check_s3_objects_task = PythonOperator(
    task_id='check_s3_files',
    python_callable=check_s3_file,
    provide_context=True,
    dag=dag,
)

insert_into_table_task = SnowflakeOperator(
    task_id='insert_into_table',
    snowflake_conn_id=snowflake_conn_id,
    sql="""
        COPY INTO DOGS.stg_data
        FROM @S3_STAGE/
        FILE_FORMAT = (TYPE = 'CSV', FIELD_OPTIONALLY_ENCLOSED_BY = '"', FIELD_DELIMITER = ';', COMPRESSION = 'NONE',   ERROR_ON_COLUMN_COUNT_MISMATCH = FALSE);
    """,
    dag=dag,
)

initate_dbt_task = BashOperator(
    task_id = 'dbt_initiate',
    bash_command = 'dbt deps && dbt seed --select state_codes --profiles-dir . --target dev',
    cwd=PATH_TO_DBT_PROJECT,
    dag=dag,
)

execute_dbt_task = BashOperator(
    task_id = 'dbt_run',
    bash_command = 'dbt deps && dbt run --profiles-dir . --target dev',
    cwd=PATH_TO_DBT_PROJECT,
    dag=dag,
)

test_dbt_data_task = BashOperator(
    task_id='dbt_test',
    bash_command='dbt test --profiles-dir . --target dev',
    cwd=PATH_TO_DBT_PROJECT,
    dag=dag,
)


check_s3_objects_task >> insert_into_table_task
run_denormalized_data_task >> check_s3_objects_task >> insert_into_table_task >> initate_dbt_task >> execute_dbt_task >> test_dbt_data_task
