from fasthtml.common import (
    FastHTML, FileResponse, Mount, Route, serve
)

import config
import db.database as database
from exceptions import handlers as exception_handlers

from routes.home import home_app
from routes.logbook import logbook_app

app = FastHTML(
    exception_handlers=exception_handlers,
    routes=[
        Route('/', home_app, name="home"),
        Mount('/logbook', logbook_app, name="logbook")
    ]
)
db = database.db

@app.get("/health")
async def get_health():
    status = "error"
    if db: status = "ok"
    return {
        "database": status
    }

@app.get("/static/{fname:path}.{ext:static}")
async def get(fname: str, ext: str):
    return FileResponse(f'static/{fname}.{ext}')

if __name__ == "__main__":
    serve()
