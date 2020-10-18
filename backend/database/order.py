from datetime import datetime
from typing import List, Union
from sqlalchemy import update, delete, select
from backend.database.connect import Connect


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
            status='to_capture'
        )
        # status = ['to_capture', 'paid', 'cancelled']
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
        # status = ['paid', 'on_time', 'delayed', 'cancelled']
        insert_transactions = self.transactions_table.insert()
        conn.execute(insert_transactions, trans_items)
        conn.close()

    def cancel(self, order_id: str) -> None:
        conn = self.engine.connect()
        updt = update(self.orders_table) \
            .where(self.orders_table.c.id == order_id) \
            .values({'status': 'cancelled'})
        conn.execute(updt)
        updt = update(self.transactions_table) \
            .where(self.transactions_table.c.order_id == order_id) \
            .values({'status': 'cancelled'})
        conn.execute(updt)
        conn.close()

    def paid(self, order_id: str, installments: List[int]):
        conn = self.engine.connect()

        for installment in installments:
            updt = update(self.transactions_table) \
                .where(self.transactions_table.c.order_id == order_id) \
                .where(self.transactions_table.c.installment == installment) \
                .values({'status': 'paid'})
            conn.execute(updt)

        last_installment = select([self.clients_table]) \
            .where(self.transactions_table.c.order_id == order_id) \
            .order_by(self.transactions_table.c.installment) \
            .execute()
        last_installment = last_installment[-1]

        if last_installment.status == 'paid':
            updt = update(self.orders_table) \
                .where(self.orders_table.c.id == order_id) \
                .values({'status': 'paid'})
            conn.execute(updt)

        conn.close()

    def read_all_orders(self) -> list:
        """Read client database"""
        select_all = select([self.orders_table]).execute()
        return [row for row in select_all]

    def read_orders_by_order_id(self, order_id: str) -> list:
        """Read all clients by name"""
        select_by_name = self.orders_table \
            .select() \
            .where(self.orders_table.c.id == order_id) \
            .execute()
        return [row for row in select_by_name]

    def read_orders_by_cpf(self, cpf_cnpj: str) -> list:
        """Read all clients by cpf_cnpj"""
        select_cpf = self.orders_table \
            .select() \
            .where(self.orders_table.c.cpf_cnpj==cpf_cnpj) \
            .execute()
        return [row for row in select_cpf]
    
    def read_all_transactions(self) -> list:
        """Read client database"""
        select_all = select([self.transactions_table]).execute()
        return [row for row in select_all]

    def read_orders_by_order_id(self, order_id: str) -> list:
        """Read all clients by name"""
        select_by_name = self.transactions_table \
            .select() \
            .where(self.transactions_table.c.order_id == order_id) \
            .execute()
        return [row for row in select_by_name]

    def read_orders_by_cpf(self, cpf_cnpj: str) -> list:
        """Read all clients by cpf_cnpj"""
        select_cpf = self.transactions_table \
            .select() \
            .where(self.transactions_table.c.cpf_cnpj==cpf_cnpj) \
            .execute()
        return [row for row in select_cpf]


