# Meeting Transcript Summarizer

This project provides a Python script to summarize meeting transcripts from VVT files using a model from Hugging Face.

## Project Structure

```
llm
├── inference.py
└── README.md
```

## Requirements

- Python 3.7 or higher
- `transformers` library
- `torch` library
- `webvtt-py` library
- `huggingface_hub` library

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd llm
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install transformers torch webvtt-py huggingface_hub
   ```

4. **Set up Hugging Face token:**
   - Create a `config.py` file in the `llm` directory and add your Hugging Face token:
     ```python
     settings = {
         "HUGGINGFACE_TOKEN": "your_token_here"
     }
     ```

## Running the Script

To run the script and summarize a meeting transcript, execute the following command:

```bash
python inference.py
```

Make sure to place your VVT file in the appropriate directory as specified in the script.

## License

This project is licensed under the MIT License.