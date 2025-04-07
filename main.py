from cryptography.fernet import Fernet
import base64
import hashlib
import socket
import threading

# Настройки сокета
host = "127.0.0.1"
port = 8080

# Генерация ключа
def gen_key(user_input):
    key = hashlib.sha256(user_input.encode()).digest()
    return base64.urlsafe_b64encode(key)

# Шифрование
def encrypt(message, key):
    fernet = Fernet(key)
    return fernet.encrypt(message.encode())

# Дешифрование
def decrypt(message_encrypt, key):
    fernet = Fernet(key)
    return fernet.decrypt(message_encrypt).decode()

# Получение сообщений
def get_message(client, key):
    while True:
        try:
            data = client.recv(1024)
            if not data:
                break
            print(f"Server# {decrypt(data, key)}")
        except Exception as e:
            break

# Получение сообщений
def get_message_server(client_socket, key):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Client# {decrypt(data, key)}")
        except Exception as e:
            break

banner = f'''
Your host: {host}
Your port: {port}

1. Connect (client)
2. Create server
3. Exit'''

print(banner)

menu = int(input("--> "))

if menu == 1:
    # Клиентский режим
    host = input("Input host --> ")
    port = int(input("Input port --> "))
    user_input = input("Crypt key --> ")
    key = gen_key(user_input)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print("\nConnection to the server is established")

    # Запуск потока для получения сообщений
    thread = threading.Thread(target=get_message, args=(client, key))
    thread.daemon = True
    thread.start()

    try:
        while True:
            message = input()
            if message.lower() == 'exit':
                break
            encrypted = encrypt(message, key)
            client.sendall(encrypted)
    finally:
        client.close()

elif menu == 2:
    # Серверный режим
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    print("Server is running, waiting for connections...")

    user_input = input("Crypt key --> ")
    key = gen_key(user_input)

    client_socket, addr = server.accept()
    print(f"Connection from {addr}")

    # Запуск потока для получения сообщений
    thread = threading.Thread(target=get_message_server, args=(client_socket, key))
    thread.daemon = True
    thread.start()

    try:
        while True:
            message = input()
            if message.lower() == 'exit':
                break
            encrypted = encrypt(message, key)
            client_socket.sendall(encrypted)
    finally:
        client_socket.close()
        server.close()