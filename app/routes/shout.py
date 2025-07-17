from fasthtml.common import *

import config
from components import page_content as page
from models.shout import shout as shout_model
from pages.shout import shout as shout_page

shout_app = FastHTML(prefix="/shout")

@shout_app.get("/")
def shout_index():
    return page(
        config.APP_NAME,
        Container(
            H3("To use this, pass an argument to the endpoint.")
        )
    )

@shout_app.get("/{name}")
def get_name(name: str):
    upper = shout_model(name)
    return page(
        config.APP_NAME,
        Container(
            P(B(Em(upper)))
        )
    )
