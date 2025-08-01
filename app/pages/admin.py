from fasthtml.common import (
    A, Br, Button, Card, Container, Div,
    Em, H3, Nav, Ul, Li, P,
    Table, Th, Td, Tr, Thead, Tbody
)

import models.users as users_model

def users_blurb():
    return Nav(
        Ul(
            Li(A("Administration")),
            Li(A("Users", href="#users-table"))
        ),
        aria_label="breadcrumb"
    )

def users_table():
    users = users_model.get_all_users()
    users_rows = [
        Tr(
            Td(user.id),
            Td(user.email),
            Td("Yes" if user.is_active else "No"),
            Td(A("More details", href="/admin/user/" + str(user.id), role="button"))
        )
        for user in users
    ]
    return Table(
        Thead(
            Tr(
                Th('ID'),
                Th('Email'),
                Th('Active?'),
            )
        ),
        Tbody(
            *users_rows
        ),
        id="users-table"
    )

def user_blurb(user_email):
    return Nav(
        Ul(
            Li(A("Administration", href="/admin/")),
            Li(A("Users", href="/admin#users-table")),
            Li(user_email)
        ),
        aria_label="breadcrumb"
    )

def user_card(user, hide_operations=False):
    is_active = bool(user.is_active)
    is_admin = bool(user.is_admin)
    details = (H3(user.email),
        Table(
            Tr(Td('ID'), Td(str(user.id))),
            Tr(Td('Creation date'), Td(user.creation_date)),
            Tr(Td('Last login'), Td(user.last_login)),
            Tr(Td('Active'), Td("Yes" if is_active else "No")),
            Tr(Td('Admin'), Td("Yes" if is_admin else "No")),
        )
    )
    operations = (H3("Options"),
        P(Em("Each operation is logged.")),
        Div(
            Button(
                "Deactivate user" if is_active else "Activate user",
                hx_post=f"/admin/user/{user.id}/" + ("deactivate" if is_active else "activate"),
                hx_swap="outerHTML",
                hx_target="#user-card"
            ),
            Button(
                "Revoke admin" if is_admin else "Grant admin",
                hx_post=f"/admin/user/{user.id}/" + ("revoke" if is_admin else "grant") + "-admin",
                hx_swap="outerHTML",
                hx_target="#user-card"
            ),
            cls="grid"
        )
    )
    return Card(
        details,
        None if hide_operations else operations,
        id="user-card"
    )

def admin_page():
    return Container(
        users_blurb(),
        users_table()
    )

def user_page(user, hide_operations=False):
    return Container(
        user_blurb(user.email),
        user_card(user, hide_operations)
    )