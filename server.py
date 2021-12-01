import socket
import threading

HOST = '127.0.0.1'
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(2)

clients = []

def broadcast(move):
    for client in clients:
        client.send(move)

def handle(client):
    while True:
        try:
            move = client.recv(1024)
            broadcast(move)
        except:
            clients.remove(client)
            client.close()
            break


def receive():
    client, address = server.accept()
    print(f"client with address: {address} has connected")
    clients.append(client)
    thread = threading.Thread(target=handle, args=(client, ))
    thread.start()