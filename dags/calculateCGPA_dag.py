from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime , timedelta


# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 7, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

def marks_to_gradepoints(marks):
    if marks >= 90:
        return 10
    elif marks >= 80:
        return 9
    elif marks >= 70:
        return 8
    elif marks >= 60:
        return 7
    elif marks >= 50:
        return 6
    elif marks >= 40:
        return 5
    elif marks >= 30:
        return 4
    else:
        return 0
    

def sem1_GPA():
    marks = [25, 86, 32, 41, 47]
    total_gradepoints = sum(marks_to_gradepoints(mark) for mark in marks)
    gpa = total_gradepoints / len(marks)
    print(f"GPA for Semester 1: {gpa:.2f}")
    return gpa

def sem2_GPA():
    marks = [25, 86, 32, 41, 47]
    total_gradepoints = sum(marks_to_gradepoints(mark) for mark in marks)
    gpa = total_gradepoints / len(marks)
    print(f"GPA for Semester 2: {gpa:.2f}")
    return gpa

def sem3_GPA():
    marks = [25, 86, 32, 41, 47]
    total_gradepoints = sum(marks_to_gradepoints(mark) for mark in marks)
    gpa = total_gradepoints / len(marks)
    print(f"GPA for Semester 3: {gpa:.2f}")
    return gpa

def sem4_GPA():
    marks = [25, 86, 32, 41, 47]
    total_gradepoints = sum(marks_to_gradepoints(mark) for mark in marks)
    gpa = total_gradepoints / len(marks)
    print(f"GPA for Semester 4: {gpa:.2f}")
    return gpa

def sem5_GPA():
    marks = [25, 86, 32, 41, 47]
    total_gradepoints = sum(marks_to_gradepoints(mark) for mark in marks)
    gpa = total_gradepoints / len(marks)
    print(f"GPA for Semester 5: {gpa:.2f}")
    return gpa

def sem6_GPA():
    marks = [25, 86, 32, 41, 47]
    total_gradepoints = sum(marks_to_gradepoints(mark) for mark in marks)
    gpa = total_gradepoints / len(marks)
    print(f"GPA for Semester 6: {gpa:.2f}")
    return gpa

def sem7_GPA():
    marks = [25, 86, 32, 41, 47]
    total_gradepoints = sum(marks_to_gradepoints(mark) for mark in marks)
    gpa = total_gradepoints / len(marks)
    print(f"GPA for Semester 7: {gpa:.2f}")
    return gpa

def sem8_GPA():
    marks = [95, 86, 32, 41, 47]
    total_gradepoints = sum(marks_to_gradepoints(mark) for mark in marks)
    gpa = total_gradepoints / len(marks)
    print(f"GPA for Semester 8: {gpa:.2f}")
    return gpa

# Calculate GPA for semester 1
gpa_sem1 = sem1_GPA()
gpa_sem2 = sem2_GPA()
gpa_sem3 = sem3_GPA()
gpa_sem4 = sem4_GPA()
gpa_sem5 = sem5_GPA()
gpa_sem6 = sem6_GPA()
gpa_sem7 = sem7_GPA()
gpa_sem8 = sem8_GPA()

def total_cgpa():
    total_gpa = (gpa_sem1 + gpa_sem2 + gpa_sem3 + gpa_sem4 + gpa_sem5 + gpa_sem6 + gpa_sem7 + gpa_sem8)/8
    print(total_gpa)

total_cgpa()        

# Define the DAG
with DAG('calculate_cgpa', 
         default_args=default_args,
         description='A DAG with calculation of CGPA of 8 Semester',
         schedule=timedelta(days=1),
         catchup=False) as dag:
    
    sem_1_cgpa = PythonOperator(
        task_id = "sem_1_cgpa",
        python_callable = sem1_GPA
    )
    sem_2_cgpa = PythonOperator(
        task_id = "sem_2_cgpa",
        python_callable = sem1_GPA
    )
    sem_3_cgpa = PythonOperator(
        task_id = "sem_3_cgpa",
        python_callable = sem1_GPA
    )
    sem_4_cgpa = PythonOperator(
        task_id = "sem_4_cgpa",
        python_callable = sem1_GPA
    )
    sem_5_cgpa = PythonOperator(
        task_id = "sem_5_cgpa",
        python_callable = sem1_GPA
    )
    sem_6_cgpa = PythonOperator(
        task_id = "sem_6_cgpa",
        python_callable = sem1_GPA
    )
    sem_7_cgpa = PythonOperator(
        task_id = "sem_7_cgpa",
        python_callable = sem1_GPA
    )
    sem_8_cgpa = PythonOperator(
        task_id = "sem_8_cgpa",
        python_callable = sem1_GPA
    )
    total_cgpa_marks = PythonOperator(
        task_id = "total_cgpa_marks",
        python_callable = total_cgpa
    )

    [sem_1_cgpa, sem_2_cgpa, sem_3_cgpa ,sem_4_cgpa, sem_5_cgpa, sem_6_cgpa, sem_7_cgpa, sem_8_cgpa] >> total_cgpa_marks

