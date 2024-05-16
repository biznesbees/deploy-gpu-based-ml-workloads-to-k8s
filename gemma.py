from fastapi import FastAPI
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import os

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

app = FastAPI()

tokenizer = AutoTokenizer.from_pretrained(
    "google/gemma-2b",
    token=ACCESS_TOKEN,
    )

model = AutoModelForCausalLM.from_pretrained(
    "google/gemma-2b",
    torch_dtype=torch.bfloat16,
    device_map="auto",
    token=ACCESS_TOKEN
)


@app.post("/generate/")
async def generate_text(data: dict):
    input_text = data.get("input_text")
    input_ids = tokenizer(input_text, return_tensors="pt").to("cuda")
    outputs = model.generate(**input_ids)
    generated_text = tokenizer.decode(outputs[0])
    return {"generated_text": generated_text}
