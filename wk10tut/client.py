import socket

SERVER_IP = "192.168.56.102"
PORT = 6000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

client.sendall(b"Hello from 101 client")

data = client.recv(1024)
print("Received:", data.decode())

client.close()

