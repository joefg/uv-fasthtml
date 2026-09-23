from json import dumps

from fasthtml.common import *

from components.daisy import DyHeader, DyFooter

from auth.utils import get_current_user, is_authenticated, is_admin
import config


def header(current_page="/", title=None, links=None):
    links_li = []
    if links: links_li = [Li(link) for link in links]
    left = A(Strong(title or config.APP_NAME), href="/")
    right = Ul(*links_li) if links_li else None
    return DyHeader(left, right)


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
    nav = Small(f"{footer_text}")
    return DyFooter(nav, *links_li)


def login_with(label_text, target):
    return A(label_text, href=target)


def meta_headers(headers):
    return [
        Meta(name=header[0], content=header[1])
        for header in headers
    ]


def link_headers(headers):
    return [
        Link(rel=header[0], href=header[1])
        for header in headers
    ]


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

    csrf = session.get('csrf')
    hx_headers={"X-CSRF-TOKEN": csrf} if csrf else {}

    head = Head(
        Title(title),
        *meta_headers([
            ("viewport", "width=device-width,initial_scale=1.0"),
            ("description", config.APP_DESCRIPTION)
        ]),
        *link_headers([
            ("stylesheet", "https://cdn.jsdelivr.net/npm/daisyui@5"),
            #("stylesheet", "/static/styles.css")
        ]),
        Script(src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"),
        Script(src="https://cdn.jsdelivr.net/npm/htmx.org@latest/dist/htmx.min.js"),
    )
    body = Body(
        header(title=title, links=links_li),
        content,
        footer(),
        cls="bg-base-100 text-base-content min-h-screen p-8"
    )
    return Html(head, body, hx_headers=dumps(hx_headers))
