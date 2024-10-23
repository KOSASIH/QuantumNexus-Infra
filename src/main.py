import argparse
import json
from edge_computing.node_manager import NodeManager
from ai_routing.routing_algorithm import RoutingAlgorithm

def load_node_config(config_file):
    """Load node configurations from a JSON file."""
    try:
        with open(config_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Configuration file {config_file} not found.")
        return {}

def main():
    """Main entry point for the application."""
    parser = argparse.ArgumentParser(description="Quantum Nexus Infrastructure Management")
    parser.add_argument('--node-config', type=str, default='node_config.json', help='Path to the node configuration file')
    parser.add_argument('--action', type=str, choices=['add', 'remove', 'deploy', 'health'], help='Action to perform on nodes')
    parser.add_argument('--node-id', type=str, help='Node ID for the action')
    parser.add_argument('--node-info', type=json.loads, help='Node information in JSON format for adding a node')

    args = parser.parse_args()

    # Load node configurations
    node_manager = NodeManager(args.node_config)

    if args.action == 'add':
        if args.node_id and args.node_info:
            node_manager.add_node(args.node_id, args.node_info)
            print(f"Node {args.node_id} added successfully.")
        else:
            print("Node ID and information are required to add a node.")

    elif args.action == 'remove':
        if args.node_id:
            node_manager.remove_node(args.node_id)
            print(f"Node {args.node_id} removed successfully.")
        else:
            print("Node ID is required to remove a node.")

    elif args.action == 'deploy':
        if args.node_id:
            node_manager.deploy_node(args.node_id)
        else:
            print("Node ID is required to deploy a node.")

    elif args.action == 'health':
        if args.node_id:
            node_manager.health_check(args.node_id)
        else:
            print("Node ID is required to perform a health check.")

    else:
        print("No valid action specified. Use --action to specify an action.")

if __name__ == "__main__":
    main()
