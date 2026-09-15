from fasthtml import APIRouter

from models.system import get_db_info

health_app = APIRouter(prefix="/health")

@health_app.get("/")
async def get_health():
    return {"database": "ok" if get_db_info() else "error"}
