import socket

client = socket.socket()

client.connect(('127.0.0.1',4040))

name = input("Enter your name: ")

client.send(bytes(name, encoding='utf-8'))

print(client.recv(1024).decode('utf-8'))