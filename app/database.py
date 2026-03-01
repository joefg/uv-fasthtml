from contextlib import contextmanager

import config

from sqlalchemy.engine import Engine
from sqlalchemy import event
from sqlmodel import create_engine, Session

engine = create_engine("sqlite:///database/database.sqlite3")

@event.listens_for(Engine, "connect")
def _set_sqlite_wal(connection, record):
    cursor = connection.cursor()
    cursor.execute("PRAGMA journal_mode=WAL;")
    cursor.close()

@contextmanager
def connect():
    with Session(engine) as session:
        yield session
