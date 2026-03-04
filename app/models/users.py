from datetime import datetime
from typing import Any, Callable

from sqlmodel import select

from .models import User


def _default_session_factory() -> Any:
    from database import connect

    return connect()


def search_users(
    query: str, session_factory: Callable[[], Any] | None = None
) -> list[User]:
    session_factory = session_factory or _default_session_factory
    users = []
    with session_factory() as session:
        statement = select(User).where(User.gh_login.contains(query))
        selected_users = session.exec(statement)
        if selected_users:
            users = list(selected_users.all())
    return users


def get_user_by_id(
    id: int, session_factory: Callable[[], Any] | None = None
) -> User | None:
    session_factory = session_factory or _default_session_factory
    user = None
    with session_factory() as session:
        statement = select(User).where(User.id == id)
        user = session.exec(statement).first()
    return user


def register_user(
    gh_user_info: dict, session_factory: Callable[[], Any] | None = None
) -> None:
    session_factory = session_factory or _default_session_factory
    created_at = datetime.fromisoformat(gh_user_info["created_at"])
    new_user = User(
        id=gh_user_info["id"],
        is_active=True,
        is_admin=False,
        gh_login=gh_user_info["login"],
        gh_node_id=gh_user_info["node_id"],
        gh_avatar_url=gh_user_info["avatar_url"],
        gh_type=gh_user_info["type"],
        gh_created_at=created_at,
    )
    with session_factory() as session:
        session.add(new_user)
        session.commit()


def update_user(
    gh_user_info: dict, session_factory: Callable[[], Any] | None = None
) -> None:
    session_factory = session_factory or _default_session_factory
    id = gh_user_info["id"]
    with session_factory() as session:
        statement = select(User).where(User.id == id)
        updated_user = session.exec(statement).one()
        updated_user.is_active = True
        updated_user.gh_login = gh_user_info["login"]
        updated_user.gh_node_id = gh_user_info["node_id"]
        updated_user.gh_avatar_url = gh_user_info["avatar_url"]
        updated_user.gh_type = gh_user_info["type"]
        session.add(updated_user)
        session.commit()


def delete_user(id: int, session_factory: Callable[[], Any] | None = None) -> None:
    session_factory = session_factory or _default_session_factory
    with session_factory() as session:
        statement = select(User).where(User.id == id)
        user = session.exec(statement).one()
        session.delete(user)
        session.commit()


def authenticate_user(
    id: int, session_factory: Callable[[], Any] | None = None
) -> bool:
    session_factory = session_factory or _default_session_factory
    active_user = False
    with session_factory() as session:
        statement = select(User).where(User.id == id)
        user = session.exec(statement).one()
        active_user = user.is_active
    return active_user


def update_last_login(
    user_id: int, session_factory: Callable[[], Any] | None = None
) -> None:
    session_factory = session_factory or _default_session_factory
    now = datetime.now()
    with session_factory() as session:
        statement = select(User).where(User.id == user_id)
        user = session.exec(statement).one()
        user.last_login = now
        session.add(user)
        session.commit()


def set_user_admin(
    user_id: int, change_to: bool, session_factory: Callable[[], Any] | None = None
) -> None:
    session_factory = session_factory or _default_session_factory
    with session_factory() as session:
        statement = select(User).where(User.id == user_id)
        user = session.exec(statement).one()
        user.is_admin = change_to
        session.add(user)
        session.commit()


def set_user_active(
    user_id: int, change_to: bool, session_factory: Callable[[], Any] | None = None
) -> None:
    session_factory = session_factory or _default_session_factory
    with session_factory() as session:
        statement = select(User).where(User.id == user_id)
        user = session.exec(statement).one()
        user.is_active = change_to
        session.add(user)
        session.commit()
