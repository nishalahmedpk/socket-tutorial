from email import message
import socket
import threading
HEADER = 64
PORT = 5050
SERVER = input('IP: ')
FORMAT = 'utf-8'
DISCON = 'exit'
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msglen = len(message)
    sendlen = str(msglen).encode(FORMAT)
    sendlen += b' ' * (HEADER - len(sendlen))
    client.send(sendlen)
    client.send(message)

while True:
    x = input('msg: ')
    send(x)
