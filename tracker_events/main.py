from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse, Response
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
import jsonify


from . import crud, models
from .db import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/get_all_events/")
def get_all_events(db: Session = Depends(get_db)):
    events = crud.read_all_events(db)
    return events

@app.get("/get_all_oos_events/")
def get_all_oos_events(db: Session = Depends(get_db)):
    events = crud.read_oos_events(db)
    return events