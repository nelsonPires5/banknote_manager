CREATE TABLE clientes (
        cpf_cnpj INTEGER NOT NULL PRIMARY KEY,
        created_at DATE NOT NULL,
        updated_at DATE NOT NULL,
        full_name TEXT NOT NULL,
        company_name TEXT NOT NULL,
        address TEXT NOT NULL,
        address_number TEXT NOT NULL,
        district TEXT NOT NULL,
        city TEXT NOT NULL,
        phone TEXT,
        notes TEXT,
);
