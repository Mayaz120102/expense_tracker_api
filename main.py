from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
from database import SessionLocal, engine


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get('/')
def home_page():
    return "this is transaction home page"