from backend.db import Connect
from sqlalchemy import update, delete, select


class Client():
    """Client main class"""
    def __init__(
        self,
        db_connection: Connect,
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
        self.engine = db_connection.engine
        self.clients_table = db_connection.clients_table
        self.cpf_cnpj = cpf_cnpj
        self.full_name = full_name
        self.address = address
        self.address_number = address_number
        self.district = district
        self.city = city
        self.company_name = company_name
        self.phone_number = phone_number
        self.notes = notes

    def create(self) -> None:
        """Create client in the database"""
        conn = self.engine.connect()
        insert = self.clients_table.insert()
        new_client = insert.values(
            cpf_cnpj=self.cpf_cnpj,
            full_name=self.full_name,
            company_name=self.company_name,
            address=self.address,
            address_number=self.address_number,
            district=self.district,
            city=self.city,
            phone_number=self.phone_number,
            notes=self.notes
        )
        conn.execute(new_client)
        conn.close()

    def read_all(self):
        """Read client database"""
        sele = select([self.clients_table])
        return sele.execute()

    def update(self, cpf_cnpj: int, column_and_change: dict) -> None:
        """Update an specific client"""
        conn = self.engine.connect()
        updt = update(self.clients_table) \
            .where(self.clients_table.c.cpf_cpnj == cpf_cnpj)
        # example updt = updt.values(nome='qualquercoisa')
        conn.execute(updt)

    def delete_client(self, cpf_cnpj: int) -> None:
        """Delete an specific client"""
        conn = self.engine.connect()
        dele = delete(self.clients_table) \
            .where(self.clients_table.c.cpf_cpnj == cpf_cnpj)
        conn.execute(dele)
