from fasthtml.common import FastHTML, Redirect

import auth.email
import auth.utils
import config
from components import page_content as page
from exceptions import handlers as exception_handlers

from pages.login import login as login_page
from pages.register import register as register_page

auth_app = FastHTML(exception_handlers=exception_handlers)


@auth_app.get("/login")
async def login_home(session):
    return page(config.APP_NAME, login_page(), links=None, session=session)


@auth_app.post("/login")
async def login(session, email: str, password: str):
    try:
        authenticated_user = auth.email.authenticate_user(email, password)
        if authenticated_user:
            auth.utils.login_user(session, authenticated_user)
            return Redirect("/")
        else:
            raise ValueError("User does not exist.")
    except ValueError as ve:
        return str(ve)
    except Exception:
        return "Error"


@auth_app.get("/logout")
async def logout(session):
    auth.utils.logout_user(session)
    return Redirect("/auth/login")


@auth_app.get("/register")
async def register_home(session):
    if auth.utils.is_authenticated(session):
        return Redirect("/")
    return page(config.APP_NAME, register_page(), links=None, session=session)


@auth_app.post("/register")
async def register(email: str, password: str, confirm_password: str):
    try:
        if password != confirm_password:
            raise ValueError("Passwords do not match.")
        auth.email.register_user(email, password)
        return Redirect("/")
    except ValueError as ve:
        return str(ve)
    except Exception:
        return "Error"
