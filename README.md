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
