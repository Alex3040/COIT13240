import socket
import json
import hashlib
from cryptography.fernet import Fernet
import base64
SERVER_IP = "192.168.56.102"
PORT = 8000
p = 23
g = 5
client_private = 15
client_public = (g ** client_private) % p
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))
client.sendall(json.dumps({"client_public": client_public}).encode())
data = client.recv(4096).decode()
server_data = json.loads(data)
server_public = server_data["server_public"]
shared_secret = (server_public ** client_private) % p
print("Shared secret:", shared_secret)
key_material = hashlib.sha256(str(shared_secret).encode()).digest()
fernet_key = base64.urlsafe_b64encode(key_material)
cipher = Fernet(fernet_key)
message = b"Hello from DH AES client 101"
encrypted_message = cipher.encrypt(message)
print("Plain message:", message)
print("Encrypted message:", encrypted_message)
client.sendall(encrypted_message)
encrypted_reply = client.recv(4096)
decrypted_reply = cipher.decrypt(encrypted_reply)
print("Encrypted reply:", encrypted_reply)
print("Decrypted reply:", decrypted_reply.decode())
client.close()
