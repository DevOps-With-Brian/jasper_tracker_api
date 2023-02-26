from sqlalchemy import create_engine, text
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy_utils import JSONType
from sqlalchemy.dialects.postgresql import JSONB, JSON


from fastapi import FastAPI
from sqlalchemy import Column, Integer, String, Text, Float
import os

from .db import Base


class TrackerEvents(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, server_default=text("nextval('\"public\".events_id_seq'::regclass)"))
    sender_id = Column(String(256), nullable=False, index=True)
    type_name = Column(String(256), nullable=False)
    timestamp = Column(Float(53))
    intent_name = Column(String(256))
    action_name = Column(String(256))
    data = Column(Text)
    