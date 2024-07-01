from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import random

# Define Python functions for the tasks
def task1():
    print("the task1 number is",random.randint(1, 100))

def task2():
    print("the task2 number is",random.randint(1, 100))

def task3():
    print("the task3 number is",random.randint(1, 100))

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 2),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG('bharat_dag', 
         default_args=default_args,
         description='An example DAG with three tasks',
         schedule_interval=timedelta(minutes=2),
         catchup=False) as dag:

    # Define the tasks
    task_1 = PythonOperator(
        task_id='task_1',
        python_callable=task1
    )

    task_2 = PythonOperator(
        task_id='task_2',
        python_callable=task2
    )

    task_3 = PythonOperator(
        task_id='task_3',
        python_callable=task3
    )

    # Define the task dependencies
    task_1 >> task_2 >> task_3
