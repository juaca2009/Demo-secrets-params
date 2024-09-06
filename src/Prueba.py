from parameters import get_parameter
from dataBase import connect_to_database
from secretos import get_secret


def main():
    parameter_name = '/config/db_credentials_secret_name'
    
    # Obtener el nombre del secreto desde Parameter Store
    secret_name = get_parameter(parameter_name)
    if not secret_name:
        print("No se pudo obtener el nombre del secreto desde Parameter Store.")
        return

    # Obtener las credenciales desde Secrets Manager
    credentials = get_secret(secret_name)
    if not credentials:
        print("No se pudieron obtener las credenciales desde Secrets Manager.")
        return

    # Conectar a la base de datos
    connection = connect_to_database(credentials)
    if not connection:
        print("No se pudo establecer la conexión a la base de datos.")
        return

    try:
        # Ejecutar una consulta de ejemplo
        with connection.cursor() as cursor:
            cursor.execute("SELECT version();")
            db_version = cursor.fetchone()
            print(f"Versión de la base de datos: {db_version[0]}")
    except Exception as e:
        print(f"Error al ejecutar la consulta: {e}")
    finally:
        # Cerrar la conexión
        connection.close()
        print("Conexión cerrada correctamente.")

if __name__ == "__main__":
    main()
