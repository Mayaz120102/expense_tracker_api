from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
from database import SessionLocal, engine
from router import auth


app = FastAPI()

models.Base.metadata.create_all(bind=engine)
app.include_router(auth.router)

@app.get('/')
def home_page():
    return "this is transaction home page"