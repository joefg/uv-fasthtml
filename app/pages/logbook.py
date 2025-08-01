from fasthtml.common import (
    Container, Div, H3, Fieldset, Form, Input, P, Table, Tbody, Thead, Td, Th, Tr
)

import models.logbook as logbook_model

def header():
    return Div(
        H3("Logbook")
    )


def log_form():
    return Form(
        Fieldset(
            Input(
                autocomplete="off",
                name="content",
                placeholder="Text here"
            ),
            Input(
                type="submit",
                value="Add to logbook"
            ),
            role="group"
        ),
        hx_post="/logbook/submit",
        hx_target="#log-table"
    )

def log_error():
    return P("Error")

def log_table():
    logs = logbook_model.get_all_logs()
    logs_rows = [
        Tr(
            Td(log.id),
            Td(log.content),
            Td(log.created_at),
            Td(log.user_email)
        ) for log in logs
    ]
    return Table(
        Thead(
            Tr(
                Th('ID'),
                Th('Content'),
                Th('Date'),
                Th('By')
            )
        ),
        Tbody(
            *logs_rows
        ),
        id="log-table"
    )


def view_logbook():
    return Container(
        header(),
        log_table()
    )


def add_logbook():
    return Container(
        header(),
        log_form(),
        log_table()
    )
