from fasthtml.components import *

hdrs=(
    Script(src="https://cdn.tailwindcss.com"),
    Link(
        rel="stylesheet",
        href="https://cdn.jsdelivr.net/npm/daisyui@latest/dist/full.min.css",
        type="text/css",
        attributes={"charset": "UTF-8"},
    ),
)

def DyHeader(left: None, title: None, right: None):
    return Div(
        Div(left, cls="navbar-start"),
        Div(title, cls="navbar-mid"),
        Div(right, cls="navbar-end"),
        cls="navbar bg-base-200 rounded-box glass w-1/2 justify-self-center"
    )

def DyFooter(*children):
    return Footer(
        cls="footer footer-center bg-base-200 rounded-box p-6 text-base-content glass w-1/2"
    )(*children)

def DySection(title, *children):
    return Div(cls="mb-8")(
        H2(cls="text-2xl font-bold mb-4")(title),
        Div(cls="flex flex-wrap gap-4")(*children),
    )

def DyContainer(*children): return Div(cls="bg-base-100 text-base-content p-8")(*children)

def DyCard(*children):
    return Div(
        *children,
        cls="card w-64 bg-base-100 shadow-x1"
    )

def DyButton(size: None, modifier: None, state: None, text):
    classes="btn "
    if size: classes += f"btn-{size} "
    if modifier: classes += f"btn-{modifier} "
    if state: classes += f"btn-{btn-state} "
    return Button(text, cls=classes)
