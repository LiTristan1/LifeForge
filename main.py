from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


class userdata(BaseModel):
    name: str
    username: str
    age: int
    height: int
    activityLevel: int
    budget: int
    dietaryRestrictions: []
    mealsPerDay: int

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q":q}

@app.put("/setup")
def initData(data: userdata):
    return {data}



