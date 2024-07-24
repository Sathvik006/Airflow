from airflow import DAG
from airflow.operators.bash import BashOperator 
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'run_bash_python_operators',
    default_args=default_args,
    description='Run a Bash script followed by a Python script',
    schedule=None, 
    start_date=datetime.today(), 
    catchup=False
)

# Define tasks
bash_task = BashOperator(
    task_id='run_bash_script',
    bash_command='./basic_bash.sh',
    dag=dag,
)

def python_function():
    print("Hello, World!")
    print(f"Current date and time: {datetime.now()}")
    pass

python_task = PythonOperator(
    task_id='run_python_script',
    python_callable=python_function,
    dag=dag,
)

# Define the task dependencies
bash_task >> python_task
