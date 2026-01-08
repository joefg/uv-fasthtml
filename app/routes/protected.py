from fasthtml.common import FileResponse

from auth.utils import require_auth
from routes.base import RouteApp

protected_app = RouteApp()


@protected_app.get("/{fname:path}.{ext:static}")
@require_auth
async def get(session, fname: str, ext: str):
    return FileResponse(f"protected/{fname}.{ext}")
