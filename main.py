from backend.db import Connect
from backend.clients import Client

if __name__ == "__main__":
    db_conn = Connect('primary.db')
    cl = Client(db_conn)
    cl.create(        
        '22689495618',
        'Nelson Pires',
        'Rua cristiano viana',
        '605',
        'Pinheiros',
        'São Paulo'
    )
    cl.create(        
        '22689495610',
        'Carolina Costa',
        'Rua cristiano viana',
        '400',
        'Universidade',
        'Uberaba'
    )
    print(cl.read_all())
    print(cl.read_by_name('pires'))
    # db_conn.export_db('backup.sql')
    # db_conn.import_db('backup.sql')