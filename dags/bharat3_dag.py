from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import random

# Define Python functions for the tasks
def generate_random_number():
    return random.randint(1, 100)

def multiply_by_two(num):
    return num * 2

def square_number(num):
    return num ** 2

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG('bharat2_dag', 
         default_args=default_args,
         description='A DAG with three tasks where the second and third tasks take input from the first and second tasks, respectively',
         schedule=timedelta(days=1),
         catchup=False) as dag:

    # Define the tasks
    generate_number = PythonOperator(
        task_id='generate_number',
        python_callable=generate_random_number
    )

    multiply_task = PythonOperator(
        task_id='multiply_task',
        python_callable=multiply_by_two,
        op_kwargs={'num': "{{ task_instance.xcom_pull(task_ids='generate_number') }}"}  # Get output from previous task
    )

    square_task = PythonOperator(
        task_id='square_task',
        python_callable=square_number,
        op_kwargs={'num': "{{ task_instance.xcom_pull(task_ids='multiply_task') }}"}  # Get output from previous task
    )

    # Define the task dependencies
    generate_number >> multiply_task >> square_task
