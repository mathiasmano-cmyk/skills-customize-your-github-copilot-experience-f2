from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float

items: Dict[int, Item] = {
    1: Item(id=1, name="Sample Item", description="A sample item", price=9.99)
}

@app.get("/items")
def list_items():
    return list(items.values())

@app.get("/items/{item_id}")
def get_item(item_id: int):
    item = items.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items")
def create_item(item: Item):
    if item.id in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item.id] = item
    return item

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    return item

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"ok": True}

# Run with: uvicorn starter-code:app --reload
