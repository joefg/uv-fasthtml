from fasthtml.common import H2, P
from fasthtml.pico import Container, Card


def head():
    return H2("Log In")


def login(login_forms=[]):
    return Container(
        Card(
            head(),
            P(
                *login_forms,
                cls="grid"
            )
        )
    )


def account_deactivated():
    return Container(
        Card(
            H2("Account deactivated"),
            P("Please contact support.")
        )
    )
