#!/bin/bash

# Script to deploy edge computing nodes

CONFIG_FILE="config/network_config.yaml"

# Function to deploy a node
deploy_node() {
    local node_id=$1
    local deployment_script=$2

    echo "Deploying node: $node_id"
    if [ -f "$deployment_script" ]; then
        bash "$deployment_script"
        echo "Node $node_id deployed successfully."
    else
        echo "Deployment script for $node_id not found."
    fi
}

# Load node configurations from YAML file
nodes=$(python3 -c "import yaml; print(yaml.safe_load(open('$CONFIG_FILE'))['network']['max_nodes'])")

# Loop through each node and deploy
for ((i=1; i<=nodes; i++)); do
    NODE_ID="node$i"
    DEPLOYMENT_SCRIPT="deployment_scripts/deploy_$NODE_ID.sh"
    deploy_node "$NODE_ID" "$DEPLOYMENT_SCRIPT"
done

echo "All nodes have been processed."
