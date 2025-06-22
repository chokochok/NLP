from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

device = torch.device("cpu")
tokenizer = T5Tokenizer.from_pretrained("stanfordnlp/SteamSHP-flan-t5-large", legacy=True)
model = T5ForConditionalGeneration.from_pretrained("stanfordnlp/SteamSHP-flan-t5-large").to(device) # type: ignore
model.eval()

def create_input(prompt, response_a, response_b):
    return (
        f"POST: {prompt.strip()}\n\n"
        f"RESPONSE A: {response_a.strip()}\n\n"
        f"RESPONSE B: {response_b.strip()}\n\n"
        f"Which response is better? RESPONSE"
    )

def predict_answer(prompt, response_a, response_b):
    input_text = create_input(prompt, response_a, response_b)
    input_ids = tokenizer([input_text], return_tensors="pt", truncation=True, max_length=512).input_ids.to(device)
    with torch.no_grad():
        outputs = model.generate(input_ids, max_new_tokens=1)
    prediction = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return prediction.strip()

if __name__ == "__main__":
    prompt = "What is the capital of France?"
    response_a = "The capital of France is Paris."
    response_b = "France's capital is Paris."
    
    prediction = predict_answer(prompt, response_a, response_b)
    print(f"Prompt: {prompt}")
    print(f"Prediction: {prediction}\n")

    prompt = "What is the largest planet in our solar system?"
    response_a = "The largest planet in our solar system is Mars."
    response_b = "The largest planet in our solar system is Jupiter."

    prediction = predict_answer(prompt, response_a, response_b)
    print(f"Prompt: {prompt}")
    print(f"Prediction: {prediction}\n")
