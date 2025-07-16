from fasthtml.common import *

def head():
    return Div(
        H2("uv + FastHTML = ❤️")
    )

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

def examples_card():
    return Div(
        Card(
            Ul(
                Li("Create/Read from a database"),
                Li("Database migrations"),
                Li("Using HTMX")
            ),
            header=H3("What examples are included?")
        )
    )

def how_to_use_card():
    return Div(
        Card(
            Ol(
                Li('Clone this repository;'),
                Li('Run ', Code('./run restore;')),
                Li('Re-initialise repository;'),
                Li('Build your app and have fun!')
            ),
            header=H3("How do I use it?")
        )
    )

def home():
    return Container(
        head(),
        about_card(),
        examples_card(),
        how_to_use_card()
    )
