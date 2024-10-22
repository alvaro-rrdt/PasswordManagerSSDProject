import json
import os
from encryption import encrypt_message, decrypt_message
from password_generator import generate_password

class PasswordManager:
    def __init__(self, master_passphrase, db_file='passwords.json'):
        self.db_file = db_file
        self.master_passphrase = master_passphrase
        self.credentials = self.load_credentials()

    def load_credentials(self):
        if os.path.exists(self.db_file):
            with open(self.db_file, 'rb') as file:
                encrypted_data = file.read()
            try:
                decrypted_data = decrypt_message(encrypted_data, self.master_passphrase)
                return json.loads(decrypted_data)
            except Exception:
                print("Invalid master passphrase or corrupted data.")
                return {}
        return {}

    def save_credentials(self):
        encrypted_data = encrypt_message(json.dumps(self.credentials), self.master_passphrase)
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
    while True:
        master_passphrase = input("Enter your master passphrase: ")
        if len(master_passphrase) < 8:
            print("Master passphrase should be at least 8 characters.")
            continue
        break

    manager = PasswordManager(master_passphrase)
    while True:
        action = input("Do you want to add or get a password? (add/get/exit): ").lower()
        if action == 'add':
            service = input("Enter service name: ")
            username = input("Enter username: ")
            password = input("Enter password or leave empty to generate one: ")
            if not password:
                password = generate_password()
                print(f"Generated password: {password}")
            manager.add_credential(service, username, password)
            print("Credential added successfully.")
        elif action == 'get':
            service = input("Enter service name: ")
            credential = manager.get_credential(service)
            if credential:
                print(f"Username: {credential['username']}")
                print(f"Password: {credential['password']}")
            else:
                print("Credential not found.")
        elif action == 'exit':
            break
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()