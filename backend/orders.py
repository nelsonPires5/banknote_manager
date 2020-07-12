from datetime import datetime
from backend.db import Connect
from sqlalchemy import update, delete, select
from typing import List


class Order():
    """Order main class"""
    def __init__(
        self,
        db_connection: Connect
    ) -> None:
        self.engine = db_connection.engine
        self.orders_table = db_connection.orders_table
        self.transactions_table = db_connection.transactions_table

    def create(
        self,
        cpf_cnpj: str,
        amount: float,
        installments: str,
        amount_installments: float,
        expiration_dates: List[str],
        date_format: str = '%d/%m/%y',
        payment_method: str = None,
        status: str = None,
    ) -> None:
        """Create orders and transactions in the database"""
        conn = self.engine.connect()
        insert_orders = self.orders_table.insert()
        new_order = insert_orders.values(
            cpf_cnpj=cpf_cnpj,
            amount=amount,
            installments=installments,
            amount_installments=amount_installments,
        )
        res = conn.execute(new_order)

        trans_items = []
        print(res.inserted_primary_key)
        for index, date in enumerate(expiration_dates):
            date = datetime.strptime(date, date_format)
            trans_items.append({
                'order_id': res.inserted_primary_key,
                'cpf_cnpj': cpf_cnpj,
                'installment': index + 1,
                'amount': amount_installments,
                'expiration_date': date,
                'payment_method': payment_method,
                'status': status
            })
        insert_transactions = self.transactions_table.insert()
        conn.execute(insert_transactions, trans_items)
        conn.close()

    def verify_cpf_exists(self, cpf_cnpj: str):
        """Verify if is a cpf that exist in database"""
        pass

    def read_all(self) -> list:
        """Read client database"""
        select_all = select([self.clients_table]).execute()
        return [row for row in select_all] 

    def read_by_name(self, name: str) -> list:
        """Read all clients by name"""
        select_by_name = self.clients_table \
            .select() \
            .where(self.clients_table.c.full_name.like('%' + name + '%')) \
            .execute()
        return [row for row in select_by_name]

    def read_by_cpf(self, cpf_cnpj: str) -> list:
        """Read all clients by cpf_cnpj"""
        select_by_name = self.clients_table \
            .select() \
            .where(self.clients_table.c.cpf_cnpj==cpf_cnpj) \
            .execute()
        return [row for row in select_by_name]

    def update(self, cpf_cnpj: int, column_and_change: dict) -> None:
        """Update an specific client"""
        conn = self.engine.connect()
        updt = update(self.clients_table) \
            .where(self.clients_table.c.cpf_cpnj == cpf_cnpj) \
            .values(column_and_change)
        conn.execute(updt)
        conn.close()

    def delete_client(self, cpf_cnpj: int) -> None:
        """Delete an specific client"""
        conn = self.engine.connect()
        dele = delete(self.clients_table) \
            .where(self.clients_table.c.cpf_cpnj == cpf_cnpj)
        conn.execute(dele)
        conn.close()
