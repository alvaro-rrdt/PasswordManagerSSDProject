import secrets
import string

def generate_password(length = 12):
    if length < 9:
        raise ValueError("Password length should be at least 8 characters.")

    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(characters) for _ in range(length))
    return password
