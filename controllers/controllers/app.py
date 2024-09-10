import json
from controllers.controllers import AdviceController

# Leer el archivo JSON
with open('data.json', 'r') as f:
    data = json.load(f)

# Iterar sobre los registros y cargarlos en la base de datos
for advice in data:
    AdviceController.create_advice(advice['genero'], advice['edad'], advice['conducta'], advice['consejo'])
