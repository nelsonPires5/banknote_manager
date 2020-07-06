import sqlite3
import io
from datetime import datetime
from sqlalchemy import (
    create_engine, MetaData, Column, Table, Integer, DateTime, Float,
    BigInteger, Text
)


class Connect():
    """Manage connection with database"""
    def __init__(self, db_name: str) -> None:
        self.db_name = db_name
        self.db_path = 'sqlite:///' + self.db_name
        self.engine = create_engine(self.db_path)
        self.metadata = MetaData(bind=self.engine)

        Table(
            'clients',
            self.metadata,
            Column('cpf_cnpj', BigInteger, nullable=False, primary_key=True),
            Column('created_at', DateTime, default=datetime.now),
            Column(
                'updated_at',
                DateTime,
                default=datetime.now,
                onupdate=datetime.now
            ),
            Column('full_name', Text, nullable=False),
            Column('company_name', Text),
            Column('address', Text, nullable=False),
            Column('address_number', Text, nullable=False),
            Column('district', Text, nullable=False),
            Column('city', Text, nullable=False),
            Column('phone_number', Text),
            Column('notes', Text)
        )

        Table(
           'bills',
           self.metadata,
           Column('id', Integer, nullable=False, primary_key=True),
           Column('created_at', DateTime, default=datetime.now),
           Column('cpf_cnpj', BigInteger, nullable=False),
           Column('amount', Float, nullable=False),
           Column('installments', Integer, nullable=False),
           Column('amount_installments', Float, nullable=False)
        )

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
