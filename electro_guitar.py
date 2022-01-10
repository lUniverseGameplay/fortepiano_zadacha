import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(808, 892)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 491, 851))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("electroguitar3.jpg"))
        self.label.setObjectName("label")
        self.second = QtWidgets.QPushButton(self.centralwidget)
        self.second.setGeometry(QtCore.QRect(240, 170, 5, 400))
        self.second.setText("")
        self.second.setObjectName("second")
        self.first = QtWidgets.QPushButton(self.centralwidget)
        self.first.setGeometry(QtCore.QRect(230, 170, 5, 400))
        self.first.setAutoFillBackground(False)
        self.first.setText("")
        self.first.setObjectName("first")
        self.third = QtWidgets.QPushButton(self.centralwidget)
        self.third.setGeometry(QtCore.QRect(250, 170, 5, 400))
        self.third.setText("")
        self.third.setObjectName("third")
        self.fourth = QtWidgets.QPushButton(self.centralwidget)
        self.fourth.setGeometry(QtCore.QRect(260, 170, 5, 400))
        self.fourth.setText("")
        self.fourth.setObjectName("fourth")
        self.fifth = QtWidgets.QPushButton(self.centralwidget)
        self.fifth.setGeometry(QtCore.QRect(270, 170, 5, 400))
        self.fifth.setText("")
        self.fifth.setObjectName("fifth")
        self.sixth = QtWidgets.QPushButton(self.centralwidget)
        self.sixth.setGeometry(QtCore.QRect(280, 170, 5, 400))
        self.sixth.setText("")
        self.sixth.setObjectName("sixth")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(500, 10, 301, 181))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Нажмите кнопки 1,2,3,4,5,6 для игры</span></p></body></html>"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load_mp3('Zvuki_strun_gitary/1st.mp3')
        self.zv = ['1st', '2nd', '3rd', '4th', '5th', '6th']
        self.first.setStyleSheet(
                "background-color: red")
        self.second.setStyleSheet(
                "background-color: red")
        self.third.setStyleSheet(
                "background-color: red")
        self.fourth.setStyleSheet(
                "background-color: red")
        self.fifth.setStyleSheet(
                "background-color: red")
        self.sixth.setStyleSheet(
                "background-color: red")

        self.first.clicked.connect(lambda: self.sound(1))
        self.second.clicked.connect(lambda: self.sound(2))
        self.third.clicked.connect(lambda: self.sound(3))
        self.fourth.clicked.connect(lambda: self.sound(4))
        self.fifth.clicked.connect(lambda: self.sound(5))
        self.sixth.clicked.connect(lambda: self.sound(6))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_1:
            self.sound(1)
        if event.key() == Qt.Key_2:
            self.sound(2)
        if event.key() == Qt.Key_3:
            self.sound(3)
        if event.key() == Qt.Key_4:
            self.sound(4)
        if event.key() == Qt.Key_5:
            self.sound(5)
        if event.key() == Qt.Key_6:
            self.sound(6)

    def sound(self, i):
        print(i)
        self.player.stop()
        self.load_mp3('Zvuki_strun_gitary/' + self.zv[i - 1] + '.mp3')
        self.player.play()

    def load_mp3(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())