from fastapi import FastAPI
from pydantic import BaseModel
from character_generator import generate_character

app = FastAPI()

class BodyContent(BaseModel):
    name: str

class CreateCharacterRequest(BaseModel):
    body: BodyContent

@app.post("/create-character")
async def create_character(request: CreateCharacterRequest):
    name = request.body.name
    character = generate_character(name)
    return character