import json
import os
from encryption import encrypt_message, decrypt_message
from password_generator import generate_password

class PasswordManager:
    def __init__(self, master_passphrase, db_file='passwords.json'):
        self.db_file = db_file
        self.credentials = self.load_credentials()

    def load_credentials(self):
        if os.path.exists(self.db_file):
            with open(self.db_file, 'rb') as file:
                encrypted_data = file.read()
                decrypted_data = decrypt_message(encrypted_data)
                return json.loads(decrypted_data)
        return {}

    def save_credentials(self):
        encrypted_data = encrypt_message(json.dumps(self.credentials))
        with open(self.db_file, 'wb') as file:
            file.write(encrypted_data)

    def add_credential(self, service, username, password):
        if not service or not username or not password:
            print("Service, username, and password are required.")
            return
        self.credentials[service] = {'username': username, 'password': password}
        self.save_credentials()

    def get_credential(self, service):
        return self.credentials.get(service, None)

def main():
    manager = PasswordManager()
    while True:
        action = input("Do you want to add or get a credential? (add/get/exit): ").lower()
        if action == 'add':
            service = input("Enter the service name: ")
            username = input("Enter your username: ")
            password = input("Enter your password (or leave blank to generate a random one): ")
            if not password:
                password = generate_password()
                print(f"Generated password: {password}")
            manager.add_credential(service, username, password)
            print("Credential saved.")
        elif action == 'get':
            service = input("Enter the service name to retrieve: ")
            credential = manager.get_credential(service)
            if credential:
                print(f"Username: {credential['username']}, Password: {credential['password']}")
            else:
                print("No credential found for that service.")
        elif action == 'exit':
            break
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()