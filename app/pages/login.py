from fasthtml.common import (
    Div, H2, P
)


def head():
    return H2("Log In")


def login(login_forms=[]):
    return Div(
        Div(
            head(),
            cls="card-header-title",
        ),
        Div(
            P(
                *login_forms,
                cls="buttons"
            ),
            cls="card-content",
        ),
        cls="card",
    )


def account_deactivated():
    return Div(
        Div(
            H2("Account deactivated"),
            cls="card-header-title",
        ),
        Div(
            P("Please contact support."),
            cls="card-content",
        ),
        cls="card",
    )
