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

global allConn, allUserName
allConn, allUserName = [], []


def handel_client(conn, addr):
    global allConn, allUserName
    connected = True
    return

    while True:
        msg_length = conn.recv(HEADER).decode(FORMAT)

        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg in allUserName:
                conn.send(('0').encode(FORMAT))
                continue

            conn.send(('1').encode(FORMAT))
            allUserName.append(msg)
            USERNAME = msg
            print('\n')
            print(f"{USERNAME} has connected")
            allConn.append(conn)
            send(f"{USERNAME} has connected", conn)
            break

    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                print(f"{USERNAME} has disconnected")
                send(f"{USERNAME} has disconnected", conn)
                connected = False
                break

            print(f"[{USERNAME}: {msg}]")
            send(f"{USERNAME}: {msg}", conn)

    conn.close()
    return


def send(message, conn):
    global allConn

    conns = allConn.copy()
    conns.remove(conn)
    message = message.encode(FORMAT)

    for conn in conns:
        conn.send(message)
        continue
    return
    


def server_start():
    print("Starting...")
    server.listen()
    print(f"[Listening] Server is listening on {SERVER}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handel_client, args=(conn, addr))
        thread.start()
        print('')
        print(f"[Active Connections]: {threading.activeCount() - 1}")
        continue
    return


server_start()