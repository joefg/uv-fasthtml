from fasthtml.common import *

import models.shout as shout_model

def shout(text):
    shouted = shout_model.shout(text)
    return Container(
        P(B(Em(shouted)))
    )
