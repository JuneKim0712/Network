import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handel_client(conn, addr):
    connected = True
    msg_length = conn.recv(HEADER).decode(FORMAT)
    if msg_length:
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        USERNAME = msg
        print('\n')
        print(f"{USERNAME} has connected")
        conn.send("Msg recieved".encode(FORMAT))
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            conn.send("Msg recieved".encode(FORMAT))
            if msg == DISCONNECT_MESSAGE:
                print(f"{USERNAME} has disconnected")
                connected = False
                break
            print(f"[{USERNAME}: {msg}]")
            conn.send("Msg recieved".encode(FORMAT))
            
    conn.close()


def start():
    server.listen()
    print(f"[Listening] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handel_client, args=(conn, addr))
        thread.start()
        print('')
        print(f"[Active Connections]: {threading.activeCount() - 1}")


print("Starting...")
start()