from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from google import genai

client = genai.Client()
ai_router = APIRouter()

@ai_router.get('/get/{adviceType}')
def getAdvice(adviceType: str):
    response = client.models.generate_content(
        model = "gemini-3-flash-preview", content = "Explain how AI works in a few words"
    )
    print(response.text)
    return JSONResponse(status_code = status.HTTP_200_OK, content = adviceType)