import unittest
from quantum_key_distribution.qkd_protocol import QKDProtocol
from quantum_key_distribution.key_management import KeyManager
import os
import json

class TestQKDProtocol(unittest.TestCase):
    def setUp(self):
        """Set up the test environment before each test."""
        self.user_id = "test_user"
        self.qkd = QKDProtocol(self.user_id)
        self.key_manager = KeyManager(self.user_id)
        self.test_length = 100

    def test_generate_raw_key(self):
        """Test the raw key generation."""
        self.qkd.generate_raw_key(self.test_length)
        self.assertEqual(len(self.qkd.raw_key), self.test_length)
        self.assertEqual(len(self.qkd.bases), self.test_length)

    def test_simulate_eavesdropping(self):
        """Test the eavesdropping simulation."""
        error_rate = self.qkd.simulate_eavesdropping()
        self.assertGreaterEqual(error_rate, 0.1)
        self.assertLessEqual(error_rate, 0.3)

    def test_perform_key_sifting(self):
        """Test the key sifting process."""
        self.qkd.generate_raw_key(self.test_length)
        sifted_key = self.qkd.perform_key_sifting()
        self.assertTrue(all(bit in [0, 1] for bit in sifted_key))
        self.assertLessEqual(len(sifted_key), self.test_length)

    def test_error_correction(self):
        """Test the error correction process."""
        self.qkd.generate_raw_key(self.test_length)
        sifted_key = self.qkd.perform_key_sifting()
        corrected_key = self.qkd.error_correction(sifted_key)
        self.assertEqual(corrected_key, sifted_key)  # Placeholder logic

    def test_privacy_amplification(self):
        """Test the privacy amplification process."""
        self.qkd.generate_raw_key(self.test_length)
        sifted_key = self.qkd.perform_key_sifting()
        corrected_key = self.qkd.error_correction(sifted_key)
        amplified_key = self.qkd.privacy_amplification(corrected_key)
        self.assertLessEqual(len(amplified_key), len(corrected_key))

    def test_execute_protocol(self):
        """Test the complete QKD protocol execution."""
        final_key = self.qkd.execute_protocol(self.test_length)
        self.assertIsNotNone(final_key)
        self.assertTrue(all(bit in [0, 1] for bit in final_key))

    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists(self.key_manager.key_storage_path):
            os.remove(self.key_manager.key_storage_path)

if __name__ == "__main__":
    unittest.main()
