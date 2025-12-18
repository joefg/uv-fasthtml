from fasthtml.common import (
    A, Body, Details, Footer, Head, Header, Html, Li, Link, Meta,
    Nav, Script, Small, Summary, Strong,
    Title, Ul,
)

from auth.utils import get_current_user, is_authenticated, is_admin
import config


def header(current_page="/", title=None, links=None):
    links_li = []
    if links:
        links_li = [Li(link) for link in links]
    nav = Nav(
        Div(
            A(Strong(title or config.APP_NAME), href="/", cls="navbar-item"),
            A("A FastHTML template using UV", href="#", cls="navbar-item"),
            cls="navbar-start",
        ),
        Div(*links_li, cls="navbar-end"),
        cls="navbar is-light",
        role="navigation",
        aria_label="main navigation",
    )
    return Header(nav, cls="container")


def user_dropdown(user_name, links=None):
    dropdown_links = []
    if links:
        dropdown_links = [Li(link) for link in links]
    dropdown_links.append(Li(A("Logout", href="/auth/logout")))
    
    return Div(
        Div(
            A(user_name, cls="navbar-link"),
            cls="navbar-item has-dropdown is-hoverable",
        ),
        Div(
            Div(*dropdown_links, cls="navbar-dropdown"),
            cls="navbar-dropdown",
        ),
        cls="navbar-item has-dropdown is-hoverable",
    )


def footer(links=None):
    footer_text = config.FOOTER_TEXT or "uv-fasthtml"
    links_li = []
    if links:
        links_li = [Div(link, cls="navbar-item") for link in links]
    nav = Nav(
        Div(
            Small(f"{footer_text}"),
            *links_li,
            cls="navbar-start",
        ),
        cls="navbar is-light",
        role="navigation",
        aria_label="footer navigation",
    )
    return Footer(nav, cls="container")


def login_with(label_text, target):
    return A(label_text, href=target, cls="button is-primary")


def page_content(title, content, links=None, session=None):
    links_li = links or []
    drop_links = []

    if is_admin(session):
        drop_links = [A("Admin", href="/admin")]
    if is_authenticated(session):
        user = get_current_user(session)
        if user: links_li.append(user_dropdown(user.gh_login, links=drop_links))
    else:
        links_li.append(A("Login", href="/auth/login"))

    head = Head(
        Title(title),
        Meta(name="viewport", content="width=device-width,initial_scale=1.0"),
        Meta(name="description", content=f"{title} - Built with FastHTML"),
        Link(
            rel="stylesheet",
            href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css",
        ),
        Link(
            rel="stylesheet",
            href="/static/styles.css"
        ),
        Script(src="https://cdn.jsdelivr.net/npm/htmx.org@2.0.6/dist/htmx.min.js"),
        Script(src="https://cdn.jsdelivr.net/npm/bulma@0.9.4/js/bulma.min.js"),
    )
    body = Body(
        Div(
            header(title=title, links=links_li),
            Div(content, cls="section"),
            footer(),
            cls="container",
        )
    )
    return Html(head, body)
