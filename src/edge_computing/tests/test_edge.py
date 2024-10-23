import unittest
import json
import os
from unittest.mock import patch, MagicMock
from edge_computing.node_manager import NodeManager

class TestNodeManager(unittest.TestCase):
    def setUp(self):
        """Set up the test environment before each test."""
        self.config_file = 'test_node_config.json'
        self.initial_config = {
            "node1": {
                "ip_address": "192.168.1.10",
                "deployment_script": "deployment_scripts/deploy_node1.sh"
            }
        }
        with open(self.config_file, 'w') as f:
            json.dump(self.initial_config, f, indent=4)
        self.node_manager = NodeManager(self.config_file)

    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists(self.config_file):
            os.remove(self.config_file)

    def test_load_config(self):
        """Test loading the configuration from a file."""
        self.assertEqual(self.node_manager.nodes, self.initial_config)

    def test_add_node(self):
        """Test adding a new node to the configuration."""
        new_node = {
            "ip_address": "192.168.1.20",
            "deployment_script": "deployment_scripts/deploy_node2.sh"
        }
        self.node_manager.add_node('node2', new_node)
        self.assertIn('node2', self.node_manager.nodes)
        self.assertEqual(self.node_manager.nodes['node2'], new_node)

    def test_remove_node(self):
        """Test removing a node from the configuration."""
        self.node_manager.remove_node('node1')
        self.assertNotIn('node1', self.node_manager.nodes)

    def test_remove_nonexistent_node(self):
        """Test removing a node that does not exist."""
        with self.assertRaises(ValueError):
            self.node_manager.remove_node('nonexistent_node')

    @patch('subprocess.run')
    def test_deploy_node(self, mock_run):
        """Test deploying a node."""
        mock_run.return_value = MagicMock(returncode=0)
        self.node_manager.deploy_node('node1')
        mock_run.assert_called_once_with(['bash', 'deployment_scripts/deploy_node1.sh'], check=True)

    def test_deploy_nonexistent_node(self):
        """Test deploying a node that does not exist."""
        with self.assertRaises(ValueError):
            self.node_manager.deploy_node('nonexistent_node')

    @patch('builtins.print')
    def test_health_check(self, mock_print):
        """Test health check for a node."""
        self.node_manager.health_check('node1')
        mock_print.assert_called_once_with("Health check for node1: OK")

    def test_health_check_nonexistent_node(self):
        """Test health check for a node that does not exist."""
        with self.assertRaises(ValueError):
            self.node_manager.health_check('nonexistent_node')

if __name__ == "__main__":
    unittest.main()
