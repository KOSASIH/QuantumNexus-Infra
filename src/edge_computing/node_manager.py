import json
import os
import subprocess

class NodeManager:
    def __init__(self, config_file):
        self.config_file = config_file
        self.nodes = self.load_config()

    def load_config(self):
        """Load node configurations from a JSON file."""
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"Configuration file {self.config_file} not found.")
        with open(self.config_file, 'r') as file:
            return json.load(file)

    def add_node(self, node_id, node_info):
        """Add a new node to the configuration."""
        self.nodes[node_id] = node_info
        self.save_config()

    def remove_node(self, node_id):
        """Remove a node from the configuration."""
        if node_id in self.nodes:
            del self.nodes[node_id]
            self.save_config()
        else:
            raise ValueError(f"Node {node_id} does not exist.")

    def save_config(self):
        """Save the current node configurations to the JSON file."""
        with open(self.config_file, 'w') as file:
            json.dump(self.nodes, file, indent=4)

    def deploy_node(self, node_id):
        """Deploy a node using a deployment script."""
        if node_id not in self.nodes:
            raise ValueError(f"Node {node_id} does not exist.")
        
        deployment_script = self.nodes[node_id].get('deployment_script')
        if not deployment_script:
            raise ValueError(f"No deployment script defined for node {node_id}.")
        
        try:
            subprocess.run(['bash', deployment_script], check=True)
            print(f"Node {node_id} deployed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error deploying node {node_id}: {e}")

    def health_check(self, node_id):
        """Perform a health check on the specified node."""
        if node_id not in self.nodes:
            raise ValueError(f"Node {node_id} does not exist.")
        
        # Placeholder for actual health check logic
        print(f"Health check for node {node_id}: OK")

if __name__ == "__main__":
    # Example usage
    config_file = 'node_config.json'
    manager = NodeManager(config_file)

    # Add a new node
    manager.add_node('node1', {
        'ip_address': '192.168.1.10',
        'deployment_script': 'deploy_node1.sh'
    })

    # Deploy the node
    manager.deploy_node('node1')

    # Perform a health check
    manager.health_check('node1')
