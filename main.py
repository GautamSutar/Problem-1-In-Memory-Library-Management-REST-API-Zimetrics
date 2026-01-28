from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()

book_db = {}
class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int


# Home Route
@app.get("/")
def home():
    return {"message": "In-Memory Library API Running"}

@app.post("/add-books")
def add_books(book: Book):
    if book.id in book_db:
        raise HTTPException(status_code=400, detail="Book with this ID already exists.")
    book_db[book.id] = book
    return {"message": "Book added successfully."}

@app.get("/books")
def get_all_books():
    return list(book_db.values())


@app.get("/books/search")
def search_books(year: int):
    results = []
    for book in book_db.values():
        if book.year == year:
            results.append(book)
    return results


@app.get("/book/{id}")
def get_book_by_id(id: int):
    if id not in book_db:
        raise HTTPException(status_code=404, detail="Book not found.")
    return book_db[id]


@app.delete("/book/{id}")
def delete_book(id: int):
    if id not in book_db:
        raise HTTPException(status_code=404, detail="Book not found.")
    del book_db[id]
    return {"message": "Book deleted successfully."}
