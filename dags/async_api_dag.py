# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from datetime import datetime, timedelta
# import requests

# # Define the URL
# url = 'https://jsonplaceholder.typicode.com/posts/1/comments'

# # Function to fetch data from the API
# def fetch_data():
#     response = requests.get(url)
#     if response.status_code == 200:
#         # Extract the JSON data from the response
#         data = response.json()
#         print(data[0])

# # Define the default arguments for the DAG
# default_args = {
#     'owner': 'airflow',
#     'start_date': datetime(2024, 5, 3),
#     'retries': None,
# }

# # Define the DAG
# dag = DAG(
#     'fetch_api_data',
#     default_args=default_args,
#     description='A DAG to fetch data from an API',
#     schedule_interval=None,
# )

# # Define the PythonOperator to fetch data
# fetch_data_task = PythonOperator(
#     task_id='fetch_data',
#     python_callable=fetch_data,
#     dag=dag,
# )

# # Define the PythonOperator to print "Hello, World!"
# def print_hello():
#     print("Hello, World!")

# def print_something_else():
#     print("Something else!")

# # Function to print another message
# def print_another_message():
#     print("Another message!")    

# print_hello_task = PythonOperator(
#     task_id='print_hello',
#     python_callable=print_hello,
#     dag=dag,
# )

# # Define the PythonOperator to print "Something else!"
# print_something_else_task = PythonOperator(
#     task_id='print_something_else',
#     python_callable=print_something_else,
#     dag=dag,
# )

# # Define the PythonOperator to print "Another message!"
# print_another_message_task = PythonOperator(
#     task_id='print_another_message',
#     python_callable=print_another_message,
#     dag=dag,
# )

# # Set the task dependencies
# print_hello_task >> fetch_data_task >> print_something_else_task >> print_another_message_task 

# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from datetime import datetime, timedelta
# import requests

# # Define the URL
# url = 'https://jsonplaceholder.typicode.com/posts/1/comments'

# # Function to fetch data from the API
# def fetch_data():
#     response = requests.get(url)
#     if response.status_code == 200:
#         # Extract the JSON data from the response
#         data = response.json()
#         print(data[0])

# # Define the default arguments for the DAG
# default_args = {
#     'owner': 'airflow',
#     'start_date': datetime(2024, 5, 3),
#     'retries': None,
# }

# # Define the DAG
# dag = DAG(
#     'fetch_api_data',
#     default_args=default_args,
#     description='A DAG to fetch data from an API',
#     schedule_interval=None,
# )

# # Define the PythonOperator to fetch data
# fetch_data_task = PythonOperator(
#     task_id='fetch_data',
#     python_callable=fetch_data,
#     dag=dag,
# )

# # Define the PythonOperator to print "Hello, World!"
# def print_hello():
#     print("Hello, World!")

# def print_something_else():
#     print("Something else!")

# # Function to print another message
# def print_another_message():
#     print("Another message!")    

# print_hello_task = PythonOperator(
#     task_id='print_hello',
#     python_callable=print_hello,
#     dag=dag,
# )

# # Define the PythonOperator to print "Something else!"
# print_something_else_task = PythonOperator(
#     task_id='print_something_else',
#     python_callable=print_something_else,
#     dag=dag,
# )

# # Define the PythonOperator to print "Another message!"
# print_another_message_task = PythonOperator(
#     task_id='print_another_message',
#     python_callable=print_another_message,
#     dag=dag,
# )

# # Set the task dependencies
# print_hello_task >> print_something_else_task >> fetch_data_task >> print_another_message_task 


from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests
import asyncio

# Define the URL
url = 'https://jsonplaceholder.typicode.com/posts/1/comments'

# Asynchronous function to fetch data from the API
async def fetch_data_async():
    try:
        response = await asyncio.get_event_loop().run_in_executor(None, requests.get, url)
        response.raise_for_status()  # Raise an exception for 4XX and 5XX status codes
        data = response.json()
        print(data[0])
    except Exception as e:
        print(f"An error occurred while fetching data: {e}")

# Synchronous function to wrap the asynchronous task
def fetch_data():
    asyncio.run(fetch_data_async())

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 5, 3),
    'retries': None,
}

# Define the DAG
dag = DAG(
    'fetch_api_data',
    default_args=default_args,
    description='A DAG to fetch data from an API',
    schedule_interval=None,
)

# Define the PythonOperator to fetch data
fetch_data_task = PythonOperator(
    task_id='fetch_data',
    python_callable=fetch_data,
    dag=dag,
)

# Define the PythonOperator to print "Hello, World!"
def print_hello():
    print("Hello, World!")

def print_something_else():
    print("Something else!")

# Function to print another message
def print_another_message():
    print("Another message!")    

print_hello_task = PythonOperator(
    task_id='print_hello',
    python_callable=print_hello,
    dag=dag,
)

# Define the PythonOperator to print "Something else!"
print_something_else_task = PythonOperator(
    task_id='print_something_else',
    python_callable=print_something_else,
    dag=dag,
)

# Define the PythonOperator to print "Another message!"
print_another_message_task = PythonOperator(
    task_id='print_another_message',
    python_callable=print_another_message,
    dag=dag,
)

# Set the task dependencies
print_hello_task >> print_something_else_task >> fetch_data_task >> print_another_message_task


