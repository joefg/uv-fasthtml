from fasthtml.common import FastHTML, RedirectResponse
from fasthtml.oauth import redir_url

import auth.utils
import auth.github as gh

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

@auth_app.get("/login")
async def login(request, session):
    redirect = redir_url(request, gh.auth_callback)
    login_link = gh.client.login_link(redirect)
    login_text = "Sign in with GitHub"
    return page(
        config.APP_NAME,
        login_page(login_text, login_link),
        links=None,
        session=session
    )


@auth_app.get("/oauth-redirect")
async def oauth_redirect(code: str, request, session):
    redirect = redir_url(request, "/auth/oauth-redirect")
    user_info = gh.client.retr_info(code, redirect)
    user_id = user_info[gh.client.id_key]

    user = get_user_by_id(user_id)
    if not user:
        register_user(user_info)
        auth.utils.login_user(session, user_id)
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
