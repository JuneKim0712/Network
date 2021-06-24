import socket
import threading


HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
# change it if server is changed
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    msg = str(msg)
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    return


def listen():
    while True:
        inMsg = client.recv(2 ** 16).decode(FORMAT)
        print(inMsg + '\n' + '>>> ', end='')
        continue
    return


def client_start():
    while True:
        username = input('username: ')
        send(username)
        inMsg = client.recv(2 ** 8).decode(FORMAT)

        if inMsg == '1':
            connection = True
            break

        print('The Username is already taken, please type different username')
        continue

    thread = threading.Thread(target=listen)
    thread.start()

    while connection:
        sending = input('>>> ')

        if sending == 'disconnect':
            send(DISCONNECT_MESSAGE)
            break

        send(sending)
        continue
    return

client_start()