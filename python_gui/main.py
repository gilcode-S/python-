# pyQT5 introduction

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
# boiler code to keep running:


class MainWindow(QMainWindow):
    def __init__(self,):
        super().__init__()
        # GUI winodw size
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700, 300, 500, 500)
        self.button = QPushButton("Click me", self)
        self.label = QLabel("Hello", self)
        self.initUI()

        # GUI windows label
        # label = QLabel("Hello", self)
        # label.setFont(QFont("Arial", 30))
        # label.setGeometry(0, 0, 500, 100)
        # label.setStyleSheet("color: black;"
        #                     "background-color: skyblue;"
        #                     "font-weight: bold;"
        #                     "font-style: italic;"
        #                     "text-decoration: underline;")
        # label.setAlignment(Qt.AlignTop)
        # label.setAlignment(Qt.AlignBottom)
        # label.setAlignment(Qt.AlignRight)
        # label.setAlignment(Qt.AlignHcenter)
        # abel.setAlignment(Qt.AlignCenter)

        # display image
        # label = QLabel(self)
        # label.setGeometry(0, 0, 250, 250)

        # pixmap = QPixmap("python_gui/me2026.jpg")
        # label.setPixmap(pixmap)

        # label.setScaledContents(True)

        # label.setGeometry((self.width() - label.width()) // 2,
        #                   (self.height() - label.height()) // 2,
        #                   label.width(),
        #                   label.height())

        # common practice if the code was too long and messy

    # def initUI(self):
    #     central_widget = QWidget()
    #     self.setCentralWidget(central_widget)

    #     label1 = QLabel("#1", self)
    #     label2 = QLabel("#2", self)
    #     label3 = QLabel("#3", self)
    #     label4 = QLabel("#4", self)
    #     label5 = QLabel("#5", self)

    #     label1.setStyleSheet("background-color: red;")
    #     label2.setStyleSheet("background-color: yellow;")
    #     label3.setStyleSheet("background-color: green;")
    #     label4.setStyleSheet("background-color: blue;")
    #     label5.setStyleSheet("background-color: purple;")

        # vertical layout manage

        # vbox = QVBoxLayout()

        # vbox.addWidget(label1)T
        # vbox.addWidget(label2)
        # vbox.addWidget(label3)
        # vbox.addWidget(label4)
        # vbox.addWidget(label5)

        # central_widget.setLayout(vbox)

        # horizontal layout manage
        # hbox = QHBoxLayout()

        # hbox.addWidget(label1)
        # hbox.addWidget(label2)
        # hbox.addWidget(label3)
        # hbox.addWidget(label4)
        # hbox.addWidget(label5)

        # central_widget.setLayout(hbox)

        # grid layout
        # gbox = QGridLayout()

        # gbox.addWidget(label1, 0, 0)
        # gbox.addWidget(label2, 0, 1)
        # gbox.addWidget(label3,  1, 0)
        # gbox.addWidget(label4,  1, 1)
        # gbox.addWidget(label5, 2, 2)

        # central_widget.setLayout(gbox)

    def initUI(self):

        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)
        self.label.setGeometry(150, 300, 200, 100)
        self.label.setStyleSheet('font-size:50px;')

    def on_click(self):
        self.label.setText("Goodbye")


def main():
    app = QApplication(sys.argv)
    # GUI run the window and close exec_
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
