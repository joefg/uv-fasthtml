from fasthtml.common import (
    Div, Details, Code, H2, Li, Ol, P, Summary, Ul,
)


def head():
    return Div(H2("uv + FastHTML = ❤️"))


def about_card():
    return Div(
        Div(
            Summary("What is this?", role="button"),
            cls="card-header-title",
        ),
        Div(
            P(
                "This is a template aimed at going from Zero to One in a ",
                "very short span of time. Most things should be set up for ",
                "you, so you don't need to worry about project structure or ",
                "testing methods.",
            ),
            P("All you need to do is clone this repository and build!"),
            cls="card-content",
        ),
        cls="card",
    )


def examples_card():
    return Div(
        Div(
            Summary("What examples are included?", role="button"),
            cls="card-header-title",
        ),
        Div(
            Ul(
                Li("Create/Read from a database"),
                Li("Database migrations"),
                Li("Using HTMX"),
                Li("Users and administration"),
                Li("Automated testing and CI using GitHub Actions"),
            ),
            cls="card-content",
        ),
        cls="card",
    )


def how_to_use_card():
    return Div(
        Div(
            Summary("How do I use it?", role="button"),
            cls="card-header-title",
        ),
        Div(
            Ol(
                Li("Clone this repository;"),
                Li("Run ", Code("./run restore"), ";"),
                Li("Re-initialise repository;"),
                Li("Build your app and have fun!"),
            ),
            cls="card-content",
        ),
        cls="card",
    )


def home():
    return Div(
        head(),
        Div(
            Div(about_card(), cls="column"),
            Div(examples_card(), cls="column"),
            Div(how_to_use_card(), cls="column"),
            cls="columns",
        ),
        cls="container",
    )
