from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from tmt_scraper import tmt_dag

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date' : datetime(2023, 8, 15),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'tmt_dag',
    default_args=default_args,
    description='DAg to scrap phone repair prices from tmt uk website',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 8, 15),
    catchup=False,
)

run_dag = PythonOperator(
    task_id='complete_tmt_etl',
    python_callable = tmt_dag,
    dag = dag,
)

run_dag