import psycopg2
import psycopg2.errors
from psycopg2 import sql

# Library dependency: psycopg2

def connect_to_postgres_db():
    """
    Establishes a connection to a PostgreSQL database.
    Returns the connection object.
    """
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="comm",
            user="postgres",
            password="pass"
        )
        return connection
    except psycopg2.errors.Error as e:
        print(f"Error connecting to PostgreSQL database: {e}")
        return None

def list_postgres_tables(connection):
    """
    Queries the PostgreSQL database to list all tables.
    Args:
        connection (psycopg2.connection): The connection object to the PostgreSQL database.
    Returns:
        list: A list of table names.
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
            tables = cursor.fetchall()
            return [table[0] for table in tables]
    except psycopg2.errors.Error as e:
        print(f"Error querying PostgreSQL database: {e}")
        return []

def main():
    """
    Main function to establish connection, list tables, and close connection.
    """
    postgres_connection = connect_to_postgres_db()
    if postgres_connection:
        tables = list_postgres_tables(postgres_connection)
        print("Tables in PostgreSQL database:")
        for table in tables:
            print(table)
        postgres_connection.close()  # Close the connection after the operation

if __name__ == "__main__":
    main()

    host = "localhost",
    database = "comm",
    user = "postgres",
    password = "pass"

    ["core_category", "core_product", "core_order"]