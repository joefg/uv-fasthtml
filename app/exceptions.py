from fasthtml.common import (
    A, Container, H2, P
)

import config
from components import page_content as page

def _error_page(header,text):
    error = Container(
        H2(header),
        P(text),
        A("Go home", href="/")
    )
    return page(
        config.APP_NAME,
        error
    )

def forbidden(request, exception):
    return _error_page(
        "403: Forbidden",
        "Permissions insufficient to access resource."
    )

def internal_error(request, exception):
    return _error_page(
        "500: Internal Error",
        "Oops, something went wrong."
    )

def not_found(request, exception):
    return _error_page(
        "404: Page Not Found",
        f"Sorry, the page '{request.url.path}' doesn't exist."
    )

def unauthorised(request, exception):
    return _error_page(
        "401: Unauthorised",
        "Sorry, you are not allowed to access this resource."
    )

handlers = {
    401: unauthorised,
    403: forbidden,
    404: not_found,
    500: internal_error
}
