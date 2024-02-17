import json

def update_node_list(nodes):
    with open('node.json', 'w') as file:
        json.dump({"nodes": nodes}, file)

def add_node_to_list(node):
    with open('node.json', 'r') as file:
        data = json.load(file)
        nodes = data.get("nodes", [])
        nodes.append(node)
    update_node_list(nodes)

# Ejemplo de uso
new_node = "http://0.0.0.0:5004"
add_node_to_list(new_node)
