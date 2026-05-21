import socket
from cryptography.fernet import Fernet
HOST = "0.0.0.0"
PORT = 7000
key = b"6j9TtZ5eFdW3MzpN4tGQ7oQlzMuRuCMXxFsOHF9Coz4="
cipher = Fernet(key)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print("AES server listening on port", PORT)
conn, addr = server.accept()
print("Connected by", addr)
encrypted_data = conn.recv(4096)
print("Encrypted received:", encrypted_data)
decrypted_data = cipher.decrypt(encrypted_data)
print("Decrypted message:", decrypted_data.decode())
reply = cipher.encrypt(b"Hello from encrypted 102 server")
conn.sendall(reply)
conn.close()
server.close()
