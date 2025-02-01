from cryptography.fernet import Fernet

class EncryptionManager:
    def __init__(self, key=None):
        if key is None:
            self.key = Fernet.generate_key()  # Genera una clave nueva
        else:
            self.key = key
        self.cipher = Fernet(self.key)

    def encrypt(self, data):
        """Cifra los datos."""
        return self.cipher.encrypt(data.encode())

    def decrypt(self, encrypted_data):
        """Descifra los datos."""
        return self.cipher.decrypt(encrypted_data).decode()