from dataclasses import dataclass
from datetime import datetime
from secrets import token_hex
from typing import Optional

import db.database
from utils import hash_password


@dataclass
class User:
    id: int
    email: str
    password_hash: str
    password_salt: str
    is_active: bool
    is_admin: bool
    creation_date: Optional[datetime] = None
    last_login: Optional[datetime] = None


def get_all_users() -> list[User]:
    logs = []
    with db.database.db.connect() as connection:
        cursor = connection.cursor()
        cursor.row_factory = lambda cursor, row: User(*row)
        sql = """
            select
                id,
                email,
                password_hash,
                password_salt,
                is_active,
                is_admin,
                creation_date,
                last_login
            from users;
        """
        cursor.execute(sql)
        logs = cursor.fetchall()
    return logs


def get_user(email: str) -> User:
    user = None
    with db.database.db.connect() as connection:
        cursor = connection.cursor()
        cursor.row_factory = lambda cursor, row: User(*row)
        sql = """
            select
                id,
                email,
                password_hash,
                password_salt,
                is_active,
                is_admin,
                creation_date,
                last_login
            from users
            where users.email = :user_email
            limit 1;
        """
        cursor.execute(sql, {"user_email": email})
        user = cursor.fetchone()
    return user


def get_user_by_id(id: int) -> User:
    user = None
    with db.database.db.connect() as connection:
        cursor = connection.cursor()
        cursor.row_factory = lambda cursor, row: User(*row)
        sql = """
            select
                id,
                email,
                password_hash,
                password_salt,
                is_active,
                is_admin,
                creation_date,
                last_login
            from users
            where users.id = :user_id
            limit 1;
        """
        cursor.execute(sql, {"user_id": id})
        user = cursor.fetchone()
    return user


def register_user(email: str, password: str) -> None:
    password_salt = token_hex(16)
    password_hash = hash_password(password, password_salt)
    with db.database.db.connect() as connection:
        cursor = connection.cursor()
        cursor.row_factory = lambda cursor, row: User(*row)
        sql = """
            insert into users (email, password_hash, password_salt, is_active)
            values (
                :email,
                :password_hash,
                :password_salt,
                :is_active
            );
        """
        params = {
            "email": email,
            "password_hash": password_hash,
            "password_salt": password_salt,
            "is_active": True,
        }
        cursor.execute(sql, params)
        connection.commit()


def authenticate_user(email: str, password: str) -> Optional[User]:
    with db.database.db.connect() as connection:
        cursor = connection.cursor()
        cursor.row_factory = lambda cursor, row: User(*row)
        sql = """
            select id, email, password_hash, password_salt, is_active, is_admin
            from users
            where users.email = :email;
        """
        params = {"email": email}
        cursor.execute(sql, params)
        user = cursor.fetchone()
        if not user:
            return None
        if not user.is_active:
            raise ValueError("Account deactivated, please contact support.")
        if user.password_hash == hash_password(password, user.password_salt):
            return user
    return None


def update_last_login(user_id: int) -> None:
    with db.database.db.connect() as connection:
        cursor = connection.cursor()
        cursor.row_factory = lambda cursor, row: User(*row)
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
        cursor.row_factory = lambda cursor, row: User(*row)
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
        cursor.row_factory = lambda cursor, row: User(*row)
        sql = """
            update users
            set is_active = :change_to
            where users.id = :user_id;
        """
        params = {"user_id": user_id, "change_to": change_to}
        cursor.execute(sql, params)
        connection.commit()
