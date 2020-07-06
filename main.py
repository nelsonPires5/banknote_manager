from backend.db import Connect

if __name__ == "__main__":
    db_conn = Connect('primary.db')
    # db_conn.export_db('backup.sql')
    # db_conn.import_db('backup.sql')
    # db_conn = Connect('primary.db')
    # db_conn.export_db('backup.sql')
