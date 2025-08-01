from fasthtml.common import (
    FastHTML, HTTPException
)

import auth.utils
import config
from components import page_content as page
from exceptions import handlers as exception_handlers

from pages.logbook import log_error as logbook_error
from pages.logbook import add_logbook, view_logbook
from pages.logbook import log_table as logbook_table

import models.logbook as logbook_model

logbook_app = FastHTML(
    exception_handlers=exception_handlers
)

@logbook_app.get("/")
async def get_logbook(session):
    if auth.utils.is_authenticated(session):
        return page(
            config.APP_NAME,
            add_logbook(),
            session=session
        )
    else:
        return page(
            config.APP_NAME,
            view_logbook(),
            session=session
        )

@logbook_app.post("/submit")
@auth.utils.require_auth
async def post_logbook(session, content: str):
    user = auth.utils.get_current_user(session)
    added = logbook_model.add_log(content, user.id)
    if added:
        return logbook_table()
    else:
        return logbook_error()
