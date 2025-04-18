from cryptography.fernet import Fernet
import base64
import hashlib

def gen_key(user_input):
    key = hashlib.sha256(user_input.encode()).digest()
    return base64.urlsafe_b64encode(key)

def encrypt(message, key):
    fernet = Fernet(key)
    return fernet.encrypt(message.encode())

def decrypt(encrypted_message, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_message).decode()