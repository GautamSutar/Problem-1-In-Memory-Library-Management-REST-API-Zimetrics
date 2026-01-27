from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

book_db = {}
class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int