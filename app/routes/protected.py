from fasthtml.common import FastHTML, FileResponse

from auth.utils import require_auth
from exceptions import handlers as exception_handlers

protected_app = FastHTML(exception_handlers=exception_handlers)


@protected_app.get("/{fname:path}.{ext:static}")
@require_auth
async def get(session, fname: str, ext: str):
    return FileResponse(f"protected/{fname}.{ext}")
