from edge_computing.node_manager import NodeManager

def main():
    """Example usage of edge computing nodes."""
    # Initialize the NodeManager
    node_manager = NodeManager('config/network_config.yaml')

    # Add a new edge node
    node_id = 'edge_node_1'
    node_info = {'ip_address': '192.168.1.100', 'deployment_script': 'deployment_scripts/deploy_edge_node_1.sh'}
    print(f"Adding edge node: {node_id}")
    node_manager.add_node(node_id, node_info)

    # List all nodes
    print("Current nodes in the network:")
    for node in node_manager.nodes:
        print(f"- {node}")

    # Remove the edge node
    print(f"Removing edge node: {node_id}")
    node_manager.remove_node(node_id)

if __name__ == "__main__":
    main()
