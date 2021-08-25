from socket import *

class Server:
    def __init__(self, ip, port):
        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.bind((ip, int(port)))
        self.server.listen(1)
        print('listen')

        self.connectionSock, self.addr = self.server.accept()

        print(str(self.addr),'에서 접속이 확인되었습니다.')
        if self.server.recv(1024):
            print('받은 데이터 : ', self.server.recv(1024).decode('utf-8'))
        else:
            print("no")

    def send_message(self, message):
        self.connectionSock.send(message.encode('utf-8'))
        print('메시지를 보냈습니다.')

    def recv_message(self):
        data = self.server.recv(1024)
        print('받은 데이터 : ', data.decode('utf-8'))
