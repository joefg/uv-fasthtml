from fasthtml.common import *

def about_card():
    return Div(
        Card(
            P('This is a template aimed at going from Zero to One in a ',
              'very short span of time. Most things should be set up for ',
              'you, so you don\'t need to worry about project structure or ',
              'testing methods.'),
            Br(),
            P('All you need to do is clone this repository and build!'),
            header=H3("What is this?")
        )
    )

def home():
    head = Div(
        H2("uv + FastHTML = <3")
    )
    return Div(
        head,
        about_card(),
        cls="container"
    )
