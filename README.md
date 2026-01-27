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

```
from fastapi import FastAPI
```

## ✅ Step 10: Import FastAPI

Create the `main.py` file inside the project directory:

```
from fastapi import FastAPI

app = FastAPI()
```

