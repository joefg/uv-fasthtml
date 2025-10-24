from fasthtml.common import (
    Card, Container, H2, P
)


def head():
    return H2("Log In")


def login(login_forms=[]):
    return Container(
        Card(
            head(),
            *login_forms
        )
    )


def account_deactivated():
    return Container(
        Card(
            H2("Account deactivated"),
            P("Please contact support.")
        )
    )
