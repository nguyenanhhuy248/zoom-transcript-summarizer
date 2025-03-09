from fastapi import APIRouter, File, UploadFile, HTTPException, Request, Depends
from fastapi.responses import JSONResponse
from app.llm.inference import summarize, split_transcript

router = APIRouter()

def get_tokenizer_and_model(request: Request):
    return request.app.state.tokenizer, request.app.state.model

@router.post("/summarize")
async def summarize_meeting(file: UploadFile = File(...), models=Depends(get_tokenizer_and_model)):
    """
    Endpoint to summarize a meeting transcript.

    This endpoint accepts a VTT file containing a meeting transcript,
    processes the transcript using a language model, and returns a
    summarized version of the meeting.

    Args:
        file (UploadFile): The VTT file containing the meeting transcript.

    Returns:
        JSONResponse: A JSON response containing the summarized meeting
        text or an error message if the operation fails.

    Raises:
        HTTPException: If the uploaded file is not a VTT file or if there
        is an error during processing.
    """

    tokenizer, model = models

    if file.content_type != "text/vtt":
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a .vtt file.")

    contents = await file.read()
    with open("tmp/temp.vtt", "wb") as temp_file:
        temp_file.write(contents)

    try:
        groups = await split_transcript(file="temp.vtt", tokenizer=tokenizer, token_limit=8192)
        summary = await summarize(model=model, tokenizer=tokenizer, input=groups)
        return JSONResponse(content={"summary": summary})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e