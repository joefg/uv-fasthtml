from fasthtml.common import FastHTML
from exceptions import handlers as exception_handlers

class RouteApp(FastHTML):
    def __init__(self, **kwargs):
        kwargs['exception_handlers'] = exception_handlers
        super().__init__(**kwargs)

def route_app(**kwargs):
    kwargs['exception_handlers'] = exception_handlers
    return FastHTML(**kwargs)
