# Zoom Transcript Summarizer Frontend

A modern React application that provides a user-friendly interface for summarizing Zoom meeting transcripts using AI.

## Features

- Responsive UI with Material-UI components
- Drag-and-drop file upload support for VTT files
- Real-time transcript summarization
- Copy-to-clipboard functionality
- Loading states and error handling
- Modern gradient design with smooth animations

## Tech Stack

- React 18 with TypeScript
- Vite for fast development and building
- Material-UI (MUI) for components and styling
- Axios for API communication

## Getting Started

1. Install dependencies:
```bash
npm install
```

2. Start the development server:
```bash
npm run dev
```

The application will be available at `http://localhost:5173`

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run lint` - Run ESLint
- `npm run preview` - Preview production build

## Project Structure

```
src/
├── components/        # Reusable UI components
├── pages/            # Page components
├── services/         # API services
├── styles/           # Global styles and theme
└── types/           # TypeScript type definitions
```

## Environment Setup

Make sure the backend server is running at `http://localhost:8000` before starting the frontend application.
