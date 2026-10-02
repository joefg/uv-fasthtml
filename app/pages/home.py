from fasthtml.common import *
from fasthtml.pico import *

def head():
    return Div(H2("uv + FastHTML = ❤️"))


def about_card():
    return Article(
        Header(B("What is this?")),
        P(
            "This is a template aimed at going from Zero to One in a ",
            "very short span of time. Most things should be set up for ",
            "you, so you don't need to worry about project structure or ",
            "testing methods.",
        ),
        P("All you need to do is clone this repository and build!"),
    )


def examples_card():
    return Article(
        Header(B("What's included?")),
        Ul(
            Li("CRUD to/from a database"),
            Li("Database administration"),
            Li("Using HTMX"),
            Li("Automated testing and CI using GitHub Actions"),
        ),
        style="height: 350px;"
    )


def how_to_use_card():
    return Article(
        Header(B("How do I use it?")),
        Ol(
            Li("Clone this repository;"),
            Li("Run ", Code("just restore"), ";"),
            Li("Re-initialise repository;"),
            Li("Build your app and have fun!"),
        ),
        style="height: 350px;"
    )


def home():
    return Container(
        head(),
        about_card(),
        Grid(examples_card(), how_to_use_card())
    )
