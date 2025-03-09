from pydantic import BaseModel, Field


class ResponseModel(BaseModel):
    """A class inheriting from Pydantic's BaseModel class to validate the responses from Large Language Models"""
    output: str = Field(
        ...,
        title = "LLM's output string",
        description = "The output string from the Large Language Model"
    )
    timestamp: str = Field(
        ...,
        title = "UNIX timestamp",
        description = "The UNIX timestamp of the response"
    )
    time_taken: str = Field(
        ...,
        title = "Time taken",
        description = "Time in seconds the LLM takes to generate the response"
    )
    