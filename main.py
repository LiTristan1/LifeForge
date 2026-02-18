
from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from routes.foodNutrition import foodNutrition_router
from routes.humanInfo import human_health_router
from routes.ai import ai_router

app = FastAPI()
app.include_router(foodNutrition_router, prefix = '/food')
app.include_router(human_health_router, prefix = '/human')
app.include_router(ai_router, prefix = '/ai')