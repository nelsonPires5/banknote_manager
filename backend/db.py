import sqlite3
import io

class Connect():
    """Manage connection with database"""
    def __init__(self, db_name: str) -> None:
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

    def _initialize_db(self, script_path: str) -> None:
        """Execute queries that are into files"""
        with open(script_path, 'rt') as f:
            schema = f.read()
            self.cursor.executescript(schema)

    def commit_db(self) -> None:
        """Save into database"""
        if self.conn:
            self.conn.commit()

    def close_db(self) -> None:
        """Close connection with database"""
        if self.conn:
            self.conn.close()
            print("Connection close")
    
    def export_db(self, path: str) -> None:
        """Export all tables in the database"""
        with io.open(path, 'w') as f:
            for linha in self.conn.iterdump():
                f.write('%s\n' % linha)

        print(f'Backup done success! File {path}')

    def import_db(self, path: str) -> None:
        """Restore all tables in the database"""
        with open(path, 'rt') as f:
            backup = f.read()
            self.cursor.executescript(backup)

        print(f'Restore done success!')