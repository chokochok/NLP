from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from model import predict_answer
import psycopg2

app = FastAPI()

DB_CONFIG = {
    "dbname": "steam_db",
    "user": "airflow",
    "password": "airflow",
    "host": "postgres",
    "port": "5432"
}

class RequestData(BaseModel):
    prompt: str
    response_a: str
    response_b: str

@app.post("/predict")
def predict(data: RequestData):
    result = predict_answer(data.prompt, data.response_a, data.response_b)
    return {"preferred": result}

@app.post("/upload")
def upload_batch(batch: List[RequestData]):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        inserted_count = 0
        for item in batch:
            cur.execute("""
                SELECT 1 FROM input_data
                WHERE prompt = %s AND response_a = %s AND response_b = %s
                LIMIT 1
            """, (item.prompt, item.response_a, item.response_b))

            if not cur.fetchone():
                cur.execute("""
                    INSERT INTO input_data (prompt, response_a, response_b)
                    VALUES (%s, %s, %s)
                """, (item.prompt, item.response_a, item.response_b))
                inserted_count += 1

        conn.commit()
        cur.close()
        conn.close()
        return {"status": "success", "inserted": inserted_count}

    except Exception as e:
        return {"status": "error", "detail": str(e)}
