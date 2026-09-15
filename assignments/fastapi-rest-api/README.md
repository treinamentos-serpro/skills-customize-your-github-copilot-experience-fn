# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

In this assignment, students will create a small REST API with FastAPI to manage a list of tasks or products. They will practice routing, request validation, HTTP methods, and API documentation while building a practical backend service.

## 📝 Tasks

### 🛠️ Set Up the FastAPI App

#### Descrição
Create a basic FastAPI application and define a root endpoint that returns a welcome message. Use an in-memory list to store your data while the app is running.

#### Requisitos
O programa concluído deve:

- Create a FastAPI instance named `app`.
- Add a root endpoint at `/` returning a JSON message like `{ "message": "Welcome to the Task API" }`.
- Keep a simple in-memory data list for your resources.
- Run the app locally with Uvicorn.

### 🛠️ Implement CRUD Endpoints

#### Descrição
Build the main endpoints for creating, reading, updating, and deleting items. Each item should have a unique identifier and a few fields such as title, description, price, and completed status.

#### Requisitos
O programa concluído deve:

- Add `GET /items` to return all items.
- Add `POST /items` to create a new item and return the created object with status `201`.
- Add `GET /items/{item_id}` to return a single item.
- Add `PUT /items/{item_id}` to update an existing item.
- Add `DELETE /items/{item_id}` to remove an item.
- Return `404` when the item ID does not exist.

### 🛠️ Add Validation and API Docs

#### Descrição
Use Pydantic models to enforce valid input and explore the auto-generated OpenAPI documentation provided by FastAPI.

#### Requisitos
O programa concluído deve:

- Define a `Item` model with fields such as `title`, `description`, `price`, and `completed`.
- Validate required fields and data types.
- Ensure every endpoint returns JSON in a consistent structure.
- Open the `/docs` page and confirm the API documentation is generated automatically.

```python
from fastapi import FastAPI

app = FastAPI(title="Task API")

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Task API"}
```
