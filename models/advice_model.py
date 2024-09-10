from Connection import get_connection


class AdviceModel:
    @staticmethod
    def create_advice(genero, edad, conducta, consejo):
        conn = get_connection()
        cur = conn.cursor()
        try:
            cur.execute("""
                INSERT INTO advices (age, gender, behavior, advice)
                VALUES (%s, %s, %s, %s)
            """, (str(edad), genero, conducta, consejo))
            conn.commit()
        except Exception as e:
            print(f"Error al insertar: {e}")
        finally:
            cur.close()
            conn.close()

    @staticmethod
    def get_advice(id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM advices WHERE id = %s", (id,))
        advice = cur.fetchone()
        cur.close()
        conn.close()
        return advice

    @staticmethod
    def update_advice(id, new_advice):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            UPDATE advices SET advice = %s WHERE id = %s
        """, (new_advice, id))
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def delete_advice(id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM advices WHERE id = %s", (id,))
        conn.commit()
        cur.close()
        conn.close()


if __name__ == '__main__':
    # Prueba de creación de un consejo
    print("Insertando un consejo...")
    AdviceModel.create_advice('Niño', 10, 'Hiperactividad', 'Consulta a un profesional de la salud mental.')

    # Prueba de lectura de un consejo
    advice = AdviceModel.get_advice(1)  # Cambia el ID según los datos que tengas en la tabla
    print("Consejo obtenido:", advice)

    # Prueba de actualización
    print("Actualizando el consejo...")
    AdviceModel.update_advice(1, 'Consejo actualizado: Consulte a un profesional de inmediato.')

    # Prueba de eliminación
    print("Eliminando el consejo...")
    AdviceModel.delete_advice(1)
