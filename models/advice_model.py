from models.connection import get_connection

class AdviceModel:
    @staticmethod
    def create_advice(genero, edad, conducta, consejo):
        conn = get_connection()
        cur = conn.cursor()
        try:
             cur.execute("""
                 INSERT INTO advices (edad, genero, conducta, consejo)
                 VALUES (%s, %s, %s, %s)
             """,(edad, genero,conducta,consejo))
             conn.commit()
        except Exception as e :
             print(f"Error al insertar: {e}")
        finally:
            cur.close()
            conn.close()

@staticmethod
def get_advice(id):
    conn = get_connection()
    cur =  conn.cursor()
    try:
        cur.execute("SELECT * FROM advices WHERE id = %s",(id,))
        advice = cur.fetchone()
        return advice
    except Exception as e:
        print(f"Error al obtener el consejo: {e}")
    finally:
        cur.close()
        conn.close()

@staticmethod
def updated_advice(id, genero, edad, conducta, consejo):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
        UPDATE advices SET genero = %s, edad = %s, conducta = %s, consejo = %s WHERE id = %s
        """,(genero, edad, conducta,consejo,id))
        conn.commit()
    except Exception as e:
        print(f"Error al actualizar el consejo: {e}")
    finally:
        cur.close()
        conn.close()

@staticmethod
def delete_advice(id):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM advices WHERE id = %s", (id,))
        conn.commit()
    except Exception as e:
        print (f"Error al eliminar el consejo {e}")
    finally:
        cur.close()
        conn.close()
