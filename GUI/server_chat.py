from PyQt5.QtWidgets import  QApplication, QWidget, QDesktopWidget, QPushButton, QLineEdit, QLabel, QGridLayout, QPlainTextEdit
from server import Server

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
        layout.addWidget(chatBtn, 1, 2, 2, 1)
        chatBtn.clicked.connect(self.open)

        endBtn = QPushButton('채팅방 종료')
        endBtn.setObjectName('endBtn')
        layout.addWidget(endBtn, 1, 3, 2, 3)

        label5 = QLabel('내 IP')
        label5.setObjectName('label5')
        layout.addWidget(label5, 4, 1)

        myipInput = QLineEdit()
        myipInput.setObjectName('myipInput')
        layout.addWidget(myipInput, 4, 2)


        label4 = QLabel('닉네임')
        label4.setObjectName('label4')
        layout.addWidget(label4, 5, 0)

        nameInput = QLineEdit()
        nameInput.setObjectName('nameInput')
        layout.addWidget(nameInput, 5, 1)

        nameBtn = QPushButton('변경')
        nameBtn.setObjectName('nameBtn')
        layout.addWidget(nameBtn, 5, 2)

        chat = QPlainTextEdit()
        chat.setObjectName('chat')
        layout.addWidget(chat, 6, 0, 1, -1)

        chatMessage = QLineEdit()
        chatMessage.setObjectName('chatMessage')
        layout.addWidget(chatMessage, 7, 0, 1, 2)

        messageBtn = QPushButton('보내기')
        messageBtn.setObjectName('messageBtn')
        layout.addWidget(messageBtn, 7, 2, 1, -1)


        self.setWindowTitle('서버')
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
        self.server = Server(self.ip, self.port)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ClientApp()
    sys.exit(app.exec_())