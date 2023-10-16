import socket
from  threading import Thread

SERVER = None
PORT = None
IP_ADDRESS = None
CLIENTS = {}

def accept_connections():
    global CLIENTS
    global SERVER

    while True:
        player_socket, addr = SERVER.accept()
        print("Client Connected")

def setup():
    print("\n")
    print("\t\t\t\t\t\t*** LUDO LADDER ***")

    global SERVER
    global PORT
    global IP_ADDRESS

    IP_ADDRESS = '127.0.0.1'
    PORT = 5000
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    SERVER.listen(10)

    print("\t\t\t\tSERVER IS WAITING FOR INCOMING CONNECTIONS...")
    print("\n")

    accept_connections()

setup()
