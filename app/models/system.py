from sqlalchemy.sql import text
from database import connect

def get_db_info():
    ret = None
    with connect() as session:
        statement = text("select * from migrations limit 1;")
        ret = session.execute(statement).one()
    return ret
