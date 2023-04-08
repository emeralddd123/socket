import socket
import logging

port = 4040
noOfClients = 3

s = socket.socket()
logging.info("Socket created")
print(f"Socket created on {port}")

s.bind(('localhost', port))
s.listen(noOfClients)
logging.info("waiting for clients connections...")
print("Waiting for clients connections...")
while True:
    client, address = s.accept()
    name = client.recv(1024).decode("utf-8")
    logging.info(f"{name} connected with {address}")
    print(f"{name} connected with {address}")
    client.send(bytes("welcome to Usman Socket", encoding="utf-8"))
    
    client.close()
    