from fasthtml.common import (
    A, Card, Container, Div, H2, Hr,
    P
)

from components import login_form


def head():
    return Div(H2("Log In"))


def login():
    return Container(
        Card(
            head(),
            login_form("Log in", "/auth/login"),
            Hr(),
            P("Don't have an account? ", A("Sign up", href="/auth/register"), "."),
        )
    )
