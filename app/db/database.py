import os
import sqlite3
from contextlib import contextmanager

import config

from sqlmodel import create_engine, SQLModel, Session

engine = create_engine(("sqlite:///" + config.DB_PATH) or "sqlite://database/database.sqlite3")

def init_db():
    SQLModel.metadata.create_all(engine)

@contextmanager
def connect():
    with Session(engine) as session:
        yield session
