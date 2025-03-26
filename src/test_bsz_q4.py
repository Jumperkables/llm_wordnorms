__author__ = "Jumperkables"
__generatedBy__ = "ChatGPT"
"""
I asked ChatGPT to generate a minimal dummy training scenario
"""

# standard imports
from argparse import ArgumentParser

# third party imports
from datasets import load_dataset
from peft import LoraConfig, get_peft_model
import torch
from transformers import AutoModelForCausalLM, BitsAndBytesConfig, AutoTokenizer, TrainingArguments, Trainer


# local imports
from src.config import LLAMA_CONVERTED_PATH, RESULTS_PATH
from src.model_utils.load_llama import load_llama_peft_quantised


def tokenize_function(examples):
    # Tokenize input
    tokens = tokenizer(
        examples["quote"], padding="max_length", truncation=True, max_length=128
    )

    # Labels are simply the input tokens (shifted during training)
    tokens["labels"] = tokens["input_ids"].copy()
    
    return tokens



if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--BSZ", type=int, required=True)
    args = parser.parse_args()

    # Model and tokeniser
    model, tokeniser = load_llama_peft_quantised()

    # Load dummy dataset (tiny sample)
    dataset = load_dataset("Abirate/english_quotes", split="train[:5%]")  # Use only 1% of data
    dataset = dataset.map(tokenize_function, batched=True)

    # Set up training arguments (minimal setup)
    training_args = TrainingArguments(
        output_dir=RESULTS_PATH,
        per_device_train_batch_size=args.BSZ,  # Adjust batch size here
        num_train_epochs=1,
        save_steps=10,
        logging_steps=5,
        fp16=True
    )

    # Trainer setup
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset
    )

    # Train for a few steps to check VRAM
    trainer.train()