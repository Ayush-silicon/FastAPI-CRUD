from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    origin: str

Items : List[Item] = []


#Decorator to define the root endpoint
#Create a simple API with FastAPI
#CRUD operations for items

@app.get("/")
def read_root():
    return {"message": "Welcome to the Item API"}       

@app.get("/items")
def get_items():
    return Items

@app.post("/items")
def add_item(item: Item):
    Items.append(item)
    return {"message": "Item added successfully", "item": item}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    for idx, existing_item in enumerate(Items):
        if existing_item.id == item_id:
            Items[idx] = item
            return {"message": "Item updated successfully", "item": item}
    return {"message": "Item not found"}, 404

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for idx, existing_item in enumerate(Items):
        if existing_item.id == item_id:
            del Items[idx]
            return {"message": "Item deleted successfully"}
    return {"message": "Item not found"}, 404
