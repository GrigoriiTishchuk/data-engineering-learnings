from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(dag_id='espoo_analysis_pipeline', start_date=datetime(2024, 1, 1), schedule_interval="@once", catchup=False,description='Espoo notebook analysis is running', ) as dag:
    run_pipeline = BashOperator(
        task_id="run_bq_load",
        bash_command="poetry run python scripts/run_notebook.py"
    )

    run_pipeline