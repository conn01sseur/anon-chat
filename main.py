from network import start_client, start_server, receive_messages
from crypto import gen_key, encrypt, decrypt
from ui import show_banner, get_connection_params
from config import DEFAULT_HOST, DEFAULT_PORT

def main():
    show_banner(DEFAULT_HOST, DEFAULT_PORT)
    choice = input("--> ")
    
    if choice == "1":
        host, port, key_input = get_connection_params()
        key = gen_key(key_input)
        client = None
        
        try:
            client = start_client(host, port)
            if not client:
                return
                
            print("\nConnected to server")
            
            def handle_message(data):
                try:
                    print(f"Server# {decrypt(data, key)}")
                except Exception as e:
                    print(f"Decryption error: {e}")
            
            receive_messages(client, key, handle_message)
            
            while True:
                message = input()
                if message.lower() == 'exit':
                    break
                client.sendall(encrypt(message, key))
                
        except KeyboardInterrupt:
            print("\nClosing connection...")
        finally:
            if client:
                client.close()
    
    elif choice == "2":
        host, port, key_input = get_connection_params()
        key = gen_key(key_input)
        server = None
        client_socket = None
        
        try:
            server = start_server(host, port)
            if not server:
                return
                
            print("Server started, waiting for connections...")
            
            client_socket, addr = server.accept()
            print(f"Connection from {addr}")
            
            def handle_message(data):
                try:
                    print(f"Client# {decrypt(data, key)}")
                except Exception as e:
                    print(f"Decryption error: {e}")
            
            receive_messages(client_socket, key, handle_message)
            
            while True:
                message = input()
                if message.lower() == 'exit':
                    break
                client_socket.sendall(encrypt(message, key))
                
        except KeyboardInterrupt:
            print("\nShutting down server...")
        finally:
            if client_socket:
                client_socket.close()
            if server:
                server.close()

if __name__ == "__main__":
    main()