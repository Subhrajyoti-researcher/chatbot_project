import torch
from models.load_model import load_llm_model

tokenizer, model = load_llm_model()

def generate_response(prompt):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(
        inputs,
        max_length=150,
        do_sample=True,
        top_p=0.95,
        top_k=50,
        temperature=0.9
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response.strip()
