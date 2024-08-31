'''from transformers import AutoModelForCausalLM, AutoTokenizer

def load_llm_model():
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    model = AutoModelForCausalLM.from_pretrained("gpt2")
    return tokenizer, model'''


from transformers import LlamaForCausalLM, LlamaTokenizer

def load_llm_model():
    tokenizer = LlamaTokenizer.from_pretrained("huggyllama/llama-7b")
    model = LlamaForCausalLM.from_pretrained("huggyllama/llama-7b")
    return tokenizer, model

