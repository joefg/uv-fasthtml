from functools import wraps
from secrets import token_hex
from typing import Optional

from fasthtml.common import (
    Beforeware, HTTPException, RedirectResponse
)

import models.users as users_model


def login_user(session, user_id) -> None:
    session["user_id"] = user_id
    session["csrf"] = token_hex(32)

def logout_user(session) -> None:
    session.pop("user_id", None)
    session.pop("csrf", None)


def get_current_user(session) -> Optional[users_model.User]:
    user_id = session.get("user_id")
    if user_id:
        user = users_model.get_user_by_id(user_id)
        if not user: logout_user(session)
        else: return user
    else: return None


def is_authenticated(session) -> bool:
    return "user_id" in session


def is_csrf_token_valid(request, session) -> bool:
    if 'x-csrf-token' not in request.headers: return False
    return request.headers['x-csrf-token'] == session['csrf']


def is_same_origin(request) -> bool:
    if 'Sec-Fetch-Site' not in request.headers: return True
    return request.headers['Sec-Fetch-Site'] in (
        'same-origin', # From the same domain
        'same-site',   # From the same site
        'none'         # Where it's not set, e.g. direct access
    )


def is_active(session) -> bool:
    if not is_authenticated(session): return False
    user = users_model.get_user_by_id(session["user_id"])
    if not user: return False
    return bool(user.is_active)


def is_admin(session) -> bool:
    if not is_authenticated(session): return False
    user = users_model.get_user_by_id(session["user_id"])
    if not user: return False
    return bool(user.is_admin)


def csrf_protect(func):
    @wraps(func)
    async def wrapper(request, session, *args, **kwargs):
        if not is_csrf_token_valid(request, session):
            raise HTTPException(status_code=401)
        return await func(request, session, *args, **kwargs)
    return wrapper


def from_same_origin(func):
    @wraps(func)
    async def wrapper(request, session, *args, **kwargs):
        if not is_same_origin(request):
            raise HTTPException(status_code=403)
        return await func(request, session, *args, **kwargs)
    return wrapper


def require_auth(func):
    @wraps(func)
    async def wrapper(request, session, *args, **kwargs):
        if not is_authenticated(session):
            raise HTTPException(status_code=404)
        return await func(request, session, *args, **kwargs)
    return wrapper


def require_admin(func):
    @wraps(func)
    async def wrapper(request, session, *args, **kwargs):
        if not is_authenticated(session):
            raise HTTPException(status_code=404)
        if not is_admin(session):
            raise HTTPException(status_code=401)
        return await func(request, session, *args, **kwargs)
    return wrapper


def before(request, session):
    auth = request.scope['auth'] = session.get('user_id', None)
    if not auth: return RedirectResponse("/auth/login", status_code=303)

beforeware = Beforeware(before, skip=['/auth/login', '/auth/oauth-redirect'])
