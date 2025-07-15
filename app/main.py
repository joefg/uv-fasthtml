from fasthtml.common import *

from components import page_content as page

from models.shout import shout as shout_model

from pages.home import home as home_page
from pages.shout import shout as shout_page

app, route = fast_app()

@route("/")
def home():
    return page(
        "uv-fasthtml",
        home_page()
    )

@route("/shout/{name}")
def get_name(name: str):
    return page(
        "uv-fasthtml",
        shout_page(name)
    )


@route("/{path:path}")
def not_found(path: str):
    error = Div(
        H2("404: Page Not Found"),
        P(f"Sorry, the page '/{path}' doesn't exist."),
        A("Go home", href="/"),
        cls="container"
    )
    return page(
        "404: Page Not Found",
        error
    )

if __name__ == "__main__":
    serve()
