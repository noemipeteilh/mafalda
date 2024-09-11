import json
from controllers.advice_controller import AdviceController


try:
    with open('C:/Users/Noemi/Desktop/PROYECTO PEDAGOGICO INDIVIDUAL/mafalda/data/data.json', 'r') as f:
        data = json.load(f)
        print("Datos cargados exitosamente.")
except FileNotFoundError:
    print("Error: No se pudo encontrar el archivo data.json.")
    exit(1)
except json.JSONDecodeError as e:
    print(f"Error al decodificar JSON: {e}")
    exit(1)


try:
    AdviceController.create_advice_from_json(data)
    print("Consejos insertados correctamente en la base de datos.")
except Exception as e:
    print(f"Error al insertar los consejos: {e}")


try:
    id = 10
    advice = AdviceController.get_advice(id)
    if advice:
        print(f"Consejo obtenido: {advice}")
    else:
        print(f"No se encontró un consejo con el ID {id}")
except Exception as e:
    print(f"Error al obtener el consejo: {e}")


