import uuid
from datetime import datetime
from sqlalchemy import Column, Table, Integer, DateTime, Float, Text


class Transaction:

    def __init__(self, metadata) -> None:
        self.metadata = metadata

    def template(self) -> Table:
        return Table(
            'transactions',
            self.metadata,
            Column('id', Text, default=str(uuid.uuid4().hex), primary_key=True),
            Column('order_id', Text, nullable=False),
            Column('cpf_cnpj', Text, nullable=False),
            Column('created_at', DateTime, default=datetime.now),
            Column('updated_at', DateTime, default=datetime.now, onupdate=datetime.now),
            Column('installment', Integer, nullable=False),
            Column('amount', Float, nullable=False),
            Column('expiration_date', DateTime, nullable=False),
            Column('payment_method', Text, default='promissory_note'),
            Column('status', Text, nullable=False)
        )
