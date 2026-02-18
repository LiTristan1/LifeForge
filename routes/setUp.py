from fastapi import APIRouter
class userdata(BaseModel):
    name: str
    username: str
    age: int
    height: int
    activityLevel: int
    budget: int
    dietaryRestrictions: []
    mealsPerDay: int

setup_router = APIRouter()

@setup_router.post('/post/{data}')
def setUp(data: userdata):
    return {"Msg": userdata}
