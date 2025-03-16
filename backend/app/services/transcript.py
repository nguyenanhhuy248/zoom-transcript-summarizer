import tempfile
import os
from fastapi import UploadFile
from app.llm.inference import summarize, split_transcript
from app.config import settings


class TranscriptService:
    """Service for handling transcript processing and summarization."""

    def __init__(self, tokenizer, model):
        self.tokenizer = tokenizer
        self.model = model

    async def process_transcript(self, file: UploadFile) -> str:
        """
        Process and summarize a transcript file.

        Args:
            file: The uploaded transcript file

        Returns:
            str: The summarized text

        Raises:
            Exception: If there's an error processing the file
        """
        # Create a temporary file with .vtt extension
        with tempfile.NamedTemporaryFile(suffix='.vtt', delete=False) as temp_file:
            contents = await file.read()
            temp_file.write(contents)
            temp_file_path = temp_file.name

        try:
            # Split transcript into groups and summarize
            groups = await split_transcript(
                file=temp_file_path,
                tokenizer=self.tokenizer,
                token_limit=settings.max_token_limit
            )
            summary = await summarize(
                model=self.model,
                tokenizer=self.tokenizer,
                input=groups
            )
            return summary
        finally:
            # Clean up temporary file
            if os.path.exists(temp_file_path):
                os.unlink(temp_file_path) 