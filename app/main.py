from fastapi import FastAPI
from app.api.endpoints import contact, birthday

app = FastAPI()

app.include_router(contact.router, prefix="/api/v1")
app.include_router(birthday.router, prefix="/api/v1")
