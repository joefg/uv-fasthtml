from fasthtml.common import HTTPException

from auth.utils import require_admin
import config
from components import page_content as page

from routes.base import RouteApp
import models.users as users_model
from pages.admin import (
    admin_page, user_page, user_card, users_table, notes_list
)

admin_app = RouteApp()

@admin_app.get("/")
@require_admin
async def get_admin(session):
    return page(config.APP_NAME, admin_page(), session=session)


@admin_app.post("/users")
@require_admin
async def search(session, query: str):
    results = users_model.search_users(query)
    if not results: return "No user found"
    if len(query) >= 5: return users_table(results)
    else: return users_table(None)


@admin_app.get("/user/{id}")
@require_admin
async def get_user(session, id: int):
    user = users_model.get_user_by_id(id)
    notes = users_model.get_user_notes(id)
    if not user: raise HTTPException(status_code=404)
    hide_operations = session["user_id"] == id
    return page(config.APP_NAME, user_page(user, notes, hide_operations), session=session)


@admin_app.get("/user/{id}/notes")
@require_admin
async def get_user_notes(session, id: int):
    notes = users_model.get_user_notes(id)
    if not notes: raise HTTPException(status_code=404)
    return notes_list(notes)


@admin_app.post("/user/{id}/add-note")
@require_admin
async def add_note(session, id: int, note: str):
    users_model.add_user_note(id, session["user_id"], note)
    notes = users_model.get_user_notes(id)
    return notes_list(notes)


@admin_app.post("/user/{id}/grant-admin")
@require_admin
async def grant_admin(session, id: int):
    user = users_model.get_user_by_id(id)
    if not user: raise HTTPException(status_code=404)
    if bool(user.is_admin): raise HTTPException(status_code=409)
    if session["user_id"] == id: raise HTTPException(status_code=400)
    else:
        users_model.set_user_admin(user.id, True)
        ret = users_model.get_user_by_id(user.id)
    return user_card(ret)


@admin_app.post("/user/{id}/revoke-admin")
@require_admin
async def revoke_admin(session, id: int):
    user = users_model.get_user_by_id(id)
    if not user: raise HTTPException(status_code=404)
    if not bool(user.is_admin): raise HTTPException(status_code=409)
    if session["user_id"] == id: raise HTTPException(status_code=400)
    else:
        users_model.set_user_admin(user.id, False)
        ret = users_model.get_user_by_id(user.id)
    return user_card(ret)


@admin_app.post("/user/{id}/activate")
@require_admin
async def activate_user(session, id: int):
    user = users_model.get_user_by_id(id)
    if not user: raise HTTPException(status_code=404)
    if bool(user.is_active): raise HTTPException(status_code=409)
    if session["user_id"] == id: raise HTTPException(status_code=400)
    else:
        users_model.set_user_active(user.id, True)
        ret = users_model.get_user_by_id(user.id)
    return user_card(ret)


@admin_app.post("/user/{id}/deactivate")
@require_admin
async def deactivate_user(session, id: int):
    user = users_model.get_user_by_id(id)
    if not user: raise HTTPException(status_code=404)
    if not bool(user.is_active): raise HTTPException(status_code=409)
    if session["user_id"] == id: raise HTTPException(status_code=400)
    else:
        users_model.set_user_active(user.id, False)
        ret = users_model.get_user_by_id(user.id)
    return user_card(ret)
