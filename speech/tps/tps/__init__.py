import nltk
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

import os
import sys
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root_path)

from tps.handler import Handler, get_symbols_length
from tps.utils import cleaners, load_dict, save_dict, prob2bool, split_to_tokens
from tps.modules import ssml

sys.path.pop(0)