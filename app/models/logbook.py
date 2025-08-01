from dataclasses import dataclass

import db.database

@dataclass
class Log:
    id: int
    content: str
    created_at: str
    user_email: int

def get_all_logs() -> list[Log]:
    logs = []
    with db.database.db.connect() as connection:
        cursor = connection.cursor()
        cursor.row_factory = lambda cursor, row: Log(*row)
        sql = '''
            select
                logbook.id,
                logbook.content,
                logbook.created_at,
                users.email as "user_email"
            from logbook
            left join users on (
                logbook.created_by = users.id
            );
        '''
        cursor.execute(sql)
        logs = cursor.fetchall()
    return logs

def add_log(log: str, user_id: int) -> bool:
    if log and user_id:
        with db.database.db.connect() as connection:
            cursor = connection.cursor()
            sql = '''
                insert into logbook (content, created_by)
                values (:content, :created_by);
            '''
            params = {
                'content': log,
                'created_by': user_id
            }
            cursor.execute(sql, params)
        return True
    else:
        return False
