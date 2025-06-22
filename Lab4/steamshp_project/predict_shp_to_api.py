import requests
from datasets import load_dataset

dataset = load_dataset("stanfordnlp/SHP", split="train[:10]")

for example in dataset:
    prompt = example["history"]
    response_0 = example["human_ref_A"]
    response_1 = example["human_ref_B"]

    response = requests.post(
        "http://34.132.237.161:8000/predict",
        json={"prompt": prompt, "response_a": response_0, "response_b": response_1}
    )
    print("Response status:", response.status_code)
    print("Response body:", response.json())
