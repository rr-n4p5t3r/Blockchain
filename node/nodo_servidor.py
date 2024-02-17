import requests
import json
import uuid

NODE_REGISTER_URL = "http://0.0.0.0/registrar" #url de ejemplo

class Nodo:
    def __init__(self, address):
        self.address = address
        self.id = str(uuid.uuid4())
        self.registrar()

    def registrar(self):
        payload = {"id": self.id, "address": self.address}
        response = requests.post(NODE_REGISTER_URL, json=payload)
        if response.status_code == 200:
            print("Nodo registrado exitosamente.")
        else:
            print("Error al registrar el nodo.")

# Cuando se inicia un nodo, se registra automáticamente
mi_nodo = Nodo("http://mi-direccion-ip:mi-puerto")

# Servidor de registro
from flask import Flask, request

app = Flask(__name__)
nodos = {}

@app.route('/registrar', methods=['POST'])
def registrar_nodo():
    data = request.json
    nodo_id = data.get('id')
    nodo_address = data.get('address')
    if nodo_id and nodo_address:
        nodos[nodo_id] = nodo_address
        print(f"Nodo registrado: {nodo_id} en {nodo_address}")
        return json.dumps({"message": "Nodo registrado exitosamente."}), 200
    else:
        return json.dumps({"message": "Datos de nodo no válidos."}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
