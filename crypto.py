from cryptography.fernet import Fernet
import base64
import hashlib

# Генерация ключа
def gen_key(user_input):
    key = hashlib.sha256(user_input.encode()).digest()
    return base64.urlsafe_b64encode(key)

# Шифрование
def encrypt(message, key):
    fernet = Fernet(key)
    return fernet.encrypt(message.encode())

# Дешифровка
def decrypt(encrypted_message, key):
    """Дешифрование сообщения"""
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_message).decode()