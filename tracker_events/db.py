from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os


postgres_user = os.getenv("POSTGRES_USER")
postgres_pw = os.getenv("POSTGRES_PW")
postgres_host = os.getenv("POSTGRES_HOST")


my_database_connection = "postgresql://{0}:{1}@{2}/rasa".format(postgres_user, postgres_pw, postgres_host)

engine = create_engine(my_database_connection)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(object):
    def as_dict(self):
        return dict((c.name,
                     getattr(self, c.name))
                     for c in self.__table__.columns)

Base = declarative_base()