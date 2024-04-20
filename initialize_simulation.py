
import json
import random

def load_config(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def initialize_network(config):
    nodes = []
    for i in range(config['network_size']):
        node = {
            'id': i,
            'type': config['node_type'],
            'frequency': config['frequency_range'],
            'depth': random.randint(10, config['depth_variation']),
            'energy_level': 100,  # Initial energy level percentage
            'security_protocol': config['security_protocol']
        }
        nodes.append(node)
    return nodes

def main():
    config_path = 'config_network_size_50.json'  # Path to the configuration file
    config = load_config(config_path)
    network = initialize_network(config)
    print(f'Initialized network with {len(network)} nodes.')
    for node in network[:5]:  # Print details of the first 5 nodes to check
        print(node)

if __name__ == '__main__':
    main()
