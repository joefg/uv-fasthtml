from fasthtml.common import (
    A, Button, Div, Em, H3, Nav, Ul, Li, P, Table,
    Th, Td, Tr, Thead, Tbody,
)

import models.users as users_model


def users_blurb():
    return Nav(
        Ul(
            Li(A("Administration", cls="is-active")),
            Li(A("Users", href="#users-table")),
        ),
        cls="breadcrumb",
        aria_label="breadcrumbs",
    )


def users_table():
    users = users_model.get_all_users()
    users_rows = [
        Tr(
            Td(user.id),
            Td(user.gh_login),
            Td("Yes" if user.is_active else "No"),
            Td(A("More details", href="/admin/user/" + str(user.id), role="button")),
        )
        for user in users
    ]
    return Table(
        Thead(
            Tr(
                Th("ID"),
                Th("GitHub login"),
                Th("Active?"),
            )
        ),
        Tbody(*users_rows),
        cls="table is-fullwidth is-striped",
        id="users-table",
    )


def user_blurb(gh_login):
    return Nav(
        Ul(
            Li(A("Administration", href="/admin/")),
            Li(A("Users", href="/admin#users-table")),
            Li(gh_login, cls="is-active"),
        ),
        cls="breadcrumb",
        aria_label="breadcrumbs",
    )


def user_card(user, hide_operations=False):
    is_active = bool(user.is_active)
    is_admin = bool(user.is_admin)
    details = (
        H3(user.gh_login, cls="title is-4"),
        Table(
            Tr(Td("ID"), Td(str(user.id))),
            Tr(Td("Creation date"), Td(user.creation_date)),
            Tr(Td("Last login"), Td(user.last_login)),
            Tr(Td("Active"), Td("Yes" if is_active else "No")),
            Tr(Td("Admin"), Td("Yes" if is_admin else "No")),
            cls="table is-fullwidth",
        ),
    )
    operations = (
        H3("Options", cls="title is-4"),
        P(Em("Each operation is logged.")),
        Div(
            Button(
                "Deactivate user" if is_active else "Activate user",
                hx_post=f"/admin/user/{user.id}/"
                + ("deactivate" if is_active else "activate"),
                hx_swap="outerHTML",
                hx_target="#user-card",
                cls="button is-primary",
            ),
            Button(
                "Revoke admin" if is_admin else "Grant admin",
                hx_post=f"/admin/user/{user.id}/"
                + ("revoke" if is_admin else "grant")
                + "-admin",
                hx_swap="outerHTML",
                hx_target="#user-card",
                cls="button is-info",
            ),
            cls="buttons",
        ),
    )
    return Div(
        Div(details, cls="card-content"),
        Div(operations, cls="card-content") if not hide_operations else None,
        cls="card",
        id="user-card",
    )


def admin_page():
    return Div(
        users_blurb(),
        users_table(),
        cls="container",
    )


def user_page(user, hide_operations=False):
    return Div(
        user_blurb(user.gh_login),
        user_card(user, hide_operations),
        cls="container",
    )
