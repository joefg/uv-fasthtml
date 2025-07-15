from fasthtml.common import *

import components
from pages.home import home as home_page

app, route = fast_app()

@route("/")
def home():
    return components.page_content(
        home_page()
    )

if __name__ == "__main__":
    serve()
