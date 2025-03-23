"""Summarizer API endpoints."""
from __future__ import annotations

from app.config.config import settings
from app.services.transcript import TranscriptService
from fastapi import APIRouter
from fastapi import Depends
from fastapi import File
from fastapi import HTTPException
from fastapi import Request
from fastapi import UploadFile
from fastapi.responses import JSONResponse

router = APIRouter()


def get_tokenizer_and_model(request: Request):
    """Get the tokenizer and model from the application state."""
    return request.app.state.tokenizer, request.app.state.model


@router.post('/summarize', response_model=dict)
async def summarize_meeting(
    file: UploadFile = File(...),
    models=Depends(get_tokenizer_and_model),
):
    """
    Summarize a meeting transcript.

    Args:
        file: The VTT file containing the meeting transcript
        models: Tuple of (tokenizer, model) from dependencies

    Returns:
        JSONResponse with the summary

    Raises:
        HTTPException: For invalid file types or processing errors
    """
    tokenizer, model = models

    # Validate file extension
    if not any(
        file.filename.lower().endswith(ext)
        for ext in settings.allowed_extensions
    ):
        raise HTTPException(
            status_code=400,
            detail=f"Invalid file type. Please upload one of: {
                ', '.join(settings.allowed_extensions)
            }",
        )

    try:
        transcript_service = TranscriptService(
            tokenizer=tokenizer, model=model,
        )
        summary = await transcript_service.process_transcript(file)
        return JSONResponse(content={'summary': summary})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
