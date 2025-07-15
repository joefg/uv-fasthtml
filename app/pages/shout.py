from fasthtml.common import *

import models.shout as shout_model

def shout(text):
    shouted = shout_model.shout(text)
    return Div(
        P(B(Em(shouted))),
        cls="container"
    )
