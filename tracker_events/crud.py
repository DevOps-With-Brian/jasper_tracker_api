from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import json
from . import models
from .db import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def read_all_events(db:Session):
    events = jsonable_encoder(db.query(models.TrackerEvents).all())
    print(events)
    return events

def read_oos_events(db:Session):
    all_events = db.query(models.TrackerEvents)
    oos_events = []

    for event in all_events:
        if event.intent_name == 'out_of_scope':
            oos_events.append(event)
    return oos_events