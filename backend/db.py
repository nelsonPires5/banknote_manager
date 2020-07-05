import sqlite3

class Connect():
    """Fazer o gerenciamento da conexão com o banco de dados"""

    def __init__(self, db_name):
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            print("Banco:", db_name)
            self.cursor.execute('SELECT SQLITE_VERSION()')
            self.data = self.cursor.fetchone()
            print("SQLite version: %s" % self.data)
        except sqlite3.Error:
            print("Erro ao abrir banco.")

    def commit_db():
        if self.conn:
            self.conn.commit()

    def close_db():
        if self.conn:
            self.conn.close()
            print("Conexão fechada!")
