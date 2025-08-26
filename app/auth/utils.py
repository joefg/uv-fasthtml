from functools import wraps
from typing import Optional

from fasthtml.common import HTTPException

import config
import models.users as users_model

def login_user(session, user: users_model.User) -> None:
    session["user_id"] = user.id
    session["email"] = user.email

def logout_user(session) -> None:
    session.pop("user_id", None)
    session.pop("email", None)

def get_current_user(session) -> Optional[users_model.User]:
    user_id = session.get("user_id")
    if not user_id: return None
    else: return users_model.get_user_by_id(user_id)

def is_authenticated(session) -> bool:
    return "user_id" in session

def is_active(session) -> bool:
    if not is_authenticated(session): return False
    user = users_model.get_user_by_id(session["user_id"])
    return bool(user.is_active) == True

def is_admin(session) -> bool:
    if not is_authenticated(session): return False
    user = users_model.get_user_by_id(session["user_id"])
    return bool(user.is_admin) == True

def require_auth(func):
    @wraps(func)
    async def wrapper(session, *args, **kwargs):
        if not is_authenticated(session):
            raise HTTPException(status_code=404)
        return await func(session, *args, **kwargs)
    return wrapper

def require_admin(func):
    @wraps(func)
    async def wrapper(session, *args, **kwargs):
        if not is_authenticated(session):
            raise HTTPException(status_code=404)
        if not is_admin(session):
            raise HTTPException(status_code=401)
        return await func(session, *args, **kwargs)
    return wrapper