from config import DEFAULT_HOST, DEFAULT_PORT

def show_banner(host, port):
    print(f"""
Your host: {host}
Your port: {port}

1. Connect (client)
2. Create server
3. Exit""")

def get_connection_params():
    host = input(f"Input host [{DEFAULT_HOST}]: ") or DEFAULT_HOST
    port = int(input(f"Input port [{DEFAULT_PORT}]: ") or DEFAULT_PORT)
    key = input("Crypt key: ")
    return host, port, key