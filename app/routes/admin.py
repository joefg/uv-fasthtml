from fasthtml.common import (
    FastHTML, HTTPException
)

from auth.utils import (
    require_auth, require_admin, is_active, is_admin
)
import config
from components import page_content as page
from exceptions import handlers as exception_handlers

import models.users as users_model
from pages.admin import (
    admin_page, user_page, user_card
)

admin_app = FastHTML(
    exception_handlers=exception_handlers
)

@admin_app.get("/")
@require_admin
async def get_admin(session):
    return page(
        config.APP_NAME,
        admin_page(),
        session=session
    )

@admin_app.get("/user/{id}")
@require_admin
async def get_user(session, id: int):
    user = users_model.get_user_by_id(id)
    if not user:
        raise HTTPException(status_code=404)
    hide_operations = (session["user_id"] == id)
    return page(
        config.APP_NAME,
        user_page(user, hide_operations),
        session=session
    )

@admin_app.post("/user/{id}/grant-admin")
@require_admin
async def grant_admin(session, id: int):
    user = users_model.get_user_by_id(id)
    if not user:
        raise HTTPException(status_code=404)
    if user.is_admin == 1:
        raise HTTPException(status_code=409)
    if session["user_id"] == id:
        raise HTTPException(status_code=400)
    else:
        users_model.set_user_admin(user.id, True)
        ret = users_model.get_user_by_id(user.id)
    return user_card(ret)

@admin_app.post("/user/{id}/revoke-admin")
@require_admin
async def revoke_admin(session, id: int):
    user = users_model.get_user_by_id(id)
    if not user:
        raise HTTPException(status_code=404)
    if user.is_admin == 0:
        raise HTTPException(status_code=409)
    if session["user_id"] == id:
        raise HTTPException(status_code=400)
    else:
        users_model.set_user_admin(user.id, False)
        ret = users_model.get_user_by_id(user.id)
    return user_card(ret)

@admin_app.post("/user/{id}/activate")
@require_admin
async def activate_user(session, id: int):
    user = users_model.get_user_by_id(id)
    if not user:
        raise HTTPException(status_code=404)
    if user.is_active == 1:
        raise HTTPException(status_code=409)
    if session["user_id"] == id:
        raise HTTPException(status_code=400)
    else:
        users_model.set_user_active(user.id, True)
        ret = users_model.get_user_by_id(user.id)
    return user_card(ret)

@admin_app.post("/user/{id}/deactivate")
@require_admin
async def deactivate_user(session, id: int):
    user = users_model.get_user_by_id(id)
    if not user:
        raise HTTPException(status_code=404)
    if user.is_active == 0:
        raise HTTPException(status_code=409)
    if session["user_id"] == id:
        raise HTTPException(status_code=400)
    else:
        users_model.set_user_active(user.id, False)
        ret = users_model.get_user_by_id(user.id)
    return user_card(ret)