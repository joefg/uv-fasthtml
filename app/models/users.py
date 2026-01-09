from dataclasses import dataclass
from datetime import datetime
from typing import Optional

import db.database


@dataclass
class User:
    id: int
    is_active: bool
    is_admin: bool
    gh_login: str
    gh_node_id: str
    gh_avatar_url: str
    gh_type: str
    gh_created_at: datetime
    creation_date: datetime
    last_login: datetime

@dataclass
class UserNote:
    id: int
    user_id: int
    note_added_by: int
    note: str
    created_at: datetime


def search_users(query: str) -> list[User]:
    users = []
    with db.database.db.connect() as connection:
        cursor = connection.cursor()
        cursor.row_factory = lambda _, row: User(*row)
        sql = """
            select
                id,
                is_active,
                is_admin,
                gh_login,
                gh_node_id,
                gh_avatar_url,
                gh_type,
                gh_created_at,
                creation_date,
                last_login
            from users
            where gh_login like '%' || :query || '%'
            limit 15;
        """
        cursor.execute(sql, {'query': query})
        users = cursor.fetchall()
    return users


def get_user_by_id(id: int) -> User:
    user = None
    with db.database.db.connect() as connection:
        cursor = connection.cursor()
        cursor.row_factory = lambda _, row: User(*row)
        sql = """
            select
                id,
                is_active,
                is_admin,
                gh_login,
                gh_node_id,
                gh_avatar_url,
                gh_type,
                gh_created_at,
                creation_date,
                last_login
            from users
            where users.id = :user_id
            limit 1;
        """
        cursor.execute(sql, {"user_id": id})
        user = cursor.fetchone()
    return user


def register_user(gh_user_info: dict) -> None:
    with db.database.db.connect() as connection:
        cursor = connection.cursor()
        cursor.row_factory = lambda _, row: User(*row)
        sql = """
            insert into users (
                id,
                email,
                is_active,
                is_admin,
                gh_login,
                gh_node_id,
                gh_avatar_url,
                gh_type,
                gh_created_at
            ) values (
                :id,
                :email,
                :is_active,
                :is_admin,
                :gh_login,
                :gh_node_id,
                :gh_avatar_url,
                :gh_type,
                :gh_created_at
            );
        """
        params = {
            "id": gh_user_info['id'],
            "email": (gh_user_info['email'] or "None provided"),
            "is_active": True,
            "is_admin": False,
            "gh_login": gh_user_info['login'],
            "gh_node_id": gh_user_info['node_id'],
            "gh_avatar_url": gh_user_info['avatar_url'],
            "gh_type": gh_user_info['type'],
            "gh_created_at": gh_user_info['created_at']
        }
        cursor.execute(sql, params)
        connection.commit()


def update_user(gh_user_info: dict) -> None:
    with db.database.db.connect() as connection:
        cursor = connection.cursor()
        cursor.row_factory = lambda _, row: User(*row)
        sql = """
            update users
            set
                id = :id,
                email = :email,
                is_active = :is_active,
                gh_login = :gh_login,
                gh_node_id = :gh_node_id,
                gh_avatar_url = :gh_avatar_url,
                gh_type = :gh_type,
                gh_created_at = :gh_created_at
            where id = :id;
        """
        params = {
            "id": gh_user_info['id'],
            "email": (gh_user_info['email'] or "None provided"),
            "is_active": True,
            "gh_login": gh_user_info['login'],
            "gh_node_id": gh_user_info['node_id'],
            "gh_avatar_url": gh_user_info['avatar_url'],
            "gh_type": gh_user_info['type'],
            "gh_created_at": gh_user_info['created_at']
        }
        cursor.execute(sql, params)
        connection.commit()


def delete_user(id: int) -> None:
    with db.database.db.connect() as connection:
        cursor = connection.cursor()
        cursor.row_factory = lambda _, row: User(*row)
        sql = """
            delete from users
            where users.id = :id;
        """
        params = {"id": id}
        cursor.execute(sql, params)


def authenticate_user(id: int) -> Optional[User]:
    with db.database.db.connect() as connection:
        cursor = connection.cursor()
        sql = """
            select id, is_active
            from users
            where users.id = :id;
        """
        params = {"id": id}
        cursor.execute(sql, params)
        user = cursor.fetchone()
        if not user: return None
        else: return user


def update_last_login(user_id: int) -> None:
    with db.database.db.connect() as connection:
        cursor = connection.cursor()
        cursor.row_factory = lambda _, row: User(*row)
        sql = """
            update users
            set last_login = current_timestamp
            where users.id = :user_id;
        """
        params = {"user_id": user_id}
        cursor.execute(sql, params)
        connection.commit()


def set_user_admin(user_id: int, change_to: bool) -> None:
    with db.database.db.connect() as connection:
        cursor = connection.cursor()
        cursor.row_factory = lambda _, row: User(*row)
        sql = """
            update users
            set is_admin = :change_to
            where users.id = :user_id;
        """
        params = {"user_id": user_id, "change_to": change_to}
        cursor.execute(sql, params)
        connection.commit()


def set_user_active(user_id: int, change_to: bool) -> None:
    with db.database.db.connect() as connection:
        cursor = connection.cursor()
        cursor.row_factory = lambda _, row: User(*row)
        sql = """
            update users
            set is_active = :change_to
            where users.id = :user_id;
        """
        params = {"user_id": user_id, "change_to": change_to}
        cursor.execute(sql, params)
        connection.commit()

def get_user_notes(user_id: int) -> list[UserNote]:
    notes = []
    with db.database.db.connect() as connection:
        cursor = connection.cursor()
        cursor.row_factory = lambda _, row: UserNote(*row)
        sql = """
            select
                id,
                user_id,
                added_by_id,
                note,
                creation_date
            from user_note
            where user_id = :user_id
            order by creation_date desc;
        """
        cursor.execute(sql, {"user_id": user_id})
        notes = cursor.fetchall()
    return notes

def add_user_note(user_id: int, added_by_id: int, note: str) -> None:
    with db.database.db.connect() as connection:
        cursor = connection.cursor()
        sql = """
            insert into user_note (
                user_id,
                note,
                added_by_id
            ) values (
                :user_id,
                :note,
                :added_by_id
            );
        """
        params = {
            "user_id": user_id,
            "note": note,
            "added_by_id": added_by_id
        }
        cursor.execute(sql, params)
        connection.commit()
