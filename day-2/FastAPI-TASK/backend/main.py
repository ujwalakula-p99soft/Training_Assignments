from fastapi import FastAPI
from database.db import engine, Base
from routes.product_routes import router

app = FastAPI()


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
def home():
    return {"message":"Welcome to FastAPI Application with Postgres db"} 

app.include_router(router, prefix="/products", tags=["products"])