import socket
import threading
from encryption import encrypt_message, decrypt_message

HOST = '0.0.0.0'  
PORT = 65432       

def start_server(password):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[SERVER STARTED] Listening on port {PORT}...")

    def handle_client(conn, addr):
        print(f"[NEW CONNECTION] {addr} connected.")
        encrypted_data = conn.recv(1024).decode()
        message = decrypt_message(encrypted_data, password)
        print(f"[MESSAGE RECEIVED] {addr}: {message}")
        conn.close()

    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

def send_message(target_ip, message, password):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, PORT))
    encrypted_message = encrypt_message(message, password)
    client.send(encrypted_message.encode())
    client.close()

if __name__ == "__main__":
    mode = input("Choose mode (server/client): ").lower()
    password = input("Enter encryption password: ")

    if mode == 'server':
        start_server(password)
    else:
        target_ip = input("Enter recipient IP: ")
        message = input("Enter your message: ")
        send_message(target_ip, message, password)
