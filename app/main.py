from fasthtml.common import *

from components import page_content as page

from models.shout import shout as shout_model
import models.logbook as logbook_model

from pages.home import home as home_page
from pages.logbook import logbook as logbook_page
from pages.logbook import log_table as logbook_table
from pages.logbook import log_error as logbook_error

from pages.shout import shout as shout_page

import db.database as database
import config

app = FastHTML()
db = database.db

@app.get("/")
def home():
    return page(
        config.APP_NAME,
        home_page()
    )

@app.get("/health")
def get_health():
    if not db:
        return {
            "database": "error"
        }
    return {
        "database": "ok"
    }

@app.get("/shout/{name}")
def get_name(name: str):
    return page(
        config.APP_NAME,
        shout_page(name)
    )

@app.get("/logbook")
def get_logbook():
    return page(
        config.APP_NAME,
        logbook_page()
    )

@app.post("/logbook/submit")
def post_logbook(content: str):
    added = logbook_model.add_log(content)
    if added:
        return logbook_table()
    else:
        return logbook_error()

@app.get("/{path:path}")
def not_found(path: str):
    error = Container(
        H2("404: Page Not Found"),
        P(f"Sorry, the page '/{path}' doesn't exist."),
        A("Go home", href="/")
    )
    return page(
        "404: Page Not Found",
        error
    )

if __name__ == "__main__":
    serve()
