from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import webvtt

# Function to get the appropriate torch dtype based on available hardware
def get_torch_dtype():
    """
    Determine the appropriate torch dtype based on available hardware.

    If a GPU or MPS supported Mac device is available, use float16 for faster computation.
    Otherwise, use float32.
    """
    if torch.cuda.is_available() or torch.backends.mps.is_built():
        return torch.bfloat16  # Use float16 for GPU or MPS supported Mac devices
    return torch.float32

# Function to get the appropriate torch device based on available hardware
def get_torch_device():
    """
    Determine the appropriate torch device based on available hardware.

    If a GPU is available, use the GPU. If an MPS supported Mac device is available, use the MPS device.
    Otherwise, use the CPU.
    """
    if torch.cuda.is_available():
        return torch.device("cuda")
    elif torch.backends.mps.is_built():
        return torch.device("mps")
    else:
        return torch.device("cpu")

# Load the tokenizer and model from Hugging Face
async def load_model(model_name):
    """
    Load the tokenizer and model from Hugging Face.

    Parameters:
    - model_name (str): The name of the model to load from Hugging Face.

    Returns:
    - tokenizer (AutoTokenizer): The loaded tokenizer.
    - model (AutoModelForCausalLM): The loaded model.
    """
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    loaded_model = AutoModelForCausalLM.from_pretrained(
        model_name,
        low_cpu_mem_usage=True,
        return_dict=True,
        torch_dtype=get_torch_dtype(),
        device_map="auto",
    )
    return tokenizer, loaded_model

# Function to summarize the meeting transcript
async def summarize(model, tokenizer, input):
    """
    Summarize the given meeting transcript.

    Parameters:
    - model (AutoModelForCausalLM): The model to use for summarization.
    - tokenizer (AutoTokenizer): The tokenizer to use for tokenizing the input.
    - input (str): The meeting transcript to summarize.

    Returns:
    - str: The summarized meeting transcript.
    """
    prompt_template = """
        From the meeting transcript below, create a meeting summary.
        The summary should be no longer than half of the original transcript and 
        should retain all the important information such as facts, details, problems, questions, and actions needed.
        Meeting transcript:
        {}
    """
    prompt = prompt_template.format(input)
    chat = [
        {"role": "user", "content": prompt},
        {"role": "model", "content": """Summary: """},
    ]
    token_inputs = tokenizer.apply_chat_template(
        chat, tokenize=True, return_tensors="pt", add_generation_prompt=True
    )
    token_inputs = token_inputs.to(get_torch_device())
    inputs = {
        "input_ids": token_inputs,
        "max_length": 8196,
        "do_sample": True,
        "temperature": 0.001,
    }

    token_outputs = model.generate(**inputs).to(get_torch_device())
    new_tokens = token_outputs[0][token_inputs.shape[-1]:]

    return tokenizer.decode(new_tokens, skip_special_tokens=True)

# Function to remove message numbers from the transcript
async def remove_message_number(message: str) -> str:
    """
    Remove message numbers from the transcript.

    Given a string representing a meeting transcript, this function removes all lines
    that can be converted to an integer (i.e. message numbers) and returns the new string.
    """
    message_lines = message.split("\n")
    new_message = ""
    for line in message_lines:
        try:
            int(line)
        except ValueError:
            new_message += line + "\n"
    return new_message

# Function to split the transcript into manageable groups
async def split_transcript(file: str, tokenizer, token_limit: int) -> list:
    """
    Split the transcript into groups of messages that are within a specified token limit.

    This function reads a VTT file and processes each caption to remove message numbers.
    It accumulates messages into groups, ensuring that each group's total token count
    does not exceed the specified token limit. If adding a message exceeds the limit,
    a new group is started. The final list of message groups is returned.

    Parameters:
    - file (str): Path to the VTT file containing the transcript.
    - token_limit (int): The maximum number of tokens allowed in each message group.

    Returns:
    - list: A list of message groups, where each group is a string of concatenated messages.
    """

    message_groups = []
    token_counter = 0
    current_message_group = ""
    for caption in webvtt.read(file):
        message = await remove_message_number(caption.text)
        token_counter += len(tokenizer.encode(message))
        if token_counter < token_limit:
            current_message_group += message
        else:
            message_groups.append(current_message_group)
            current_message_group = message
            token_counter = len(tokenizer.encode(message))
    message_groups.append(current_message_group)
    return message_groups