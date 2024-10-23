import unittest
import subprocess
import os

class TestSystemFunctionality(unittest.TestCase):
    def test_setup_environment(self):
        """Test the setup environment script."""
        result = subprocess.run(['bash', 'scripts/setup_environment.sh'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn("Development environment setup complete.", result.stdout)

    def test_deploy_nodes(self):
        """Test the deployment of nodes."""
        # Assuming the deployment scripts are present
        result = subprocess.run(['bash', 'scripts/deploy_nodes.sh'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn("All nodes have been processed.", result.stdout)

    def test_generate_keys(self):
        """Test the key generation script."""
        key_length = 32  # 32 bytes = 256 bits
        output_file = 'test_key.bin'
        result = subprocess.run(['python3', 'scripts/generate_keys.py', str(key_length), output_file], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertTrue(os.path.exists(output_file))

        # Clean up the generated key file
        os.remove(output_file)

if __name__ == '__main__':
    unittest.main()
