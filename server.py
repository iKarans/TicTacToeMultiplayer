import socket
import threading

HOST = "localhost"
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

clients = []

def broadcast(move, client):
    for cli in clients:
        if cli != client:
            cli.send(move)
    print(len(clients))

def handle(client):
    while True:
        try:
            move = client.recv(1024)
            broadcast(move, client)
        except:
            clients.remove(client)
            client.close()
            break


def receive():
    while True:
        client, address = server.accept()
        print(f"client with address: {address} has connected")
        clients.append(client)
        thread = threading.Thread(target=handle, args=(client, ))
        thread.start()

receive()