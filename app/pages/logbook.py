from fasthtml.common import (
    Div, H3, Fieldset, Form, Input,
    P, Table, Tbody, Thead, Td, Th,
    Tr
)

import models.logbook as logbook_model


def header():
    return Div(H3("Logbook"))


def log_form():
    return Form(
        Fieldset(
            Div(
                Input(autocomplete="off", name="content", placeholder="Text here", cls="input"),
                Input(type="submit", value="Add to logbook", cls="button is-primary"),
                cls="field has-addons",
            ),
            role="group",
        ),
        hx_post="/logbook/submit",
        hx_target="#log-table",
    )


def log_error():
    return P("Error")


def log_table():
    logs = logbook_model.get_all_logs()
    logs_rows = [
        Tr(Td(log.id), Td(log.content), Td(log.created_at), Td(log.gh_login))
        for log in logs
    ]
    return Table(
        Thead(Tr(Th("ID"), Th("Content"), Th("Date"), Th("By"))),
        Tbody(*logs_rows),
        cls="table is-fullwidth is-striped",
        id="log-table",
    )


def view_logbook():
    return Div(
        header(),
        log_table(),
        cls="container",
    )


def add_logbook():
    return Div(
        header(),
        log_form(),
        log_table(),
        cls="container",
    )
