import mysql.connector

def get_connection (host: str, user: str, password: str, database: str = 'biblioteca_dardo'):
    connection = mysql.connector.connect(
        host = host,
        user = user,
        password = password,
        database = database
    )

    if (not connection.is_connected()):
        raise Exception('Error: No se pudo conectar a la base de datos.')
    
    return connection;
