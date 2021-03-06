from PyQt5.QtWidgets import  QApplication, QWidget, QDesktopWidget, QPushButton, QLineEdit, QLabel, QGridLayout, QPlainTextEdit
from client import Client
import sys

class ClientApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QGridLayout()
        self.setLayout(layout)

        label1 = QLabel('채팅방 정보')
        label1.setObjectName('label1')
        layout.addWidget(label1, 0, 0, 1, -1)

        label2 = QLabel('IP')
        label2.setObjectName('label2')
        layout.addWidget(label2, 1, 0, 1, 1)

        self.ipInput = QLineEdit()
        self.ipInput.setObjectName('ipInput')
        layout.addWidget(self.ipInput, 1, 1)

        label3 = QLabel('PORT')
        label3.setObjectName('label3')
        layout.addWidget(label3, 2, 0)

        self.portInput = QLineEdit()
        self.portInput.setObjectName('portInput')
        layout.addWidget(self.portInput, 2, 1)


        chatBtn = QPushButton('채팅방 열기')
        chatBtn.setObjectName('chatBtn')
        chatBtn.clicked.connect(self.open)
        layout.addWidget(chatBtn, 1, 2, 2, 1)

        endBtn = QPushButton('채팅방 종료')
        endBtn.setObjectName('endBtn')
        layout.addWidget(endBtn, 1, 3, 2, 3)


        label4 = QLabel('닉네임')
        label4.setObjectName('label4')
        layout.addWidget(label4, 4, 0)

        nameInput = QLineEdit()
        nameInput.setObjectName('nameInput')
        layout.addWidget(nameInput, 4, 1)

        nameBtn = QPushButton('변경')
        nameBtn.setObjectName('nameBtn')
        layout.addWidget(nameBtn, 4, 2)

        chat = QPlainTextEdit()
        chat.setObjectName('chat')
        layout.addWidget(chat, 5, 0, 1, -1)

        self.chatMessage = QLineEdit()
        self.chatMessage.setObjectName('chatMessage')
        layout.addWidget(self.chatMessage, 6, 0, 1, 2)

        messageBtn = QPushButton('보내기')
        messageBtn.setObjectName('messageBtn')
        layout.addWidget(messageBtn, 6, 2, 1, -1)
        messageBtn.clicked.connect(self.send)


        self.setWindowTitle('클라이언트')
        self.resize(700, 800)
        self.center()
        self.show()


    def center(self):
        # 창의 위치와 크기 정보 가져오기
        qr = self.frameGeometry()
        # 사용하는 모니터 가운데 위치
        cp = QDesktopWidget().availableGeometry().center()
        # 창의 중심을 화면의 중심으로 이동
        qr.moveCenter(cp)
        # 현재의 창을 qr의 위치로 옮긴다.
        self.move(qr.topLeft())


    def open(self):
        self.ip = self.ipInput.text()
        self.port = self.portInput.text()
        self.client = Client(self.ip, self.port)

    def send(self):
        message = self.chatMessage.text()
        if self.client:
            self.client.send_message(message)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ClientApp()
    sys.exit(app.exec_())
