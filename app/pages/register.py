from fasthtml.common import (
    A, Card, Container, Div, H2, Hr,
    P
)

from components import login_form


def head():
    return Div(H2("Sign Up"))


def register():
    return Container(
        Card(
            head(),
            login_form("Sign Up", "/auth/register", confirm=True),
            Hr(),
            P("Already have an account? ", A("Log in", href="/auth/login"), "."),
        )
    )
