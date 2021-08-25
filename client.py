from socket import *
class Client:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.connect((self.ip, int(self.port)))
        print('연결 확인 됐습니다.')



    def send_message(self, message):
        self.client.send(message.encode('utf-8'))
        print('메시지를 전송했습니다.')


# clientSock = socket(AF_INET, SOCK_STREAM)
# clientSock.connect(('127.0.0.1', 8060))
    def recv_message(self):
        data = self.client.recv(1024)
        print('받은 데이터 : ', data.decode('utf-8'))