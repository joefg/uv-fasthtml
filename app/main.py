from fasthtml.common import *

from exceptions import handlers as exception_handlers
import db.database as database
import config

from routes.home import home_app
from routes.logbook import logbook_app
from routes.shout import shout_app

app = FastHTML(
    exception_handlers=exception_handlers,
    routes=[
        Route('/', home_app, name="home"),
        Mount('/logbook', logbook_app, name="logbook"),
        Mount('/shout', shout_app, name="shout")
    ]
)
db = database.db

@app.get("/health")
def get_health():
    status = "error"
    if db: status = "ok"
    return {
        "database": status
    }

if __name__ == "__main__":
    serve()
