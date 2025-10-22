from fasthtml.common import (
    A, Card, Container, Div, H2, Hr,
    P
)

from components import login_with


def head():
    return H2("Log In")


def login(login_text: str, login_link: str):
    return Container(
        Card(
            head(),
            login_with(login_text, login_link)
        )
    )


def account_deactivated():
    return Container(
        Card(
            H2("Account deactivated"),
            P("Please contact support.")
        )
    )
