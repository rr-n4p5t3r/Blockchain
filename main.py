# Proyecto blockchain
# Desarrollado por Ricardo Rosero - n4p5t3r
# Email: rrosero2000@gmail.com

from flask import Flask
from app.routes import app as app_routes
from registro_servidor.servidor import app as app_registro_servidor
from node.node_manager import start_nodes
from blockchain.blockchain import start_blockchain_server
from transaction.transaction_manager import start_transaction_server

# Crear instancia de Flask
app = Flask(__name__)

# Montar las aplicaciones Flask
app.register_blueprint(app_routes)
app.register_blueprint(app_registro_servidor)

# Iniciar el servidor de nodos
start_nodes()

# Iniciar el servidor del blockchain
start_blockchain_server()

# Iniciar el servidor de transacciones
start_transaction_server()

# Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
