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


def listen():
    while True:
        inMsg = client.recv(2 ** 16).decode(FORMAT)
        print(inMsg + '\n' + '>>> ', end='')


thread = threading.Thread(target=listen)
thread.start()

username = input('username: ')
send(username)
connection = True
while connection:
    sending = input('>>> ')
    if sending == 'disconnect':
        send(DISCONNECT_MESSAGE)
        break
    send(sending)
