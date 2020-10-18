from backend.database.connect import Connect
from backend.database.client import Client
from backend.database.order import Order


if __name__ == "__main__":
    db_conn = Connect('primary.db')
    cl = Client(db_conn)
    # cl.create(        
    #     '22689495618',
    #     'Nelson Pires',
    #     'Rua cristiano viana',
    #     '605',
    #     'Pinheiros',
    #     'São Paulo'
    # )
    # cl.create(        
    #     '22689495610',
    #     'Carolina Costa',
    #     'Rua cristiano viana',
    #     '400',
    #     'Universidade',
    #     'Uberaba'
    # )
    # print(cl.read_all())
    # print(cl.read_by_name('pires'))
    ord = Order(db_conn)
    ord.create(
        '22689495618',
        150.62,
        3,
        51.68,
        ['2020-06-31', '2020-07-24', '2020-08-21']
    )
    # db_conn.export_db('backup.sql')
    # db_conn.import_db('backup.sql')