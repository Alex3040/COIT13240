import socket
from cryptography.fernet import Fernet
SERVER_IP = "192.168.56.102"
PORT = 7000
key = b"6j9TtZ5eFdW3MzpN4tGQ7oQlzMuRuCMXxFsOHF9Coz4="
cipher = Fernet(key)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))
message = b"Hello encrypted message from 101"
encrypted_message = cipher.encrypt(message)
print("Plain message:", message)
print("Encrypted message:", encrypted_message)
client.sendall(encrypted_message)
encrypted_reply = client.recv(4096)
decrypted_reply = cipher.decrypt(encrypted_reply)
print("Encrypted reply:", encrypted_reply)
print("Decrypted reply:", decrypted_reply.decode())
client.close()
