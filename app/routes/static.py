from fasthtml.common import FastHTML, FileResponse

from exceptions import handlers as exception_handlers

static_app = FastHTML(
    exception_handlers=exception_handlers
)

@static_app.get("/{fname:path}.{ext:static}")
async def get(fname: str, ext: str):
    return FileResponse(f'static/{fname}.{ext}')