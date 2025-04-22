# src/generator.py

from transformers import AutoModelForCausalLM, AutoTokenizer

def generate_answer(context, question, model_name="distilgpt2"):
    # Initialize the tokenizer and generator model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    generator = AutoModelForCausalLM.from_pretrained(model_name)

    # Instruction-focused input prompt
    input_text = f"Context: {context}\n\nQuestion: {question}\nProvide a concise, direct answer:"
    inputs = tokenizer(input_text, return_tensors="pt", max_length=300, truncation=True)
    outputs = generator.generate(**inputs, max_new_tokens=30, num_beams=5, early_stopping=True)

    return tokenizer.decode(outputs[0], skip_special_tokens=True)
