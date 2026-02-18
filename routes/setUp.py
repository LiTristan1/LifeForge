from fastapi import APIRouter
from pydantic import BaseModel
from enum import Enum
class userdata(BaseModel):
    id: str
    name: str
    sex: bool
    age: int
    height: int
    activityLevel: int
    budget: int
    dietaryRestrictions: [] | None
    allergies: []
    dislikes: []
    cravings: []
    mealsPerDay: int
    calorieTarget: int
    sugarTarget: int
    carbTarget:int
    proteinTarget: int
    sleepTarget: int
    sodiumTarget: int
    fatTarget: int
    waterTarget: int
    pastRecipes: []
    goals: [] | None
    units: str


class gender(Enum):
    male: 1
    female:2
    non_binary:2
    prefer_not_to_say:3
    other:4 

class height():
    value: str
    unit: enum

class unit(Enum):
    "cm",
    "in"



setup_router = APIRouter()
@setup_router.post('/post/{data}')
def setUp(data: userdata):
    return {"Msg": userdata}
