CREATE TABLE bills (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        created_at DATE NOT NULL,
        cpf_cnpj INTEGER NOT NULL,
        amount FLOAT NOT NULL,
        installment INTEGER NOT NULL,
        amount_installment FLOAT NOT NULL
);
