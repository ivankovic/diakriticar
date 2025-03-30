from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import httpx
import os

app = FastAPI(title="Diakriticar API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TextRequest(BaseModel):
    text: str


class TextResponse(BaseModel):
    processed_text: str


OLLAMA_API_URL = os.environ.get(
    "OLLAMA_API_URL", "http://localhost:11434/api/generate")
MODEL_NAME = os.environ.get("MODEL_NAME", "mistral")


@app.post("/api/process", response_model=TextResponse)
async def process_text(request: TextRequest):
    if not request.text:
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    # Prepare prompt for the model
    prompt = f"""
    Add correct Croatian diacritics to the following text. 
    Only return the corrected text, with no additional explanations.
    
    Text: {request.text}
    
    Corrected text:
    """

    # Call Ollama API
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                OLLAMA_API_URL,
                json={
                    "model": MODEL_NAME,
                    "prompt": prompt,
                    "stream": False
                }
            )
            response.raise_for_status()
            result = response.json()

            # Extract the generated text
            processed_text = result.get("response", "").strip()

            return TextResponse(processed_text=processed_text)
    except httpx.HTTPError as e:
        raise HTTPException(
            status_code=500, detail=f"Error calling Ollama API: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
