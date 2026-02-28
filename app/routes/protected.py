from fasthtml.common import APIRouter, FileResponse

from auth.utils import require_auth

protected_app = APIRouter(prefix="/protected")


@protected_app.get("/{fname:path}.{ext:static}")
@require_auth
async def get(session, fname: str, ext: str):
    return FileResponse(f"protected/{fname}.{ext}")
