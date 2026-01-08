from fasthtml.common import FileResponse

from routes.base import RouteApp

static_app = RouteApp()


@static_app.get("/{fname:path}.{ext:static}")
async def get(fname: str, ext: str):
    return FileResponse(f"static/{fname}.{ext}")
