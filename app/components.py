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

def page_content(content):
    return (
        header(),
        content,
        footer()
    )

