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

## ✅ Step 13: To Add the Book Data 

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

## ✅ Step 14: Import HTTPException and Create Add Books Endpoint

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

## ✅ Step 15: Book Creating Logic Done

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

## ✅ Step 15: Run the Server to Test POST Function

Run this command to start the FastAPI development server:

```bash
uvicorn main:app --reload
```

**What does this command do?**

- `uvicorn`: ASGI server that runs FastAPI applications
- `main`: The name of your Python file (main.py)
- `app`: The FastAPI instance variable name in your code
- `--reload`: Automatically restarts the server when code changes are detected (useful for development)

**Expected Output:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

this is the postman image of the data creation response coming on post request 
image path 

## ✅ Step 16: Testing POST Request in Postman

This screenshot shows a successful POST request to add a book using Postman.

![Postman POST Request Screenshot](./screenshots/postman_post_request.png)

**Request Details:**
- **Method**: POST
- **URL**: `http://127.0.0.1:8000/add-books`
- **Content-Type**: JSON (raw)

**Request Body:**
```json
{
    "id": 1,
    "title": "Atomic Habits",
    "author": "James Clear",
    "year": 2018
}
```

**Response:**
- **Status Code**: 200 OK
- **Response Time**: 26 ms
- **Response Body**:
```json
{
    "message": "Book added successfully."
}
```

**What this confirms:**
- The API is running correctly on `http://127.0.0.1:8000`
- The `/add-books` endpoint is working properly
- Book data is being validated and stored in the in-memory database
- Success message is returned as expected

**Note:** 
To display the image, create a `screenshots` folder in your project directory and save your Postman screenshot as `postman_post_request.png` in that folder.

Alternatively, you can use the direct path:
```markdown
![Postman POST Request](path/to/your/Screenshot_2026-01-28_001137.png)
```