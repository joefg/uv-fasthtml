import logging

from fasthtml.common import FastHTML
import uvicorn

from alert import telegram as tg_alert
from beforeware import rate_limiter
import config
from exceptions import handlers as exception_handlers

from routes.admin import admin_app
from routes.auth import auth_app
from routes.health import health_app
from routes.home import home_app
from routes.protected import protected_app
from routes.static import static_app

app = FastHTML(
    before=rate_limiter,
    exception_handlers=exception_handlers
)

home_app.to_app(app)
health_app.to_app(app)
static_app.to_app(app)
auth_app.to_app(app)
protected_app.to_app(app)
admin_app.to_app(app)

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
