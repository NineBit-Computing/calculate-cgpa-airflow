from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from fastapi import FastAPI, HTTPException
from datetime import datetime , timedelta
from pydantic import BaseModel
from typing import List
import asyncio

app = FastAPI()

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 7, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=1),
}


class Marks(BaseModel):
    sem1_marks: List[int]
    sem2_marks: List[int]
    sem3_marks: List[int]
    sem4_marks: List[int]
    sem5_marks: List[int]
    sem6_marks: List[int]
    sem7_marks: List[int]
    sem8_marks: List[int]

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
    


def sem1_GPA(sem1_marks):
    marks = sem1_marks
    total_gradepoints = sum(marks_to_gradepoints(mark) for mark in marks)
    gpa = total_gradepoints / len(marks)
    print(f"GPA for Semester 1: {gpa:.2f}")
    return gpa


def sem2_GPA(sem2_marks):
    marks = sem2_marks
    total_gradepoints = sum(marks_to_gradepoints(mark) for mark in marks)
    gpa = total_gradepoints / len(marks)
    print(f"GPA for Semester 2: {gpa:.2f}")
    return gpa


def sem3_GPA(sem3_marks):
    marks = sem3_marks
    total_gradepoints = sum(marks_to_gradepoints(mark) for mark in marks)
    gpa = total_gradepoints / len(marks)
    print(f"GPA for Semester 3: {gpa:.2f}")
    return gpa


def sem4_GPA(sem4_marks):
    marks = sem4_marks
    total_gradepoints = sum(marks_to_gradepoints(mark) for mark in marks)
    gpa = total_gradepoints / len(marks)
    print(f"GPA for Semester 4: {gpa:.2f}")
    return gpa


def sem5_GPA(sem5_marks):
    marks = sem5_marks
    total_gradepoints = sum(marks_to_gradepoints(mark) for mark in marks)
    gpa = total_gradepoints / len(marks)
    print(f"GPA for Semester 5: {gpa:.2f}")
    return gpa


def sem6_GPA(sem6_marks):
    marks = sem6_marks
    total_gradepoints = sum(marks_to_gradepoints(mark) for mark in marks)
    gpa = total_gradepoints / len(marks)
    print(f"GPA for Semester 6: {gpa:.2f}")
    return gpa


def sem7_GPA(sem7_marks):
    marks = sem7_marks
    total_gradepoints = sum(marks_to_gradepoints(mark) for mark in marks)
    gpa = total_gradepoints / len(marks)
    print(f"GPA for Semester 7: {gpa:.2f}")
    return gpa


def sem8_GPA(sem8_marks):
    marks = sem8_marks
    total_gradepoints = sum(marks_to_gradepoints(mark) for mark in marks)
    gpa = total_gradepoints / len(marks)
    print(f"GPA for Semester 8: {gpa:.2f}")
    return gpa

# total_cgpa()
@app.post("/calculate-gpa")
async def final_cgpa(marks: Marks):
    tasks = [
        sem1_GPA(marks.sem1_marks),
        sem2_GPA(marks.sem2_marks),
        sem3_GPA(marks.sem3_marks),
        sem4_GPA(marks.sem4_marks),
        sem5_GPA(marks.sem5_marks),
        sem6_GPA(marks.sem6_marks),
        sem7_GPA(marks.sem7_marks),
        sem8_GPA(marks.sem8_marks)
    ]
    
    # Await all GPA calculations concurrently
    results = await asyncio.gather(*tasks)
    
    # Calculate total CGPA
    total_gpa = sum(results) / 8
    
    return {"CGPA": total_gpa}

# if __name__ == "__main__":
    # import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)        

with DAG('bharat_cgpa', 
         default_args=default_args,
         description='A DAG with calculation of CGPA of 8 Semester',
         schedule=timedelta(days=1),
         catchup=False) as dag:
    
    sem_1_cgpa = PythonOperator(
        task_id = "sem_1_cgpa",
        python_callable = sem1_GPA,
    )
    sem_2_cgpa = PythonOperator(
        task_id = "sem_2_cgpa",
        python_callable = sem1_GPA,
    )
    sem_3_cgpa = PythonOperator(
        task_id = "sem_3_cgpa",
        python_callable = sem1_GPA,
    )
    sem_4_cgpa = PythonOperator(
        task_id = "sem_4_cgpa",
        python_callable = sem1_GPA,
    )
    sem_5_cgpa = PythonOperator(
        task_id = "sem_5_cgpa",
        python_callable = sem1_GPA,
    )
    sem_6_cgpa = PythonOperator(
        task_id = "sem_6_cgpa",
        python_callable = sem1_GPA,
    )
    sem_7_cgpa = PythonOperator(
        task_id = "sem_7_cgpa",
        python_callable = sem1_GPA,
    )
    sem_8_cgpa = PythonOperator(
        task_id = "sem_8_cgpa",
        python_callable = sem1_GPA,
    )
    total_cgpa_marks = PythonOperator(
        task_id = "total_cgpa_marks",
        python_callable = final_cgpa
    )


    [sem_1_cgpa, sem_2_cgpa, sem_3_cgpa ,sem_4_cgpa, sem_5_cgpa, sem_6_cgpa, sem_7_cgpa, sem_8_cgpa] >> total_cgpa_marks


