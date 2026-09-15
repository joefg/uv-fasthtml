import glob
import logging
import os
from pathlib import Path
import sqlite3
import time
from contextlib import contextmanager

class Database:
    def __init__(self, path=None):
        self.db_path = Path(path) if path else Path("database/database.sqlite3")

    def init_db(self, no_wal=False):
        with self.connect() as connection:
            if no_wal: logging.info("! WAL not enabled.")
            else:
                connection.execute('pragma journal_mode=wal')
                logging.info("• WAL enabled.")
            cursor = connection.cursor()
            cursor.executescript('''
                -- Create migrations history table.
                create table if not exists migrations (
                    id integer primary key autoincrement,
                    script text not null,
                    executed_at timestamp not null default current_timestamp
                );
                create unique index if not exists idx_migrations_id on migrations (id);
                -- Insert an entry into that table to kick off the autoincrement.
                insert into migrations (id, script)
                select 0, 'init'
                where not exists (
                    select 1
                    from migrations
                    where script = 'init'
                );
            '''
            )
            connection.commit()
            connection.close()

    def _add_migration(self, migration, verbose=False, confirm=False):
        logging.info(f"• Adding {migration}...")
        start = time.perf_counter()

        assert Path(migration).exists()
        migration_script = open(migration, 'r').read()

        with self.connect() as connection:
            if verbose:
                logging.info("• Migration:")
                logging.info("\n\n" + migration_script)

            if confirm:
                answer = input("？Confirm execution? y/yes to continue. ")
                if answer.lower() not in ("y", "yes"):
                    logging.info("✗ Migration aborted.")
                    exit(1)

            cursor = connection.cursor()
            cursor.executescript(migration_script)
            cursor.execute('''
                insert into migrations (script)
                values (:migration);
            ''',
                {"migration": migration}
            )
            connection.commit()
            logging.info(f"✓ {migration} added successfully.")

        end = time.perf_counter()
        duration = end - start
        logging.info(f"• Time taken: {duration:.6f} seconds")

    def migrate(self, verbose=False, confirm=False):
        migrated = ()
        with self.connect() as connection:
            cursor = connection.cursor()
            cursor.execute('''
                select id, script, executed_at
                from migrations
                order by executed_at;
            ''')
            migrated = set([row['script'] for row in cursor.fetchall()])

        migrations = sorted(glob.glob('migrations/*.sql'))
        migrations_count = 0
        for migration in migrations:
            if migration not in migrated:
                self._add_migration(migration, verbose, confirm)
                migrations_count += 1
        logging.info(f"• {migrations_count} migrations executed.")

    @contextmanager
    def connect(self):
        db_dir = os.path.dirname(self.db_path)
        if db_dir:
            os.makedirs(db_dir, exist_ok=True)

        connection = sqlite3.connect(self.db_path, isolation_level=None)
        connection.row_factory = sqlite3.Row

        try: yield connection
        finally: connection.close()

def main(args):
    db_path = args['db_path'] or "database/database.sqlite3"
    logging.basicConfig(format="%(message)s", level=logging.INFO)

    verbose = args['verbose']
    confirm = args['confirm']
    no_wal = args['no_wal']

    db = Database(db_path)
    db.init_db(no_wal)
    db.migrate(verbose, confirm)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        prog="sqlite_utils.py",
        description="SQLite database management and migration utility"
    )
    parser.add_argument("db_path", nargs="?", help="Path to use, defaults to database/database.sqlite")
    parser.add_argument("-v", "--verbose", action="store_true", help="Print migrations")
    parser.add_argument("-c", "--confirm", action="store_true", help="Confirm each migration")
    parser.add_argument("--no-wal", action="store_true", help="Disable WAL journaling")
    args = vars(parser.parse_args())

    main(args)
