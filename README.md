# Diakriticar

Diakriticar is a web application that automatically adds Croatian diacritics to text using the Ollama API with a Mistral model.

## Overview

This application consists of:

- **Python Backend**: FastAPI server that communicates with Ollama's Mistral model
- **TypeScript/React Frontend**: Simple UI for text input and displaying corrected text

## Architecture

### Backend
- **Technology**: Python with FastAPI
- **Package Manager**: uv
- **Features**:
  - REST API endpoint for text processing
  - Integration with Ollama API
  - Error handling for API calls

### Frontend
- **Technology**: TypeScript and React
- **Package Manager**: Bun
- **Features**:
  - Text input area
  - Submit button
  - Result display area
  - Loading state handling
  - Error messaging

## Requirements

- Python 3.8+
- Node.js and Bun
- Ollama installed with Mistral model

## Getting Started

### Setting up the Backend

```bash
# Navigate to backend directory
cd backend

# Create and activate a virtual environment with uv
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv pip install -r requirements.txt

# Start the server
python main.py
```

### Setting up the Frontend

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
bun install

# Start the development server
bun start
```

### Running Ollama

```bash
# Pull the Mistral model (run once)
ollama pull mistral

# Start Ollama (if not running as a service)
ollama serve
```

## Usage

1. Enter Croatian text without diacritics in the input field
2. Click the "Add Diacritics" button
3. View the corrected text with proper diacritics in the output area

## Future Improvements

- Enhanced error handling
- Unit tests for both backend and frontend
- Improved prompt engineering
- Batch processing capability
- History of processed texts