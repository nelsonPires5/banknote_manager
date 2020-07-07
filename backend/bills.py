from backend.db import Connect
from datetime import datetime

class Client():
    """Client interface"""
    def __init__(
        self,
        cpf_cnpj: int,
        created_at: datetime,
        updated_at: datetime,
        full_name: str,
        company_name: str,
        address: str,
        address_number: str,
        district: str,
        city: str,
        phone_number: str = None,
        notes: str = None
    ) -> None:
        self.cpf_cnpj = cpf_cnpj
        self.created_at = created_at
        self.updated_at = updated_at
        self.full_name = full_name
        self.company_name = company_name
        self.address = address
        self.address_number = address_number
        self.district = district
        self.city = city
        self.phone_number = phone_number
        self.notes = notes
        self.conn = Connect('primary.db')

    def create(self):
        """Create client in database"""
        pass