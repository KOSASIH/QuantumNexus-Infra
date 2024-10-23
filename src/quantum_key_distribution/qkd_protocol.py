import numpy as np
import random
from key_management import KeyManager

class QKDProtocol:
    def __init__(self, user_id):
        self.user_id = user_id
        self.key_manager = KeyManager(user_id)
        self.basis_choices = ['Z', 'X']  # Z-basis and X-basis
        self.key_length = 0
        self.raw_key = []
        self.bases = []

    def generate_raw_key(self, length):
        """Generate a raw key using random bits and random basis choices."""
        self.key_length = length
        self.raw_key = [random.randint(0, 1) for _ in range(length)]
        self.bases = [random.choice(self.basis_choices) for _ in range(length)]
        print(f"Raw key generated: {self.raw_key}")
        print(f"Basis choices: {self.bases}")

    def simulate_eavesdropping(self):
        """Simulate eavesdropping and return the error rate."""
        # For simplicity, assume a fixed error rate for demonstration
        error_rate = random.uniform(0.1, 0.3)  # 10% to 30% error rate
        print(f"Simulated eavesdropping error rate: {error_rate:.2%}")
        return error_rate

    def perform_key_sifting(self):
        """Sift the raw key based on the basis choices."""
        sifted_key = []
        for i in range(self.key_length):
            if self.bases[i] == 'Z':  # Only keep Z-basis bits
                sifted_key.append(self.raw_key[i])
        print(f"Sifted key: {sifted_key}")
        return sifted_key

    def error_correction(self, sifted_key):
        """Perform error correction on the sifted key."""
        # Placeholder for error correction logic
        corrected_key = sifted_key  # In a real implementation, apply error correction
        print(f"Corrected key: {corrected_key}")
        return corrected_key

    def privacy_amplification(self, corrected_key):
        """Apply privacy amplification to the corrected key."""
        # Placeholder for privacy amplification logic
        amplified_key = corrected_key[:len(corrected_key) // 2]  # Simple example
        print(f"Amplified key: {amplified_key}")
        return amplified_key

    def execute_protocol(self, length):
        """Execute the QKD protocol."""
        self.generate_raw_key(length)
        error_rate = self.simulate_eavesdropping()
        
        if error_rate > 0.2:  # Threshold for acceptable error rate
            print("Error rate too high, aborting key generation.")
            return None
        
        sifted_key = self.perform_key_sifting()
        corrected_key = self.error_correction(sifted_key)
        final_key = self.privacy_amplification(corrected_key)
        
        # Store the final key securely
        self.key_manager.store_key(final_key)
        print(f"Final key stored securely: {final_key}")
        return final_key

if __name__ == "__main__":
    user_id = "user123"
    qkd = QKDProtocol(user_id)
    qkd.execute_protocol(length=100)
