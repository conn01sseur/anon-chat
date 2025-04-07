from network import start_client, start_server, receive_messages
from crypto import gen_key, encrypt, decrypt
from ui import show_banner, get_connection_params
from config import DEFAULT_HOST, DEFAULT_PORT
import socket

def main():
    show_banner(DEFAULT_HOST, DEFAULT_PORT)
    choice = input("--> ")
    
    if choice == "1":

        host, port, key_input = get_connection_params()
        key = gen_key(key_input)
        
        try:
            client = start_client(host, port)
            print("\nConnected to server")
            
            def print_message(msg):
                print(f"Server# {msg}")
                
            receive_messages(client, key, print_message)
            
            while True:
                message = input()
                if message.lower() == 'exit':
                    break
                client.sendall(encrypt(message, key))
        finally:
            client.close()
    
    elif choice == "2":

        host, port, key_input = get_connection_params()
        key = gen_key(key_input)
        
        try:
            server = start_server(host, port)
            print("Server started, waiting for connections...")
            
            client_socket, addr = server.accept()
            print(f"Connection from {addr}")
            
            def print_message(msg):
                print(f"Client# {msg}")
                
            receive_messages(client_socket, key, print_message)
            
            while True:
                message = input()
                if message.lower() == 'exit':
                    break
                client_socket.sendall(encrypt(message, key))
        finally:
            client_socket.close()
            server.close()

if __name__ == "__main__":
    main()