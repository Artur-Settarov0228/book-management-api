from pydantic import BaseModel,Field
from enum import Enum
from typing import Annotated



class BookOut(BaseModel):
    id : int
    title : str
    auther : str
    year : int
    genre : str
    rating : float
    
    class Config:
        from_attributes = True

class BookCreate(BaseModel):
    title:str = Field(min_length=3)
    author : str = Field(min_length=3)
    genre :Genre
    year :int = Field(ge = 1)
    rating :float = Field(ge=0,le=5)

class BookUpdate(BaseModel):
    title:Annotated[str|None,Field(min_length=3)] = None
    author : Annotated[str|None,Field(min_length=3)] = None
    genre :Genre | None = None
    year :Annotated[int|None,Field(ge = 1)] = None
    rating :Annotated[float|None,Field(ge=0,le=5)] = None