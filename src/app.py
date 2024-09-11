import json
from controllers.advice_controller import AdviceController

# Cargar el archivo JSON
try:
    with open('C:/Users/Noemi/Desktop/PROYECTO PEDAGOGICO INDIVIDUAL/mafalda/data/data.json', 'r') as f:
        data = json.load(f)
        print("Datos cargados exitosamente.")
except FileNotFoundError:
    print("Error: No se pudo encontrar el archivo data.json.")
    exit(1)  # Termina el programa si el archivo no se encuentra
except json.JSONDecodeError as e:
    print(f"Error al decodificar JSON: {e}")
    exit(1)

# Insertar los datos en la base de datos
try:
    AdviceController.create_advice_from_json(data)
    print("Consejos insertados correctamente en la base de datos.")
except Exception as e:
    print(f"Error al insertar los consejos: {e}")

# Obtener un consejo por su ID
try:
    id = 1  # Aquí debes definir o asignar un ID válido existente en tu base de datos
    advice = AdviceController.get_advice(id)
    if advice:
        print(f"Consejo obtenido: {advice}")
    else:
        print(f"No se encontró un consejo con el ID {id}")
except Exception as e:
    print(f"Error al obtener el consejo: {e}")


