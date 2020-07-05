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
            self._initialize_db('backend/schemas/clients.sql')
            self._initialize_db('backend/schemas/bills.sql')
        except sqlite3.Error:
            print("Erro ao abrir banco.")

    def commit_db(self):
        """Grava no banco de dados"""
        if self.conn:
            self.conn.commit()

    def close_db(self):
        """Fecha conexão com o banco de dados"""
        if self.conn:
            self.conn.close()
            print("Conexão fechada!")
    
    def _initialize_db(self, script_path: str):
        """Roda queries sql de inicialização do db"""
        with open(script_path, 'rt') as f:
            schema = f.read()
            self.cursor.executescript(schema)