from fastapi import FastAPI

import models
from database import engine
from router import auth, transaction

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
app.include_router(auth.router)
app.include_router(transaction.router)

@app.get('/')
def home_page():
    return "this is transaction home page"


