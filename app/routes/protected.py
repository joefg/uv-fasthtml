from fasthtml.common import FileResponse

from auth.utils import require_auth
from routes.base import route_app

protected_app = route_app


@protected_app.get("/{fname:path}.{ext:static}")
@require_auth
async def get(session, fname: str, ext: str):
    return FileResponse(f"protected/{fname}.{ext}")
