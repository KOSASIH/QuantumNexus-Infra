import os
import sys
import secrets

def generate_key(length):
    """Generate a cryptographic key of specified length."""
    return secrets.token_bytes(length)

def save_key(key, filename):
    """Save the generated key to a file."""
    with open(filename, 'wb') as key_file:
        key_file.write(key)
    print(f"Key saved to {filename}")

def main():
    """Main function to generate and save a cryptographic key."""
    if len(sys.argv) != 3:
        print("Usage: python generate_keys.py <key_length> <output_file>")
        sys.exit(1)

    key_length = int(sys.argv[1])
    output_file = sys.argv[2]

    key = generate_key(key_length)
    save_key(key, output_file)

if __name__ == "__main__":
    main()
