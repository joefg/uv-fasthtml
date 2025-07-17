from fasthtml.common import *

import config
from components import page_content as page

from pages.logbook import logbook as logbook_page
from pages.logbook import log_table as logbook_table
from pages.logbook import log_error as logbook_error

import models.logbook as logbook_model

logbook_app = FastHTML()

@logbook_app.get("/")
def get_logbook():
    return page(
        config.APP_NAME,
        logbook_page()
    )

@logbook_app.post("/submit")
def post_logbook(content: str):
    added = logbook_model.add_log(content)
    if added:
        return logbook_table()
    else:
        return logbook_error()
