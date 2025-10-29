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
