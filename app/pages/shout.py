from fasthtml.common import (
    B, Container, Em, H3, P
)

import models.shout as shout_model

def shout_index():
    return Container(
        H3("To use this, pass an argument to the endpoint.")
    )

def shout(text):
    shouted = shout_model.shout(text)
    return Container(
        P(B(Em(shouted)))
    )
