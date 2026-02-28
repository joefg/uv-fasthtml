from datetime import datetime

from sqlmodel import (
    Field, Session, SQLModel,
    select, create_engine
)

from db.database import connect


class UserNote(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int
    note_added_by: int
    note: str
    created_at: datetime | None = Field(default=datetime.now())


def get_user_notes(user_id: int) -> list[UserNote]:
    notes = []
    with connect() as session:
        statement = select(UserNote) \
            .where(UserNote.user_id == user_id) \
            .order_by(UserNote.created_at.desc())
        selected_notes = session.exec(statement)
        if selected_notes:
            notes = selected_notes.all()
    return notes


def add_user_note(user_id: int, added_by_id: int, note: str) -> None:
    note = UserNote(
        user_id=user_id,
        note_added_by=added_by_id,
        note=note
    )
    with connect() as session:
        session.add(note)
        session.commit()
