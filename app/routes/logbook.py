from fasthtml.common import FastHTML

import config
from components import page_content as page
from exceptions import handlers as exception_handlers

from pages.logbook import log_error as logbook_error
from pages.logbook import logbook as logbook_page
from pages.logbook import log_table as logbook_table

import models.logbook as logbook_model

logbook_app = FastHTML(
    exception_handlers=exception_handlers
)

@logbook_app.get("/")
def get_logbook():
    return page(
        config.APP_NAME,
        logbook_page()
    )

@logbook_app.post("/submit")
def post_logbook(content: str):
    log = logbook_model.Log(None, content, None)
    added = logbook_model.add_log(log)
    if added:
        return logbook_table()
    else:
        return logbook_error()
