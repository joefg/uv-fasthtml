import db.database as database
from routes.base import route_app

health_app = route_app()

@health_app.get("/")
async def get_health():
    db = database.db
    status = "error"
    if db:
        status = "ok"
    return {"database": status}
