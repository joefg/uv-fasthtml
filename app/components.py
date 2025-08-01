from fasthtml.common import (
    A, Body, Button, Details, Footer, Form, Head, Header, Html,
    Input, Li, Link, Meta, Nav, Script, Small, Span, Summary,
    Strong, Title, Ul
)

from auth.utils import is_authenticated, is_admin
import config

def header(current_page="/", title=None, links=None):
    links_li = []
    if links: links_li = [Li(link) for link in links]
    nav = Nav(
        Ul(
            Li(A(Strong(title or config.APP_NAME), href="/")),
            Li('A FastHTML template using UV')
        ),
        Ul(
            *links_li
        )
    )
    return Header(
        nav,
        cls="container"
    )

def user_dropdown(user_email, links=None):
    return Details(
        Summary(user_email),
        Ul(
            *[Li(link) for link in links] if links else [],
            Li(A("Logout", href="/auth/logout")),
        ),
        cls="dropdown"
    )

def footer(links=None):
    footer_text = config.FOOTER_TEXT or "uv-fasthtml"
    links_li = []
    if links: links_li = [Li(link) for link in links]
    nav = Nav(
        Small(f"{footer_text}"),
        *links_li
    )
    return Footer(
        nav,
        cls="container"
    )

def login_form(btn_text, target, confirm=False):
    return Form(
        Input(id="email", type="email", placeholder="Email", required=True),
        Input(id="password", type="password", placeholder="Password", required=True),
        Input(id="confirm_password", type="password", placeholder="Confirm Password", required=True) if confirm else None,
        Button(btn_text, type="submit"),
        Span(id="error", style="color:red"),
        hx_post=target,
        hx_target="#error",
    )

def page_content(title, content, links=None, session=None):
    links_li = links or []

    drop_links = []
    if is_admin(session): drop_links = [A("Admin", href="/admin")]
    if is_authenticated(session):
        links_li.append(user_dropdown(session.get("email"), links=drop_links))
    else:
        links_li.append(A('Login', href='/auth/login'))

    head = Head(
        Title(title),
        Meta(name="viewport", content="width=device-width,initial_scale=1.0"),
        Meta(name="description", content=f"{title} - Built with FastHTML"),
        Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css"),
        Script(src="https://cdn.jsdelivr.net/npm/htmx.org@2.0.6/dist/htmx.min.js")
    )
    body = Body(
        header(title=title, links=links_li),
        content,
        footer()
    )
    return Html(
        head,
        body
    )
