# FastAPI Interview Notes

## 📘 Core Concepts
- **FastAPI**: Modern, high-performance Python framework for APIs.
- **Built on**:
  - **Starlette** → Handles HTTP requests/responses.
  - **Pydantic** → Data validation and type checking.
 ---   
## Why FastAPI over Flask?
- **Performance**: FastAPI uses **ASGI** (Asynchronous Server Gateway Interface) vs Flask’s **WSGI** (Web Server Gateway Interface).
  - ASGI → asynchronous, supports concurrent requests, better scalability..
  - WSGI → synchronous, blocking, slower under heavy load.
- **Server**: FastAPI → **Uvicorn** (ASGI server); Flask → **Gunicorn**(WSGI server).
- **Code Efficiency**: Less boilerplate, faster API development
---
## ⚡ Philosophy
- **Fast to run**:
  - Asynchronous (ASGI) → concurrent request handling.
  - Uvicorn server → non-blocking, high performance.
  - Async/await → processes multiple requests while waiting for I/O.
- **Fast to code**:
  - Minimal boilerplate.
  - Automatic validation.
  - Cleaner, developer-friendly syntax.
---
## Key Features
- **Async/Await Support**: Non-blocking request handling.
- **Data Validation**: Pydantic ensures correct input formats.
- **Industry-grade APIs**: Ideal for ML/AI/DS applications.
---
## 🆚 Flask vs FastAPI
| Feature        | Flask (WSGI) | FastAPI (ASGI) |
|----------------|--------------|----------------|
| Server         | Gunicorn     | Uvicorn        |
| Nature         | Synchronous  | Asynchronous   |
| Performance    | Blocking     | Non-blocking   |
| Analogy        | Waiter serves one table at a time | Waiter serves multiple tables efficiently |

---

## 🛠 Setup & Demo
- Install:  
  ```bash
  pip install fastapi uvicorn pydantic
- Code 
  ```
  from fastapi import FastAPI
  app = FastAPI()
  @app.get("/")
  def read_root():
      return {"Hello": "World"}
- Creating a virtual environment and activate it
  ```bash
  python -m venv myenv
  myenv\Scripts\activate
- Start an app
  ```bash
  uvicorn main:app --reload
- Swagger and Redocly routes
  ```
  /docs
  /redoc

# 📘 Study Notes: Pydantic Crash Course

## 🔑 Core Concepts
- **Python’s dynamic typing** → Flexible but risky in production.
- **Problem 1: Type Validation**
  - Type hints don’t enforce correctness.
  - Manual checks are repetitive and unscalable.
  - Pydantic enforces strict type validation automatically.
- **Problem 2: Data Validation**
  - Values must meet logical constraints (e.g., age ≥ 0, valid email).
  - Without validation, incorrect data can slip into databases.
  - Pydantic handles these rules elegantly.

## ⚙️ How Pydantic Works
1. **Define a Model**
   - Create a class inheriting from `BaseModel`.
   - Specify fields and their types.
   - Add constraints (e.g., `age > 0`).
2. **Instantiate with Raw Data**
   - Pass dictionaries into the model.
   - Pydantic validates automatically.
   - Raises errors if data is invalid.
3. **Use Validated Objects**
   - Functions receive validated Pydantic objects.
   - Cleaner, reusable, and scalable code.

## 🛠️ Features Highlighted
- **Automatic type conversion** → `"30"` (string) → `30` (int).
- **Error handling** → Clear errors for missing/invalid fields.
- **Complex fields** → Lists, dictionaries, nested models supported.

## 📌 Example
```python
from pydantic import BaseModel
from typing import List, Dict

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact: Dict[str, str]

patient = Patient(
    name="Nitesh",
    age=30,
    weight=75.2,
    married=True,
    allergies=["pollen", "dust"],
    contact={"email": "abc@gmail.com", "phone": "1234567890"}
)
