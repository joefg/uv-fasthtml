from fasthtml.common import APIRouter, FileResponse


static_app = APIRouter(prefix="/static")


@static_app.get("/{fname:path}.{ext:static}")
async def get(fname: str, ext: str):
    return FileResponse(f"static/{fname}.{ext}")
