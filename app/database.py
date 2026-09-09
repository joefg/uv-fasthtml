from contextlib import contextmanager

from sqlalchemy.engine import Engine
from sqlalchemy import event
from sqlmodel import create_engine, Session

import config

engine = create_engine(config.DB_CONNECTION)

@event.listens_for(Engine, "connect")
def _set_sqlite_wal(connection, record):
    cursor = connection.cursor()
    cursor.execute("PRAGMA journal_mode=WAL;")
    cursor.close()

@contextmanager
def connect():
    with Session(engine) as session:
        yield session
