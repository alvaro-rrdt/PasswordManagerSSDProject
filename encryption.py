from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import base64


def derive_key(passphrase, salt=None):
    if salt is None:
        salt = b'fixed_salt'

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(passphrase.encode()))
    return key


def encrypt_message(message, passphrase):
    key = derive_key(passphrase)
    f = Fernet(key)
    encoded_mesaage = message.encode()
    encrypted_message = f.encrypt(encoded_mesaage)
    return encrypted_message

def decrypt_message(encrypted_message, passphrase):
    key = derive_key(passphrase)
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

