from fasthtml.common import *

import models.logbook as logbook_model

def header():
    return Div(
        H3("Logbook"),
        P("Add entry to the logbook.")
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
                value="Submit"
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
            Td(log.created_at)
        ) for log in logs
    ]
    return Table(
        Thead(
            Tr(
                Th('ID'),
                Th('Content'),
                Th('Date')
            )
        ),
        Tbody(
            *logs_rows
        ),
        id="log-table"
    )

def logbook():
    return Container(
        header(),
        log_form(),
        log_table()
    )
