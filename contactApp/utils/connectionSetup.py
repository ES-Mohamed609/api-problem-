import mariadb


def get_db_connection():
    conn = mariadb.connect(
        user='root',
        password='ahmed2006',
        host='localhost',
        port=3306,
        database='internship'
    )
    return conn