from fasthtml.common import FastHTML, FileResponse

import db.database as database
from exceptions import handlers as exception_handlers

health_app = FastHTML(
    exception_handlers=exception_handlers
)

@health_app.get("/")
async def get_health():
    db = database.db
    status = "error"
    if db: status = "ok"
    return {
        "database": status
    }