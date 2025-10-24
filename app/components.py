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
        Ul(
            Li(A(Strong(title or config.APP_NAME), href="/")),
            Li("A FastHTML template using UV"),
        ),
        Ul(*links_li),
    )
    return Header(nav, cls="container")


def user_dropdown(user_name, links=None):
    return Details(
        Summary(user_name),
        Ul(
            *[Li(link) for link in links] if links else [],
            Li(A("Logout", href="/auth/logout")),
        ),
        cls="dropdown",
    )


def footer(links=None):
    footer_text = config.FOOTER_TEXT or "uv-fasthtml"
    links_li = []
    if links:
        links_li = [Li(link) for link in links]
    nav = Nav(Small(f"{footer_text}"), *links_li)
    return Footer(nav, cls="container")


def login_with(label_text, target):
    return A(label_text, href=target)


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
            href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css",
        ),
        Link(
            rel="stylesheet",
            href="/static/styles.css"
        ),
        Script(src="https://cdn.jsdelivr.net/npm/htmx.org@2.0.6/dist/htmx.min.js"),
    )
    body = Body(header(title=title, links=links_li), content, footer())
    return Html(head, body)
