from fasthtml.common import (
    Container, Card, Code, Div, Details,
    H2, Li, Ol, P, Summary, Ul,
)


def head():
    return Div(H2("uv + FastHTML = ❤️"))


def about_card():
    return Details(
        Summary("What is this?", role="button"),
        Card(
            P(
                "This is a template aimed at going from Zero to One in a ",
                "very short span of time. Most things should be set up for ",
                "you, so you don't need to worry about project structure or ",
                "testing methods.",
            ),
            P("All you need to do is clone this repository and build!"),
        ),
    )


def examples_card():
    return Details(
        Summary("What examples are included?", role="button"),
        Card(
            Ul(
                Li("Create/Read from a database"),
                Li("Database migrations"),
                Li("Using HTMX"),
                Li("Users and administration"),
                Li("Automated testing and CI using GitHub Actions"),
            )
        ),
    )


def how_to_use_card():
    return Details(
        Summary("How do I use it?", role="button"),
        Card(
            Ol(
                Li("Clone this repository;"),
                Li("Run ", Code("./run restore"), ";"),
                Li("Re-initialise repository;"),
                Li("Build your app and have fun!"),
            )
        ),
    )


def home():
    return Container(head(), about_card(), examples_card(), how_to_use_card())
