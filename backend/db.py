import sqlite3

class Connect():
    """Manage connection with database"""
    def __init__(self, db_name):
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            print("Database name:", db_name)
            self.cursor.execute('SELECT SQLITE_VERSION()')
            self.data = self.cursor.fetchone()
            print("SQLite version: %s" % self.data)
            self._initialize_db('backend/schemas/clients.sql')
            self._initialize_db('backend/schemas/bills.sql')
        except sqlite3.Error as e:
            print(f"Error open database \n {e}")

    def _initialize_db(self, script_path: str):
        """Execute queries that are into files"""
        with open(script_path, 'rt') as f:
            schema = f.read()
            self.cursor.executescript(schema)

    def commit_db(self):
        """Save into database"""
        if self.conn:
            self.conn.commit()

    def close_db(self):
        """Close connection with database"""
        if self.conn:
            self.conn.close()
            print("Connection close")
    
    