import unittest
from edge_computing.node_manager import NodeManager
from ai_routing.routing_algorithm import RoutingAlgorithm

class TestNodeManagerIntegration(unittest.TestCase):
    def setUp(self):
        """Set up the NodeManager for testing."""
        self.node_manager = NodeManager('config/network_config.yaml')

    def test_add_node_integration(self):
        """Test the integration of adding a node."""
        node_id = 'test_node'
        node_info = {'ip_address': '192.168.1.100', 'deployment_script': 'deployment_scripts/deploy_test_node.sh'}
        self.node_manager.add_node(node_id, node_info)
        self.assertIn(node_id, self.node_manager.nodes)

    def test_remove_node_integration(self):
        """Test the integration of removing a node."""
        node_id = 'test_node'
        self.node_manager.add_node(node_id, {'ip_address': '192.168.1.100'})
        self.node_manager.remove_node(node_id)
        self.assertNotIn(node_id, self.node_manager.nodes)

    def test_routing_integration(self):
        """Test the integration of routing functionality."""
        self.node_manager.add_node('node1', {'ip_address': '192.168.1.10'})
        self.node_manager.add_node('node2', {'ip_address': '192.168.1.20'})
        routing_algorithm = RoutingAlgorithm(self.node_manager)
        path = routing_algorithm.find_route('node1', 'node2')
        self.assertIsNotNone(path)
        self.assertIn('node1', path)
        self.assertIn('node2', path)

if __name__ == '__main__':
    unittest.main()
