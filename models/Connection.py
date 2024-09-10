import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="mafalda_guidance",
        user="postgres",
        password="Dldg2907"
    )
    return conn

if __name__ == '__main__':
    try:
        conn = get_connection()
        print("Conexión exitosa a la base de datos.")
        conn.close()
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")

