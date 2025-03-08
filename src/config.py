__author__ = "Jumperkables"

# standard imports
import os

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODELS_PATH = os.path.join(ROOT_PATH, "models")
DATA_PATH = os.path.join(ROOT_PATH, "data")
RESULTS_PATH = os.path.join(ROOT_PATH, "results")

WORD_NORM_PATH = os.path.join(DATA_PATH, "all_norms.pickle")
LLAMA_CONVERTED_PATH = os.path.join(MODELS_PATH, "Llama3.2-1B_CONVERTED")