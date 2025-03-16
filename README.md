# Zoom Transcript Summarizer

A web application that uses AI model to generate summaries of Zoom meeting transcripts. Built with FastAPI, React, and used a fine-tuned Gemma-2B model.

## Features

- 🚀 Responsive UI built with React and Material-UI
- 🤖 AI-powered summarization using a fine-tuned Gemma-2B model
- 📝 Support for VTT transcript files downloaded from Zoom
- ⚡ Asynchronous processing with FastAPI
- 🎨 Intuitive interface with drag-and-drop file upload
- 📋 Easy copy-to-clipboard functionality

## Demo video

https://github.com/user-attachments/assets/3d195ab1-62ea-468e-b18b-62252ff1f1c5


## Project Structure

```
zoom-transcript-summariser/
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
└── notebook/              # A notebook for fine-tunning Gemma-2B model in Google Colab
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
