from backend.db import Connect
from backend.clients import Client

if __name__ == "__main__":
    db_conn = Connect('primary.db')
    cl = Client(db_conn)
    # cl.create(        
    #     22689495618, # Tem que ser string pq não permite começar com zero
    #     'Nelson Pires',
    #     'Rua cristiano viana',
    #     '605',
    #     'Pinheiros',
    #     'São Paulo'
    # )
    print(cl.read_all())
    # db_conn.export_db('backup.sql')
    # db_conn.import_db('backup.sql')
    # db_conn = Connect('primary.db')
    # db_conn.export_db('backup.sql')
