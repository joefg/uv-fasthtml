from typing import Any, Callable

from sqlmodel import select

from .models import UserNote


def _default_session_factory() -> Any:
    from database import connect

    return connect()


def get_user_notes(
    user_id: int, session_factory: Callable[[], Any] | None = None
) -> list[UserNote]:
    session_factory = session_factory or _default_session_factory
    notes = []
    with session_factory() as session:
        statement = (
            select(UserNote)
            .where(UserNote.user_id == user_id)
            .order_by(UserNote.created_at.desc())
        )
        selected_notes = session.exec(statement)
        if selected_notes:
            notes = list(selected_notes.all())
    return notes


def add_user_note(
    user_id: int,
    added_by_id: int,
    note: str,
    session_factory: Callable[[], Any] | None = None,
) -> None:
    session_factory = session_factory or _default_session_factory
    user_note = UserNote(user_id=user_id, note_added_by=added_by_id, note=note)
    with session_factory() as session:
        session.add(user_note)
        session.commit()
