from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
import os

from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from models.User_model import User
from routes.user_routes import router

load_dotenv()

app = FastAPI()

app.add_middleware(
    SessionMiddleware,
    secret_key=os.getenv("SESSION_SECRET_KEY")
)

mongo_url = os.getenv("MongoDB_URL")
database_name = os.getenv("DATABASE_NAME")

client = AsyncIOMotorClient(mongo_url)
database = client[database_name]


@app.on_event("startup")
async def start_database():
    await init_beanie(
        database=database,
        document_models=[User]
    )


app.include_router(router)


@app.get("/")
async def root():
    return {
        "message": "MongoDB connected successfully"
    }