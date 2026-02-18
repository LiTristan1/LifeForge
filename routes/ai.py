from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from google import genai
from google.genai import types

client = genai.Client()
ai_router = APIRouter()


@ai_router.get('/get/{meal}')
def getRecipe(meal: str):
    response = client.models.generate_content(
        model = "gemini-3-flash-preview", 
        contents = "Generate the recipe for {meal}",
        config = types.GenerateContentConfig(
            system_instruction = "You are a professional restaurant chef for medium income customers",
            thinking_config = types.ThinkingConfig(thinking_level="low")
        )
    )
    print(response.text)
    return JSONResponse(status_code = status.HTTP_200_OK, content = {'recipe': response.text})