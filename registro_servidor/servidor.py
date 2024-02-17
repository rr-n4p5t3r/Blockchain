from flask import Flask, request, jsonify

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
        return jsonify({"message": "Nodo registrado exitosamente."}), 200
    else:
        return jsonify({"message": "Datos de nodo no válidos."}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
