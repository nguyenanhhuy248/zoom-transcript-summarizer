import logging
import os
from enum import Enum
import torch
from transformers import AutoTokenizer
from langchain.prompts import PromptTemplate
from pydantic import BaseModel, Field, model_validator
from config import settings


class ModelID(Enum):
    llama2_13b = "meta-llama/Llama-2-13b-hf"
    falcon_7b = "tiiuae/falcon-7b-instruct"

class TorchDtype(Enum):
    float16 = torch.float16
    float32 = torch.float32

class Quantization(Enum):
    four_bit = "4-bit"
    eight_bit = "8-bit"
    none = "None"


