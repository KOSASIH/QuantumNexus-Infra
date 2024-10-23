from ai_routing.routing_algorithm import RoutingAlgorithm
from edge_computing.node_manager import NodeManager

def main():
    """Example usage of routing algorithms."""
    # Initialize the NodeManager and add nodes
    node_manager = NodeManager('config/network_config.yaml')
    node_manager.add_node('node1', {'ip_address': '192.168.1.10'})
    node_manager.add_node('node2', {'ip_address': '192.168.1.20'})
    node_manager.add_node('node3', {'ip_address': '192.168.1.30'})

    # Initialize the routing algorithm
    routing_algorithm = RoutingAlgorithm(node_manager)

    # Find the route from node1 to node2
    print("Finding route from node1 to node2...")
    path = routing_algorithm.find_route('node1', 'node2')
    if path:
        print(f"Route found: {' -> '.join(path)}")
    else:
        print("No route found.")

if __name__ == "__main__":
    main()
