

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.btn1 = QPushButton("#1")
        self.btn2 = QPushButton("#2")
        self.btn3 = QPushButton("#3")

        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)
        hbox.addWidget(self.btn3)

        central_widget.setLayout(hbox)

        self.btn1.setObjectName("btn1")
        self.btn2.setObjectName("btn2")
        self.btn3.setObjectName("btn3")

        self.setStyleSheet("""
            QPushButton{
                font-size:24px;
                font-family: Arial;
                padding: 15px 75px;
                margin: 25px;
                border: 3px solid;
                border-radius: 15px;
            }
            QPushButton#btn1{
                background-color: red;
            }
            QPushButton#btn2{
                background-color: green;
                }
            QPushButton#btn3{
                background-color: skyblue;
            }
            QPushButton#btn1:hover{
            background-color: #FF7F7F;
            }
            QPushButton#btn2:hover{
                background-color:#90EE90;
            }
            QPushButton#btn3:hover{
                background-color: blue;
            }
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
