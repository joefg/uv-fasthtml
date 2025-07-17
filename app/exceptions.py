from fasthtml.common import *

from components import page_content as page
import config

def not_found(request, exception):
    error = Container(
        H2("404: Page Not Found"),
        P(f"Sorry, the page '{request.url.path}' doesn't exist."),
        A("Go home", href="/")
    )
    return page(
        config.APP_NAME,
        error
    )

def internal_error(request, exception):
    error = Container(
        H2("500: Internal Error"),
        P("Oops, something went wrong."),
        A("Go Home", href="/")
    )
    return page(
        config.APP_NAME,
        error
    )

handlers = {
    404: not_found,
    500: internal_error
}
