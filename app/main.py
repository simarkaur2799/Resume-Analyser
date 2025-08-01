# app/main.py
from fastapi import FastAPI
from app.api.routes import router  # import your router

app = FastAPI()

app.include_router(router)
