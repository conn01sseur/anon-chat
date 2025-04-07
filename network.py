import socket
import threading
from .crypto import encrypt, decrypt
from .config import BUFFER_SIZE

def start_client(host, port, key):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    return client

def start_server(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    return server

def receive_messages(client, key, callback):
    def run():
        while True:
            try:
                data = client.recv(BUFFER_SIZE)
                if not data:
                    break
                decrypted = decrypt(data, key)
                callback(decrypted)
            except Exception as e:
                print(f"Ошибка получения: {e}")
                break
    thread = threading.Thread(target=run)
    thread.daemon = True
    thread.start()
    return thread