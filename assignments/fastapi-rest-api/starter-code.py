from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Task API")


class Item(BaseModel):
    title: str
    description: str = ""
    price: float
    completed: bool = False


items = [
    {
        "id": 1,
        "title": "Learn FastAPI",
        "description": "Build a small restful API",
        "price": 0.0,
        "completed": False,
    }
]


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Task API"}


@app.get("/items")
async def list_items():
    return {"items": items}


@app.post("/items", status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    # TODO: create a new item and append it to the list
    pass


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    # TODO: find the item by id or raise 404
    pass


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    # TODO: update the item if it exists, otherwise raise 404
    pass


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int):
    # TODO: remove the item from the list and return no content
    pass
