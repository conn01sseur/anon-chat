import socket
import threading
from config import BUFFER_SIZE

def start_client(host, port):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))
        return client
    except Exception as e:
        print(f"Connection error: {e}")
        return None

def start_server(host, port):
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen(1)
        return server
    except Exception as e:
        print(f"Server start error: {e}")
        return None

def receive_messages(connection, key, callback):
    def listener():
        while True:
            try:
                data = connection.recv(BUFFER_SIZE)
                if not data:
                    break
                callback(data)
            except Exception as e:
                print(f"Receive error: {e}")
                break
    
    thread = threading.Thread(target=listener)
    thread.daemon = True
    thread.start()
    return thread