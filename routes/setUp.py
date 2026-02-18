from fastapi import APIRouter
from pydantic import BaseModel
class userdata(BaseModel):
    id: str
    name: str
    username: str
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

setup_router = APIRouter()
@setup_router.post('/post/{data}')
def setUp(data: userdata):
    return {"Msg": userdata}
