from dataclasses import dataclass

import db.database

@dataclass
class Log:
    id: int
    content: str
    created_at: str

def get_all_logs() -> list[Log]:
    logs = []
    with db.database.db.connect() as connection:
        cursor = connection.cursor()
        cursor.row_factory = lambda cursor, row: Log(*row)
        sql = '''
            select id, content, created_at
            from logbook;
        '''
        cursor.execute(sql)
        logs = cursor.fetchall()
    return logs

def add_log(log: Log) -> bool:
    if log.content:
        with db.database.db.connect() as connection:
            cursor = connection.cursor()
            sql = '''
                insert into logbook (content)
                values (:content)
            '''
            cursor.execute(sql, (log.content,))
        return True
    else:
        return False
