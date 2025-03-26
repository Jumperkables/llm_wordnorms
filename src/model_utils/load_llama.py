__author__ = "Jumperkables"

# local imports

# 3rd party imports
from peft import LoraConfig, get_peft_model
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

# local imports
from src.config import LLAMA_CONVERTED_PATH

def load_llama_peft_quantised():
    """
    Load HuggingFace tokeniser and model for the Llama in 4-bit and quantised form
    """
    # Model, PEFT, and quantisation
    quantization_config = BitsAndBytesConfig(load_in_4bit=True)
    model = AutoModelForCausalLM.from_pretrained(
        LLAMA_CONVERTED_PATH,
        quantization_config=quantization_config,
        torch_dtype=torch.float16,
    )
    peft_config = LoraConfig(
        r=8, lora_alpha=16, target_modules=["q_proj", "v_proj"],
        lora_dropout=0.1, bias="none", task_type="CAUSAL_LM"
    )
    model = get_peft_model(model, peft_config)

    # Tokeniser
    tokenizer = AutoTokenizer.from_pretrained(LLAMA_CONVERTED_PATH)
    tokenizer.pad_token = tokenizer.eos_token

    return model, tokenizer

