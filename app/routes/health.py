from fasthtml import APIRouter

import db.database as database

health_app = APIRouter(prefix="/health")

@health_app.get("/")
async def get_health():
    db = database.db
    status = "error"
    if db:
        status = "ok"
    return {"database": status}
