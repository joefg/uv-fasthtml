from fasthtml import APIRouter

import config
from components import page_content as page

from pages.home import home as home_page

home_app = APIRouter()

@home_app.get("/")
async def home(session):
    return page(config.APP_NAME, home_page(), links=None, session=session)
