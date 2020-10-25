# import pytest
from backend.database.connect import Connect
from backend.database.client import Client


class TestCreate():
    def test_full(self):
        cpf_cnpj = "00011122233"
        full_name = "Cliente 1"
        address = "Rua A"
        address_number = 11
        district = "Bairro B"
        city = "Cidade C"
        company_name = "Loja 1"
        phone_number = "11965231478"
        notes = "Nota sobre o cliente e sua relação com a empresa"

        db_conn = Connect('test.db')
        cl = Client(db_conn)
        cl.create(
            cpf_cnpj=cpf_cnpj,
            full_name=full_name,
            address=address,
            address_number=address_number,
            district=district,
            city=city,
            company_name=company_name,
            phone_number=phone_number,
            notes=notes
        )

    def test_only_necessary(self):
        cpf_cnpj = "99999999999"
        full_name = "Cliente 2"
        address = "Rua B"
        address_number = 12
        district = "Bairro A"
        city = "Cidade C"

        db_conn = Connect('test.db')
        cl = Client(db_conn)
        cl.create(
            cpf_cnpj=cpf_cnpj,
            full_name=full_name,
            address=address,
            address_number=address_number,
            district=district,
            city=city
        )

    def test_not_full(self):
        cpf_cnpj = "00011122233"
        full_name = "Cliente 1"
        address = "Rua A"
        address_number = 11
        district = "Bairro B"

        db_conn = Connect('test.db')
        cl = Client(db_conn)

        flag_error = None
        try:
            cl.create(
                cpf_cnpj=cpf_cnpj,
                full_name=full_name,
                address=address,
                address_number=address_number,
                district=district
            )
        except TypeError:
            flag_error = 1

        if flag_error:
            assert True
        else:
            assert False

    def test_wrong_type(self):
        cpf_cnpj = "00000000000"
        full_name = "Cliente 2"
        address = "Rua B"
        address_number = "11"
        district = "Bairro A"
        city = "Cidade C"

        db_conn = Connect('test.db')
        cl = Client(db_conn)

        flag_error = None
        try:
            cl.create(
                cpf_cnpj=cpf_cnpj,
                full_name=full_name,
                address=address,
                address_number=address_number,
                district=district,
                city=city
            )
        except Exception:
            flag_error = 1

        if flag_error:
            assert True
        else:
            assert False


class TestReadAll():
    def test_full(self):
        pass


class TestReadByName():
    def test_exist(self):
        pass

    def test_not_exist(self):
        pass


class TestReadByCpf():
    def test_exist(self):
        pass

    def test_not_exist(self):
        pass


class TestUpdate():
    def test_exist(self):
        pass

    def test_not_exist(self):
        pass


class TestDeleteClient():
    def test_exist(self):
        pass

    def test_not_exist(self):
        pass
