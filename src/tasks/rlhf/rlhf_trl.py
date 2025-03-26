__author__ = "Jumperkables"

# standard imports
import argparse

# third party imports
import torch
from trl import AutoModelForCausalLMWithValueHead, PPOConfig, PPOTrainer

# local imports
from src.model_utils.load_llama import load_llama_peft_quantised

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--bsz", type=int, default=4)
    args = parser.parse_args()

    # Model and Tokeniser loading
    model, tokeniser = load_llama_peft_quantised()

    # demo here: https://huggingface.co/docs/trl/en/quickstart
    ppo_config = {
        "mini_batch_size": 1,
        "batch_size": 1,
    }