from airflow import DAG
from airflow.operators.python import PythonOperator  # type: ignore
from datetime import datetime
import psycopg2
import requests

def run_etl():
    conn = psycopg2.connect(
        dbname="steam_db",
        user="airflow",
        password="airflow",
        host="postgres",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT id, prompt, response_a, response_b FROM input_data WHERE id NOT IN (SELECT id FROM predicted_data)")
    rows = cur.fetchall()

    for row in rows:
        payload = {
            "prompt": row[1],
            "response_a": row[2],
            "response_b": row[3]
        }
        response = requests.post("http://api:8000/predict", json=payload)
        response.raise_for_status()
        preferred = response.json()["preferred"]
        cur.execute("INSERT INTO predicted_data (id, preferred) VALUES (%s, %s)", (row[0], preferred))
        conn.commit()

    cur.close()
    conn.close()

default_args = {
    'start_date': datetime(2024, 1, 1)
}

dag = DAG(
    dag_id="llm_etl_dag",
    description="Run ETL with model",
    schedule="*/10 * * * *",
    default_args=default_args,
    catchup=False,
    tags=["llm"]
)

etl_task = PythonOperator(
    task_id="run_llm_etl",
    python_callable=run_etl,
    dag=dag
)
