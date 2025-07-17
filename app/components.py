from fasthtml.common import (
    A, Body, Footer, Head, Header, Html, Li, Link,
    Meta, Nav, Script, Strong, Title, Ul, Small
)

def header(current_page="/", title="uv-fasthtml", links=None):
    links_li = []
    if links: links_li = [(Li(A(link[0], href=str(link[1])))) for link in links]
    nav = Nav(
        Ul(
            Li(Strong(title)),
            Li('A FastHTML template using UV')
        ),
        Ul(
            Li(A('Home', href='/')),
            *links_li
        )
    )
    return Header(
        nav,
        cls="container"
    )

def footer():
    year = 2025
    return Footer(
        Small(
            f"©{year}, all rights reserved."
        ),
        cls="container"
    )

def page_content(title, content):
    links = [
        ('Logbook', '/logbook')
    ]
    head = Head(
        Title(title),
        Meta(name="viewport", content="width=device-width,initial_scale=1.0"),
        Meta(name="description", content=f"{title} - Built with FastHTML"),
        Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css"),
        Script(src="https://cdn.jsdelivr.net/npm/htmx.org@2.0.6/dist/htmx.min.js")
    )
    body = Body(
        header(title=title, links=links),
        content,
        footer()
    )
    return Html(
        head,
        body
    )
