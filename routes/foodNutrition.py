from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
foodNutrition_router = APIRouter()

@foodNutrition_router.get('/{foodName}')
def getFoodNutrition(foodName: str):
    return JSONResponse(status_code = status.HTTP_200_OK,content = foodName)




