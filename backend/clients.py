from backend.db import Connect
from sqlalchemy import update, delete, select


class Client():
    """Client main class"""
    def __init__(
        self,
        db_connection: Connect
    ) -> None:
        self.engine = db_connection.engine
        self.clients_table = db_connection.clients_table

    def create(
        self,
        cpf_cnpj: int,
        full_name: str,
        address: str,
        address_number: int,
        district: str,
        city: str,
        company_name: str = None,
        phone_number: str = None,
        notes: str = None
    ) -> None:
        """Create client in the database"""
        conn = self.engine.connect()
        insert = self.clients_table.insert()
        new_client = insert.values(
            cpf_cnpj=cpf_cnpj,
            full_name=full_name,
            company_name=company_name,
            address=address,
            address_number=address_number,
            district=district,
            city=city,
            phone_number=phone_number,
            notes=notes
        )
        conn.execute(new_client)
        conn.close()

    def read_all(self) -> list:
        """Read client database"""
        sele = select([self.clients_table])
        return [row for row in sele.execute()] 

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
