from fasthtml.common import *


def users_blurb():
    return Nav(
        Ul(Li(A("Administration")), Li(A("Users", href="#users-table"))),
        aria_label="breadcrumb",
    )


def users_table(users):
    users_rows = [
        Tr(
            Td(user.id),
            Td(user.gh_login),
            Td("Yes" if user.is_active else "No"),
            Td(A("More details", href="/admin/user/" + str(user.id), role="button")),
        )
        for user in users
    ] if users else []
    return Table(
        Thead(
            Tr(
                Th("ID"),
                Th("GitHub login"),
                Th("Active?"),
            )
        ),
        Tbody(*users_rows),
        id="users-table",
    )


def user_blurb(gh_login):
    return Nav(
        Ul(
            Li(A("Administration", href="/admin/")),
            Li(A("Users", href="/admin#users-table")),
            Li(gh_login),
        ),
        aria_label="breadcrumb",
    )


def user_card(user, hide_operations=False):
    is_active = bool(user.is_active)
    is_admin = bool(user.is_admin)
    details = (
        H3(user.gh_login),
        Table(
            Tr(Td("ID"), Td(str(user.id))),
            Tr(Td("Creation date"), Td(user.creation_date)),
            Tr(Td("Last login"), Td(user.last_login)),
            Tr(Td("Active"), Td("Yes" if is_active else "No")),
            Tr(Td("Admin"), Td("Yes" if is_admin else "No")),
        ),
    )
    operations = (
        H3("Options"),
        P(Em("Each operation is logged.")),
        Div(
            Button(
                "Deactivate user" if is_active else "Activate user",
                hx_post=f"/admin/user/{user.id}/"
                + ("deactivate" if is_active else "activate"),
                hx_swap="outerHTML",
                hx_target="#user-card",
            ),
            Button(
                "Revoke admin" if is_admin else "Grant admin",
                hx_post=f"/admin/user/{user.id}/"
                + ("revoke" if is_admin else "grant")
                + "-admin",
                hx_swap="outerHTML",
                hx_target="#user-card",
            ),
            cls="grid",
        ),
    )
    return Card(details, None if hide_operations else operations, id="user-card")

def search_box():
    return Div(
        H3("Search"),
        Input(
            hx_post="/admin/users", hx_target="#users-table",
            hx_trigger="input changed delay:500ms, search",
            type="search", name="query",
            placeholder="Start typing GitHub username to search users..."
        )
    )

def admin_page():
    return Container(users_blurb(), search_box(), users_table(None))


def user_page(user, hide_operations=False):
    return Container(user_blurb(user.gh_login), user_card(user, hide_operations))
