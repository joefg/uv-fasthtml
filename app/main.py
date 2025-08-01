from fasthtml.common import (
    FastHTML, Mount, Route, serve
)
import uvicorn

import config
import db.database as database
from exceptions import handlers as exception_handlers

from routes.admin import admin_app
from routes.auth import auth_app
from routes.health import health_app
from routes.home import home_app
from routes.logbook import logbook_app
from routes.protected import protected_app
from routes.static import static_app

app = FastHTML(
    exception_handlers=exception_handlers,
    routes=[
        Route('/', home_app, name="home"),
        Mount('/admin', admin_app, name="admin"),
        Mount('/auth', auth_app, name="auth"),
        Mount('/health', health_app, name="health"),
        Mount('/logbook', logbook_app, name="logbook"),
        Mount('/protected', protected_app, name="protected"),
        Mount('/static', static_app, name="static")
    ],
)

if __name__ == "__main__":
    database.db.migrate()
    uvicorn.run("main:app", host='0.0.0.0', port=int(config.PORT), reload=True)
