import socket
import threading

HOST = "localhost"
PORT = 9090
FORMAT = "utf-8"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(2)

clients = []

def broadcast(move, client):
    print(move.decode(FORMAT))
    for cli in clients:
        if cli != client:
            cli.send(move)

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