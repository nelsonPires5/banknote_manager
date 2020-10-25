from datetime import datetime
from sqlalchemy import Column, Table, Integer, DateTime, Text


class Client:

    def __init__(self, metadata) -> None:
        self.metadata = metadata

    def template(self) -> Table:
        return Table(
            'clients',
            self.metadata,
            Column('cpf_cnpj', Text, nullable=False, primary_key=True),
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
            Column('address_number', Integer, nullable=False),
            Column('district', Text, nullable=False),
            Column('city', Text, nullable=False),
            Column('phone_number', Text),
            Column('notes', Text)
        )
