import sqlite3
from src.encryption import EncryptionManager

class PasswordManager:
    def __init__(self, db_name="contrasenas.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.encryption_manager = EncryptionManager()
        self._create_table()

    def _create_table(self):
        """Crea la tabla para almacenar contraseñas."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS passwords (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                service TEXT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def add_password(self, service, username, password):
        """Añade una nueva contraseña."""
        encrypted_password = self.encryption_manager.encrypt(password)
        self.cursor.execute("""
            INSERT INTO passwords (service, username, password)
            VALUES (?, ?, ?)
        """, (service, username, encrypted_password))
        self.conn.commit()

    def get_password(self, service):
        """Obtiene una contraseña por servicio."""
        self.cursor.execute("""
            SELECT username, password FROM passwords WHERE service = ?
        """, (service,))
        result = self.cursor.fetchone()
        if result:
            username, encrypted_password = result
            password = self.encryption_manager.decrypt(encrypted_password)
            return username, password
        return None

    def close(self):
        """Cierra la conexión a la base de datos."""
        self.conn.close()