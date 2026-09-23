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

def DyHeader(left: None, right: None):
    return Div(
        Div(left, cls="flex-1"),
        Div(right, cls="flex-none"),
        cls="navbar bg-base-200 rounded-box"
    )

def DyFooter(*children):
    return Div(cls="footer footer-center p-10 bg-base-200 rounded-box text-base-content")(*children)

def DySection(title, *children):
    return Div(cls="mb-8")(
        H2(cls="text-2xl font-bold mb-4")(title),
        Div(cls="flex flex-wrap gap-4")(*children),
    )

def DyContainer(*children): return Div(cls="bg-base-100 text-base-content min-h-screen p-8")(*children)

def DyCard(*children):
    return Div(
        Figure(),
        cls="card w-64 bg-base-100 shadow-x1"
    )
    return Div(cls="bg-base-100 text-base-content min-h-screen p-8")(*children)

def DyButton(size: None, modifier: None, state: None, text):
    classes="btn "
    if size: classes += f"btn-{size} "
    if modifier: classes += f"btn-{modifier} "
    if state: classes += f"btn-{btn-state} "
    return Button(text, cls=classes)
