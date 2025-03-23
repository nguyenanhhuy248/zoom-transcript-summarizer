"""Service for handling transcript processing and summarization."""
from __future__ import annotations

import os
import tempfile

from app.config.config import settings
from app.llm.inference import split_transcript
from app.llm.inference import summarize
from fastapi import UploadFile


class TranscriptService:  # pylint: disable=too-few-public-methods
    """Service for handling transcript processing and summarization."""

    def __init__(self, tokenizer, model):
        self.tokenizer = tokenizer
        self.model = model

    async def _save_to_temp_file(self, file: UploadFile) -> str:
        """Save contents to a temporary VTT file and return the path."""
        with tempfile.NamedTemporaryFile(suffix='.vtt', delete=False) as temp_file:
            contents = await file.read()
            temp_file.write(contents)
            return temp_file.name

    async def process_transcript(self, file_content: UploadFile) -> str:
        """
        Process and summarize a transcript file.

        Args:
            file_content: The uploaded transcript file content as bytes

        Returns:
            str: The summarized text

        Raises:
            Exception: If there's an error processing the file
        """
        temp_file_path = await self._save_to_temp_file(file_content)

        try:
            # Split transcript into groups and summarize
            groups = await split_transcript(
                file=temp_file_path,
                tokenizer=self.tokenizer,
                token_limit=settings.max_token_limit,
            )
            summary = await summarize(
                model=self.model,
                tokenizer=self.tokenizer,
                input_str='\n'.join(groups),
            )
            return summary
        finally:
            # Clean up temporary file
            if os.path.exists(temp_file_path):
                os.unlink(temp_file_path)
