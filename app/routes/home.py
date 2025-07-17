from fasthtml.common import FastHTML

import config
from components import page_content as page
from exceptions import handlers as exception_handlers

from pages.home import home as home_page

home_app = FastHTML(
    exception_handlers=exception_handlers
)

@home_app.get("/")
async def home():
    return page(
        config.APP_NAME,
        home_page()
    )