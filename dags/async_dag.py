import asyncio
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def sync_fn():
    async def fn():
        print('My name is ')
        await asyncio.sleep(10)
        print('Yadav')
        await asyncio.sleep(1)
        print('Bharat')

    asyncio.run(fn())

default_args = {
    'owner': "bharat",
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 3),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG('async_dag',
         default_args=default_args,
         description='Async Function',
         schedule_interval=timedelta(minutes=2),
         catchup=False) as dag:
    
    task = PythonOperator(
        task_id='task',
        python_callable=sync_fn
    )
