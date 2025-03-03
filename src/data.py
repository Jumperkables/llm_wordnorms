# standard imports
import pickle

# third-party imports
from loguru import logger

# local imports
from src.config import WORD_NORM_PATH
from src.data_utils.word_norms import Word2Norm

if __name__ == "__main__":
    word_norms = pickle.load(open(WORD_NORM_PATH, "rb"))
    
    breakpoint()