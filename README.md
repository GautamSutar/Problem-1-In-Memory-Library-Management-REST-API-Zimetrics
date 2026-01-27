# 📚 In-Memory Library Management REST API

## Project Title & Goal

A REST API built with FastAPI that manages a library's book inventory using in-memory data storage.

## ✅ STEP 1 — Create GitHub Repository

Open https://github.com

Click New Repository

Repository Name:
```
Problem-1-In-Memory-Library-Management-REST-API-Zimetrics
```

Keep Public

Click Create Repository

## ✅ STEP 2 — Copy Repo URL

Click Code → HTTPS → Copy

Example:
```
https://github.com/GautamSutar/Problem-1-In-Memory-Library-Management-REST-API-Zimetrics.git
```

## ✅ STEP 3 — Clone Repository (On Your PC)

Open terminal:
```
git clone https://github.com/GautamSutar/Problem-1-In-Memory-Library-Management-REST-API-Zimetrics.git

cd Problem-1-In-Memory-Library-Management-REST-API-Zimetrics
```


## ✅ Step 4. Create requirements.txt file
fastapi
uvicorn

## ✅ Step 5. Create Virtual Environment (Optional but Recommended)

```
python -m venv venv
venv\Scripts\activate   (Windows)
source venv/Scripts/activate   (bash)
```
## ✅ Step 6: Install Dependencies

```
pip install -r requirements.txt
```

## ✅ Step 7: Upgrade pip (if needed)

If you face this recommendation:
```
[notice] A new release of pip is available: 24.3.1 -> 25.3
[notice] To update, run: python.exe -m pip install --upgrade pip
```

Run:
```
python.exe -m pip install --upgrade pip
```

## ✅ Step 8: Create the main.py file

Create the `main.py` file inside the project directory:

```
1. Problem-1-In-Memory-Library-Management-REST-API-Zimetrics/
   └── main.py
```

Directory Structure:
```
Problem-1-In-Memory-Library-Management-REST-API-Zimetrics/
├── main.py
├── requirements.txt
└── README.md
```

## ✅ Step 9: Import FastAPI

Import the FastAPI framework into your main.py file:

```python
from fastapi import FastAPI
```

## ✅ Step 10: Initialize FastAPI Application

Create the FastAPI application instance in your `main.py` file:

```python
from fastapi import FastAPI

app = FastAPI()
```

This creates the main FastAPI application object that will handle all your API routes and requests.


## ✅ Step 11: Create the Model Class

Create the Book model class using Pydantic's BaseModel for data validation:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
```

This Book model defines the structure of a book object with four fields:
- `id`: Unique identifier for the book (integer)
- `title`: Title of the book (string)
- `author`: Author of the book (string)
- `year`: Publication year (integer)

Pydantic's BaseModel provides automatic data validation and serialization for your API.

## ✅ Step 12: Create the In-Memory Storage

Create an in-memory database using a Python dictionary to store books:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

book_db = {}

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
```

**What is `book_db = {}`?**

This line creates an empty Python dictionary that will store all books in RAM (memory). 

- **Key**: Book ID (integer)
- **Value**: Book object (dictionary with book details)



## ✅ Step 12: To Add the Book Data 

Create an in-memory database using a Python dictionary to store books:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

book_db = {}

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
```

**What is `book_db = {}`?**

This line creates an empty Python dictionary that will store all books in RAM (memory). 

- **Key**: Book ID (integer)
- **Value**: Book object (dictionary with book details)



## ✅ Step 13: Import HTTPException and Create Add Books Endpoint

Import HTTPException for error handling and create the first API endpoint to add books:

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

book_db = {}

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
```


## ✅ Step 14: Book Creating Logic Done

Complete the add books endpoint with full functionality:

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

book_db = {}

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int

@app.post("/add-books")
def add_books(book: Book):
    if book.id in book_db:
        raise HTTPException(status_code=400, detail="Book with this ID already exists.")
    book_db[book.id] = book
    return {"message": "Book added successfully."}
```

