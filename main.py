from fastapi import FastAPI, Request
from pydantic import BaseModel
from character_generator import generate_character

app = FastAPI()

class BodyContent(BaseModel):
    name: str

class CreateCharacterRequest(BaseModel):
    body: BodyContent

@app.post("/create-character")
async def create_character(request: Request):
    data = await request.json()
    print("Request recibido:", data)
    name = data["body"]["name"]
    character = generate_character(name)
    return character