import io
import sqlite3
from sqlalchemy import create_engine, MetaData
from backend.template.database.client import Client
from backend.template.database.order import Order
from backend.template.database.transaction import Transaction


class Connect():
    """Manage connection with database"""
    def __init__(self, db_name: str) -> None:
        self.db_name = db_name
        self.db_path = 'sqlite:///' + self.db_name
        self.engine = create_engine(self.db_path)
        self.metadata = MetaData(bind=self.engine)
        self.clients_table = Client(self.metadata).template()
        self.orders_table = Order(self.metadata).template()
        self.transactions_table = Transaction(self.metadata).template()

        self.metadata.create_all()

    def export_db(self, path: str) -> None:
        """Export all tables in the database"""
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        with io.open(path, 'w') as f:
            for linha in self.conn.iterdump():
                f.write('%s\n' % linha)
        self.conn.close()
        print(f'Backup done success! File {path}')

    def import_db(self, path: str) -> None:
        """Restore all tables in the database"""
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        with open(path, 'rt') as f:
            backup = f.read()
            self.cursor.executescript(backup)
        self.conn.close()
        print('Restore done success!')
