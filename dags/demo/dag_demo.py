from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'Gulu Mammadli',
    'depends_on_past': False,
    'email': ['gulu.mammadli@heyjobs.de'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}

with DAG(
    dag_id="demo",
    default_args=default_args,
    description="A simple demo DAG",
    schedule_interval=timedelta(days=1),
    start_date=datetime(2021, 11, 24, 13, 0, 0),
    catchup=False,
    tags=['example']
) as dag:
    print_date = BashOperator(
        task_id='print_date',
        bash_command='date'
    )

    print_date_airflow_template = BashOperator(
        task_id='print_date_airflow_template',
        bash_command='echo {{ params.param }}',
        params={'param': 'ds'}
    )

    print_date >> print_date_airflow_template