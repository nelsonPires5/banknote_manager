from backend.db import Connect

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
        self.cpf_cnpj = cpf_cpnj
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
        self.conn = self.engine.connect()
        insert = self.clients_table.insert()
        new_client = insert.values(
            cpf_cnpj = self.cpf_cnpj,
            full_name = self.full_name,
            company_name = self.company_name,
            address = self.address,
            address_number = self.address_number,
            district = self.district,
            city = self.city,
            phone_number = self.phone_number,
            notes = self.notes
        )
        self.conn.execute(new_client)
        self.conn.close()
