import db.database as database
from routes.base import RouteApp

health_app = RouteApp()

@health_app.get("/")
async def get_health():
    db = database.db
    status = "error"
    if db:
        status = "ok"
    return {"database": status}
