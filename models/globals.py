db_connection = None
def set_db_connection(db):
    global db_connection
    db_connection = db
def get_db_connection():
    return db_connection
