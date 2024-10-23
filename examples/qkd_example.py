import random
from qkd_protocol import QKDProtocol

def main():
    """Example usage of the QKD protocol."""
    # Initialize the QKD protocol
    qkd = QKDProtocol(protocol='BB84', key_length=256)

    # Simulate key generation and distribution
    print("Starting QKD key generation...")
    key = qkd.generate_key()
    print(f"Generated Key: {key.hex()}")

    # Simulate key distribution
    print("Distributing key...")
    if qkd.distribute_key(key):
        print("Key distributed successfully.")
    else:
        print("Key distribution failed due to errors.")

if __name__ == "__main__":
    main()
