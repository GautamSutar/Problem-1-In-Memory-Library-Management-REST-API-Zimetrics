from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()

book_db = {}
class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int

@app.post("/add-books"):
def add_books(book: Book):
    if book.id in book_db:
        raise HTTPException(status_code=400, detail="Book with this ID already exists.")
    book_db[book.id] = book
    return {"message": "Book added successfully."}


