import db.database

def get_all_logs():
    logs = []
    with db.database.db.connect() as connection:
        cursor = connection.cursor()
        sql = '''
            select id, content, created_at
            from logbook;
        '''
        cursor.execute(sql)
        logs = cursor.fetchall()
    return [dict(zip(row.keys(), row)) for row in logs]

def add_log(log_text):
    if log_text:
        with db.database.db.connect() as connection:
            cursor = connection.cursor()
            sql = '''
                insert into logbook (content)
                values (:content)
            '''
            cursor.execute(sql, (log_text,))
        return True
    else:
        return False
