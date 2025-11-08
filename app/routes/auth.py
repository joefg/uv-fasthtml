from fasthtml.common import FastHTML, RedirectResponse
from fasthtml.oauth import redir_url

from starlette.background import BackgroundTasks

import auth.utils
import auth.github as github

from alert import telegram
import config
from components import page_content as page
from exceptions import handlers as exception_handlers

from models.users import (
    authenticate_user, get_user_by_id, register_user,
    update_last_login, update_user
)
from pages.login import login as login_page
from pages.login import account_deactivated as account_deactivated_page

auth_app = FastHTML(exception_handlers=exception_handlers)

def alert_new_signup(username: str):
    alert_message = f"""
✨ A new user has registered! ✨

{username} has signed up!
"""
    telegram(msg=alert_message)


@auth_app.get("/login")
async def login(request, session):
    login_forms = [
        github.auth.login_button(request),
    ]
    return page(
        config.APP_NAME,
        login_page(login_forms),
        links=None,
        session=session
    )


@auth_app.get("/oauth-redirect")
async def oauth_redirect(code: str, request, session):
    redirect = redir_url(request, "/auth/oauth-redirect")
    user_info = github.auth.client.retr_info(code, redirect)
    user_id = user_info[github.auth.client.id_key]

    user = get_user_by_id(user_id)
    if not user:
        register_user(user_info)
        user = get_user_by_id(user_id)
        tasks = BackgroundTasks()
        tasks.add_task(alert_new_signup, username=user.gh_login)
        auth.utils.login_user(session, user_id)
        return RedirectResponse("/", status_code=303, background=tasks)
    else:
        if not bool(user.is_active):
            return page(
                config.APP_NAME,
                account_deactivated_page(),
                links=None,
                session=session
            )
        else:
            authenticate_user(user_id)
            auth.utils.login_user(session, user_id)
            update_user(user_info)
            update_last_login(user_id)
    return RedirectResponse("/", status_code=303)


@auth_app.get("/logout")
async def logout(session):
    auth.utils.logout_user(session)
    return RedirectResponse("/auth/login", status_code=303)
