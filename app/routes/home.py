from fasthtml.common import *

import config
from components import page_content as page

from pages.home import home as home_page

home_app = FastHTML()

@home_app.get("/")
def home():
    return page(
        config.APP_NAME,
        home_page()
    )