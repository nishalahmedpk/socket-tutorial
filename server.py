import socket
import threading
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR = (SERVER,PORT)
server.bind(ADDR)
FORMAT = 'utf-8'
DISCON = 'exit'

def handle_client(conn,addr):
    print(f'{addr} connected.')
    while True:
        msglen = conn.recv(HEADER).decode(FORMAT)     

        #will run into error if ran without any message
        if msglen:
            msglen = int(msglen)
            msg = conn.recv(msglen).decode(FORMAT)
            if msg == DISCON:
                break
            else:
                print(f'[{socket.gethostname}] {msg}')
        


def start():
    server.listen()
    print(f'[IP] {SERVER}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[ACTIVE] {threading.active_count()-1}')

start()