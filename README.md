# Zoom Transcript Summarizer

A web application built with FastAPI and React. Uses a fine-tuned Google's Gemma-2B-it Large Language Model to summarize Zoom meeting transcripts.

The notebook for fine-tuning Gemma-2B-it model on Google Colab is provided in the /notebook directory. The fine-tuned model is published to Hugging Face @ https://huggingface.co/nguyenanhhuy248/gemma-2b-it-samsum

## Demo video

https://github.com/user-attachments/assets/d458ab34-fe41-4095-9c94-b48d4f06d5b9

## Features

- Responsive UI built with React and Material-UI
- AI-powered summarization using a fine-tuned Gemma-2B model
- Support for VTT transcript files downloaded from Zoom
- Asynchronous processing with FastAPI

## Project Structure

```
zoom-transcript-summarizer/
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── api/            # API endpoints
│   │   ├── llm/           # AI model and inference
│   │   ├── services/      # Business logic
│   │   └── config.py      # Configuration settings
│   └── requirements.txt    # Python dependencies
│
└── frontend/              # React frontend
│   ├── src/
│   │   ├── components/    # Reusable UI components
│   │   ├── pages/         # Page components
│   │   └── services/      # API services
│   └── package.json       # Node.js dependencies
│
└── notebook/              # A notebook for fine-tunning Gemma-2B model by LoRA in Google Colab
```

## Prerequisites

- Python 3.8 or higher
- Node.js 16 or higher
- npm or yarn

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:

   ```bash
   cd backend
   ```

2. Install dependencies:

   ```bash
   poetry install
   ```

3. Create a `.secrets.toml` file in `app/config` with your HuggingFace token:

```toml
# .secrets.toml
HUGGINGFACE_TOKEN = "your_token_here"
```

### Frontend Setup

1. Navigate to the frontend directory:

   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   # or
   yarn install
   ```

## Running the Application

1. Start the backend server:

   ```bash
   cd backend
   uvicorn app.main:app --reload
   ```

2. In a new terminal, start the frontend development server:

   ```bash
   cd frontend
   npm start
   # or
   yarn start
   ```

3. Open your browser and visit `http://localhost:3000`

## Usage

1. Open the application in your browser
2. Drag and drop a Zoom VTT transcript file or click to select one
3. Click the "Upload" button
4. Wait for the AI to process and generate the summary
5. View the generated summary in the text box
6. Use the "Copy to Clipboard" button to copy the summary

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
