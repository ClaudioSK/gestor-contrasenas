from src.database import PasswordManager

def main():
    manager = PasswordManager()

    # Ejemplo de uso
    manager.add_password("Gmail", "usuario@gmail.com", "contraseña_secreta")
    username, password = manager.get_password("Gmail")
    print(f"Usuario: {username}, Contraseña: {password}")

    manager.close()

if __name__ == "__main__":
    main()