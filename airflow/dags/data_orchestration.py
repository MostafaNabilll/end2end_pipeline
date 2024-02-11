from airflow import DAG
from airflow.operators.sensors import S3KeySensor
from airflow.providers.snowflake.transfers.s3_to_snowflake import S3ToSnowflakeOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 2, 10),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'data_orchestration',
    default_args=default_args,
    schedule_interval='@daily',  # Adjust the schedule as needed
    catchup=False
)

s3_sensor_task = S3KeySensor(
    task_id='wait_for_s3_file',
    bucket_name='dogspipeline-personal',
    bucket_key='s3://dogspipeline-personal/data/',
    timeout=6000,
    poke_interval=60,
    mode='poke',
    dag=dag,
)

# Task 2: Update Tables in Snowflake
snowflake_update_task = S3ToSnowflakeOperator(
    task_id='update_snowflake_tables',
    sql='sql_script.sql',
    snowflake_conn_id='snowflake_conn',
    autocommit=True,
    warehouse='compute_wh',
    database='dogpipeline',
    schema='dogs',
    dag=dag,
)

# Task 3: Run dbt Tasks
dbt_task = BashOperator(
    task_id='run_dbt_tasks',
    bash_command='dbt run',
    dag=dag,
)

# Set up task dependencies
s3_sensor_task >> snowflake_update_task >> dbt_task
