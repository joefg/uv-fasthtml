import logging

from fasthtml.common import FastHTML, Mount, Route
import uvicorn

from alert import telegram as tg_alert
import config
from exceptions import handlers as exception_handlers

from routes.admin import admin_app
from routes.auth import auth_app
from routes.health import health_app
from routes.home import home_app
from routes.protected import protected_app
from routes.static import static_app

app = FastHTML(
    exception_handlers=exception_handlers,
    routes=[
        Route("/", home_app, name="home"),
        Mount("/admin", admin_app, name="admin"),
        Mount("/auth", auth_app, name="auth"),
        Mount("/health", health_app, name="health"),
        Mount("/protected", protected_app, name="protected"),
        Mount("/static", static_app, name="static"),
    ],
)

if __name__ == "__main__":
    try:
        uvicorn.run("main:app", host="0.0.0.0", port=int(config.PORT), reload=config.DEBUG)
    except Exception as ex:
        logging.exception(f"Something went wrong on {config.APP_NAME}!")
        import traceback
        msg = (
            f"Something went wrong on {config.APP_NAME}!\n" +
            "\n" +
            "\n".join(traceback.format_exception(ex))
        )
        tg_alert(msg)
