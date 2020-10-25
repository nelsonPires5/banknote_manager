import uuid
from datetime import datetime
from sqlalchemy import Column, Table, Integer, DateTime, Float, Text


class Order:

    def __init__(self, metadata) -> None:
        self.metadata = metadata

    def template(self) -> Table:
        return Table(
            'orders',
            self.metadata,
            Column(
                'id',
                Text,
                default=str(uuid.uuid4().hex),
                primary_key=True
            ),
            Column('cpf_cnpj', Text, nullable=False),
            Column('created_at', DateTime, default=datetime.now),
            Column(
                'updated_at',
                DateTime,
                default=datetime.now,
                onupdate=datetime.now
            ),
            Column('amount', Float, nullable=False),
            Column('installments', Integer, nullable=False),
            Column('amount_installments', Float, nullable=False),
            Column('status', Text, nullable=False)
        )
