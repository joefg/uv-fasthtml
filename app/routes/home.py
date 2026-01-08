import config
from components import page_content as page

from routes.base import RouteApp
from pages.home import home as home_page

home_app = RouteApp()

@home_app.get("/")
async def home(session):
    return page(config.APP_NAME, home_page(), links=None, session=session)
