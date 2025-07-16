from fasthtml.common import *

def header(current_page="/", links=None):
    links_li = []
    if links: links_li = [(Li(A(link[0], href=str(link[1])))) for link in links]
    nav = Nav(
        Ul(
            Li(A('Home', href='/')),
            *links_li
        )
    )
    return (
        Header(
            Hgroup(
                H1('uv-fasthtml'),
                P('A FastHTML template using UV'),
                nav
            ),
            cls="container"
        )
    )

def footer():
    year = 2025
    return (
        Footer(
            Small(
                f"©{year}, all rights reserved."
            ),
            cls="container"
        )
    )

def page_content(title, content):
    head = Head(
        Title(title),
        Meta(name="viewport", content="width=device-width,initial_scale=1.0"),
        Meta(name="description", content=f"{title} - Built with FastHTML"),
        Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css")
    )
    body = Body(
        header(),
        content,
        footer()
    )
    return Html(
        head,
        body
    )
