import json

class TransactionManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_transaction_data(self):
        with open(self.file_path, 'r') as file:
            transaction_data = json.load(file)
        return transaction_data

    def write_transaction_data(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def update_transaction_data(self, updates):
        current_data = self.read_transaction_data()
        current_data.update(updates)
        self.write_transaction_data(current_data)

if __name__ == "__main__":
    transaction_manager = TransactionManager('transaction.json')

    # Leer los datos actuales
    current_data = transaction_manager.read_transaction_data()
    print("Datos actuales:", current_data)

    # Actualizar los datos
    updates = {'sender': "Alice", 'receiver': "Bob", 'amount': "20"}
    transaction_manager.update_transaction_data(updates)

    # Leer los datos actualizados
    current_data = transaction_manager.read_transaction_data()
    print("Datos actualizados:", current_data)
