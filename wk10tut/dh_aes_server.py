import socket
import json
import hashlib
from cryptography.fernet import Fernet
import base64
HOST = "0.0.0.0"
PORT = 8000
p = 23
g = 5
server_private = 6
server_public = (g ** server_private) % p
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print("DH + AES server listening on port", PORT)
conn, addr = server.accept()
print("Connected by", addr)
data = conn.recv(4096).decode()
client_data = json.loads(data)
client_public = client_data["client_public"]
conn.sendall(json.dumps({"server_public": server_public}).encode())
shared_secret = (client_public ** server_private) % p
print("Shared secret:", shared_secret)
key_material = hashlib.sha256(str(shared_secret).encode()).digest()
fernet_key = base64.urlsafe_b64encode(key_material)
cipher = Fernet(fernet_key)
encrypted_message = conn.recv(4096)
print("Encrypted received:", encrypted_message)
decrypted_message = cipher.decrypt(encrypted_message)
print("Decrypted message:", decrypted_message.decode())
encrypted_reply = cipher.encrypt(b"Hello from DH AES server 102")
conn.sendall(encrypted_reply)
conn.close()
server.close()
