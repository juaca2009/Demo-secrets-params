import psycopg2

def connect_to_database(credentials):
    """
    Establece una conexión a la base de datos PostgreSQL usando las credenciales proporcionadas.
    """
    try:
        connection = psycopg2.connect(
            user=credentials['username'],
            password=credentials['password'],
            host=credentials['host'],
            port=credentials['port'],
            database=credentials['dbname']
        )
        print("Conexión a la base de datos establecida correctamente.")
        return connection
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None