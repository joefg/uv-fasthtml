from fasthtml.common import (
    FastHTML, FileResponse, Mount, Route, serve
)

from exceptions import handlers as exception_handlers

from routes.health import health_app
from routes.home import home_app
from routes.logbook import logbook_app
from routes.static import static_app

app = FastHTML(
    exception_handlers=exception_handlers,
    routes=[
        Route('/', home_app, name="home"),
        Mount('/health', health_app, name="health"),
        Mount('/static', static_app, name="static"),
        Mount('/logbook', logbook_app, name="logbook")
    ],
)

if __name__ == "__main__":
    serve()
