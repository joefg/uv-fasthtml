from fasthtml.common import FastHTML

import config
from components import page_content as page
from exceptions import handlers as exception_handlers

from models.shout import shout as shout_model
from pages.shout import shout as shout_page
from pages.shout import shout_index as shout_home

shout_app = FastHTML(
    exception_handlers=exception_handlers
)

@shout_app.get("/")
async def shout_index():
    return page(
        config.APP_NAME,
        shout_home()
    )

@shout_app.get("/{name}")
async def get_name(name: str):
    return page(
        config.APP_NAME,
        shout_page(name)
    )
