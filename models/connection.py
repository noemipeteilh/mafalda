import psycopg2
from psycopg2 import sql

def get_connection():
    try:
        conn = psycopg2.connect(
            dbname="mafalda_guidance",
            user="postgres",
            password="Dldg2907",
            host="localhost",  # o el host de tu base de datos
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
