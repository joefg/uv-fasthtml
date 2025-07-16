import glob
import logging
import os
import sqlite3
from contextlib import contextmanager

import config

class Database:
    def __init__(self, path=None):
        self.db_path = path or config.DB_PATH

        if not self.db_path:
            self.db_path = "database/database.db"

        self._init_db()
        self._migrate()

    def _init_db(self):
        with self.connect() as connection:
            cursor = connection.cursor()
            cursor.executescript('''
                -- Create schema_history table for migrations.
                create table if not exists schema_history (
                    id integer primary key autoincrement,
                    script text not null,
                    executed_at timestamp not null default current_timestamp
                );

                -- Insert an entry into that table to kick off
                -- the autoincrement
                insert into schema_history(id, script)
                select 0, 'init'
                where not exists (
                    select 1
                    from schema_history
                    where script = 'init'
                );
            '''
            )
            connection.commit()

    def _add_migration(self, schema):
        logging.info(f"Adding {schema}...")
        migration = None
        with open(schema, 'r') as f:
            migration = f.read()

        with self.connect() as connection:
            cursor = connection.cursor()
            cursor.executescript(migration)
            cursor.execute('''
                insert into schema_history (script)
                values (
                    :schema
                );
            ''', (schema,))
            connection.commit()
            logging.info(f"{schema} added successfully.")

    def _migrate(self):
        migrated = ()
        with self.connect() as connection:
            cursor = connection.cursor()
            cursor.execute('''
                select id, script, executed_at
                from schema_history
                order by executed_at;
            ''')
            migrated = set([row['script'] for row in cursor.fetchall()])

        schemas = sorted(glob.glob('app/db/schema/*.sql'))
        for schema in schemas:
            if schema not in migrated:
                self._add_migration(schema)

    @contextmanager
    def connect(self):
        db_dir = os.path.dirname(self.db_path)
        if db_dir: os.makedirs(db_dir, exist_ok=True)

        connection = sqlite3.connect(self.db_path, isolation_level=None)
        connection.execute('pragma journal_mode=wal')
        connection.row_factory = sqlite3.Row

        try:
            yield connection
        finally:
            connection.close()

db = Database()
