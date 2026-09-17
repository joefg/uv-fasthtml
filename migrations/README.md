# Database migrations

This uses [alembic](https://alembic.sqlalchemy.org/en/latest/index.html) to
handle migrations, with alembic available to the justfile so it can
be ran in entirety through `just alembic`.

Once you have made your changes in `app/models/models.py`, you can
autogenerate migrations using `just alembic revision --autogenerate`.

The developer is advised to get familiar with the following doc:

<https://alembic.sqlalchemy.org/en/latest/autogenerate.html>.

## When you should use this

- Schema changes
- Mass data updates which don't require nannying

## When you shoudln't

- Alembic can't autogenerate handle changes in column or table name. Ideally
you shouldn't rename either of these things as it should be caught in review.

Out-of-band migrations should be considered very carefully as these are easy
to get lost.

## Conventions

### Filenames

Autogenerate uses the convention `<hash>_<message>.py` Keep this message
brief. If you're adding an index it could be `add_idx_to_table`, such that
you have a filename of `000000_add_idx_to_table.py`.

### Indexes

| Shorthand | Term                |
| --------- | ------------------- |
| ix        | index               |
| uq        | unique constraint   |
| ck        | checking constraint |
| fk        | foreign key         |
| pk        | primary key         |
