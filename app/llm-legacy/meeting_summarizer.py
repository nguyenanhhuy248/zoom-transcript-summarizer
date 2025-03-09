from transformers import AutoTokenizer, AutoModelForSeq2SeqGeneration
import torch
import os

def load_model_and_tokenizer():
    """Load the model and tokenizer from Hugging Face"""
    model_name = "facebook/bart-large-cnn"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqGeneration.from_pretrained(model_name)
    return model, tokenizer

def read_transcript(file_path):
    """Read the VVT transcript file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        transcript = f.read()
    return transcript

def generate_summary(model, tokenizer, transcript, max_length=130, min_length=30):
    """Generate summary using the model"""
    # Prepare the input
    inputs = tokenizer.encode("summarize: " + transcript, 
                            return_tensors="pt",
                            max_length=1024,
                            truncation=True)

    # Generate summary
    summary_ids = model.generate(inputs,
                               max_length=max_length,
                               min_length=min_length,
                               length_penalty=2.0,
                               num_beams=4,
                               early_stopping=True)
    
    # Decode and return the summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

def main():
    # File path
    transcript_file = "path_to_your_transcript.vtt"
    
    # Load model and tokenizer
    print("Loading model and tokenizer...")
    model, tokenizer = load_model_and_tokenizer()
    
    # Read transcript
    print("Reading transcript...")
    transcript = read_transcript(transcript_file)
    
    # Generate summary
    print("Generating summary...")
    summary = generate_summary(model, tokenizer, transcript)
    
    # Print results
    print("\nSummary:")
    print(summary)

if __name__ == "__main__":
    main()