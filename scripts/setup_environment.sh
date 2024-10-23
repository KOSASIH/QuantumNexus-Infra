#!/bin/bash

# Script to set up the development environment for QuantumNexus-Infra

echo "Setting up the development environment..."

# Update package list
sudo apt-get update

# Install Python and pip
sudo apt-get install -y python3 python3-pip

# Install required Python packages
pip3 install -r requirements.txt

# Install additional tools (if needed)
sudo apt-get install -y git

echo "Development environment setup complete."
