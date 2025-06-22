# 🧠 SteamSHP Project: Preference Modeling via FastAPI + Airflow ETL

![Kaggle Screenshot](assets/kaggle_submission.png)

## 🔍 Overview

This project implements an end-to-end pipeline to evaluate human preference between two text completions using a small language model. It includes:

- **FastAPI**: API to run inference and store input samples.
- **Airflow**: ETL pipeline to fetch unprocessed records and write model predictions.
- **PostgreSQL**: Stores input prompts and model responses.
- **Docker Compose**: Full orchestration.

## 📁 Structure

```
steamshp_project/
├── api/                   # FastAPI app (model + endpoints)
│   ├── main.py            # FastAPI endpoints for /predict and /upload
│   ├── model.py           # Scoring model based on a pretrained LLM
│   ├── requirements.txt   # Python dependencies
│   └── Dockerfile         # FastAPI service container
├── airflow_dags/
│   └── llm_etl_dag.py     # Airflow DAG to process and score input_data
├── upload_shp_to_db.py    # Script to upload SHP dataset samples to DB
├── predict_shp_to_api.py  # (optional) Send SHP samples directly to /predict
├── docker-compose.yml     # Orchestration of all services
├── init.sql               # PostgreSQL DB schema for input/predicted data
└── README.md              # You're here!
```

## 🚀 Quickstart

### 1. Install Docker & Docker Compose

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install docker.io docker-compose -y
sudo usermod -aG docker $USER
newgrp docker
```

### 2. Initialize the Database

```bash
docker-compose run airflow-webserver airflow db init
```

### 3. Start Services

```bash
docker-compose up --build -d
```

- FastAPI: [http://localhost:8000/docs](http://localhost:8000/docs)
- Airflow: [http://localhost:8080](http://localhost:8080)
- PostgreSQL: port `5432`

## 🧩 API Endpoints

### `POST /upload`

Batch upload SHP-style entries to the `input_data` table.

**Payload:**
```json
[
  {
    "prompt": "Why do cats purr?",
    "response_a": "They are content.",
    "response_b": "To manipulate humans."
  }
]
```

### `POST /predict`

Model returns which response is better.

**Payload:**
```json
{
  "prompt": "...",
  "response_a": "...",
  "response_b": "..."
}
```

**Response:**
```json
{"preferred": "A"}
```

## 🧠 Model

Model loaded in `model.py` is a lightweight pairwise scoring function using HuggingFace + `T5Tokenizer`.

> 🔍 Requires `sentencepiece`, `torch`, `transformers`.

## 📥 Load SHP Samples

Use this script to send SHP dataset samples:

```bash
python upload_shp_to_db.py
```

It uses the `datasets` library and sends a batch to FastAPI.

## 📅 DAG: Airflow ETL

Airflow DAG (`llm_etl_dag.py`) runs periodically:

- Pulls new `input_data` entries
- Calls `/predict`
- Stores result in `predicted_data`

---

_Лабораторна робота виконана у межах курсу з обробки природної мови._