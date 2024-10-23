import os
import json
from cryptography.fernet import Fernet

class KeyManager:
    def __init__(self, user_id):
        self.user_id = user_id
        self.key_storage_path = f"keys/{user_id}_keys.json"
        self.secret_key = self.generate_secret_key()
        self.cipher = Fernet(self.secret_key)

    def generate_secret_key(self):
        """Generate a secret key for encrypting stored keys."""
        return Fernet.generate_key()

    def store_key(self, key):
        """Store the generated key securely."""
        encrypted_key = self.cipher.encrypt(json.dumps(key).encode())
        if not os.path.exists('keys'):
            os.makedirs('keys')
        with open(self.key_storage_path, 'w') as f:
            json.dump({'encrypted_key': encrypted_key.decode(), 'secret_key': self.secret_key.decode()}, f)
        print(f"Key stored securely for user {self.user_id}.")

    def retrieve_key(self):
        """Retrieve the stored key securely."""
        if not os.path.exists(self.key_storage_path):
            print("No key found.")
            return None
        with open(self.key_storage_path, 'r') as f:
            data = json.load(f)
            encrypted_key = data['encrypted_key'].encode()
            secret_key = data['secret_key'].encode()
            cipher = Fernet(secret_key)
            decrypted_key = cipher.decrypt(encrypted_key)
            return json.loads(decrypted_key.decode())

if __name__ == "__main__":
    user_id = "user123"
    km = KeyManager(user_id)
    km.store_key([1, 2, 3, 4, 5])  # Example key
    retrieved_key = km.retrieve_key()
    print(f"Retrieved key: {retrieved_key}")
