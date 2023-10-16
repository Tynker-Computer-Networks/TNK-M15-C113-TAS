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

        # Receive player_name from player_socket
        player_name = player_socket.recv(1024).decode().strip()
            
        # Check if len() of CLIENTS is 0 (Check length of CLIENT.keys())
        if(len(CLIENTS.keys()) == 0):
            # Set player_name key in CLIENTS to value {'player_type' : 'player1'}
            CLIENTS[player_name] = {'player_type' : 'player1'}
        # else
        else:
            # Set player_name key in CLIENTS to value {'player_type' : 'player2'}
            CLIENTS[player_name] = {'player_type' : 'player2'}

        # Set Keys under player_name key as "player_socket", "address", "player_name", "turn"
        CLIENTS[player_name]["player_socket"] = player_socket
        CLIENTS[player_name]["address"] = addr
        CLIENTS[player_name]["player_name"] = player_name
        CLIENTS[player_name]["turn"] = False

        # Print Connection established with player_name : addr
        print(f"Connection established with {player_name} : {addr}")
        # Print all clients
        print(CLIENTS)

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
