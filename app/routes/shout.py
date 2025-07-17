from fasthtml.common import *

import config
from components import page_content as page
from exceptions import handlers as exception_handlers

from models.shout import shout as shout_model
from pages.shout import shout as shout_page

shout_app = FastHTML(
    exception_handlers=exception_handlers,
    prefix="/shout"
)

@shout_app.get("/")
def shout_index():
    return page(
        config.APP_NAME,
        Container(
            H3("To use this, pass an argument to the endpoint.")
        )
    )

@shout_app.get("/{name}")
def get_name(name: str):
    return page(
        config.APP_NAME,
        shout_page(name)
    )
