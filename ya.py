import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import QtCore, QtWidgets, QtMultimedia


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 350)
        Form.setMinimumSize(QtCore.QSize(650, 350))
        Form.setMaximumSize(QtCore.QSize(650, 350))
        self.D_btn = QtWidgets.QPushButton(Form)
        self.D_btn.setGeometry(QtCore.QRect(150, 80, 61, 221))
        self.D_btn.setText("")
        self.D_btn.setObjectName("D_btn")
        self.E_btn = QtWidgets.QPushButton(Form)
        self.E_btn.setGeometry(QtCore.QRect(220, 80, 61, 221))
        self.E_btn.setText("")
        self.E_btn.setObjectName("E_btn")
        self.F_btn = QtWidgets.QPushButton(Form)
        self.F_btn.setGeometry(QtCore.QRect(290, 80, 61, 221))
        self.F_btn.setText("")
        self.F_btn.setObjectName("F_btn")
        self.G_btn = QtWidgets.QPushButton(Form)
        self.G_btn.setGeometry(QtCore.QRect(360, 80, 61, 221))
        self.G_btn.setText("")
        self.G_btn.setObjectName("G_btn")
        self.A_btn = QtWidgets.QPushButton(Form)
        self.A_btn.setGeometry(QtCore.QRect(430, 80, 61, 221))
        self.A_btn.setText("")
        self.A_btn.setObjectName("A_btn")
        self.C_btn = QtWidgets.QPushButton(Form)
        self.C_btn.setGeometry(QtCore.QRect(80, 80, 61, 221))
        self.C_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.C_btn.setAutoFillBackground(False)
        self.C_btn.setText("")
        self.C_btn.setObjectName("C_btn")
        self.B_btn = QtWidgets.QPushButton(Form)
        self.B_btn.setGeometry(QtCore.QRect(500, 80, 61, 221))
        self.B_btn.setText("")
        self.B_btn.setObjectName("B_btn")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(450, 310, 16, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(520, 310, 16, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(380, 310, 16, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(320, 310, 16, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(250, 310, 16, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(180, 310, 16, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(110, 310, 16, 16))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "A"))
        self.label_2.setText(_translate("Form", "B"))
        self.label_3.setText(_translate("Form", "G"))
        self.label_4.setText(_translate("Form", "F"))
        self.label_5.setText(_translate("Form", "E"))
        self.label_6.setText(_translate("Form", "D"))
        self.label_7.setText(_translate("Form", "C"))


class MyWidget(QMainWindow, Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.player = QtMultimedia.QMediaPlayer()
        self.A_btn.clicked.connect(self.A_run)
        self.B_btn.clicked.connect(self.B_run)
        self.C_btn.clicked.connect(self.C_run)
        self.D_btn.clicked.connect(self.D_run)
        self.E_btn.clicked.connect(self.E_run)
        self.F_btn.clicked.connect(self.F_run)
        self.G_btn.clicked.connect(self.G_run)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_A:
            self.A_run()
        elif event.key() == QtCore.Qt.Key.Key_B:
            self.B_run()
        elif event.key() == QtCore.Qt.Key.Key_C:
            self.C_run()
        elif event.key() == QtCore.Qt.Key.Key_D:
            self.D_run()
        elif event.key() == QtCore.Qt.Key.Key_E:
            self.E_run()
        elif event.key() == QtCore.Qt.Key.Key_F:
            self.F_run()
        elif event.key() == QtCore.Qt.Key.Key_G:
            self.G_run()

    def A_run(self):
        content = QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(
            'source/A.mp3'))
        self.player.setMedia(content)
        self.player.play()

    def B_run(self):
        content = QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(
            'source/B.mp3'))
        self.player.setMedia(content)
        self.player.play()

    def C_run(self):
        content = QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(
            'source/C.mp3'))
        self.player.setMedia(content)
        self.player.play()

    def D_run(self):
        content = QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(
            'source/D.mp3'))
        self.player.setMedia(content)
        self.player.play()

    def E_run(self):
        content = QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(
            'source/E.mp3'))
        self.player.setMedia(content)
        self.player.play()

    def F_run(self):
        content = QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(
            'source/F.mp3'))
        self.player.setMedia(content)
        self.player.play()

    def G_run(self):
        content = QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(
            'source/G.mp3'))
        self.player.setMedia(content)
        self.player.play()

    def H_run(self):
        content = QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(
            'source/H.mp3'))
        self.player.setMedia(content)
        self.player.play()

    def run(self):
        math = self.textEdit.toPlainText()
        self.widget.clear()
        self.widget.plot([eval(math.replace('x', str(i)))
                          for i in range(int(self.start.toPlainText()),
                                         int(self.end.toPlainText()))],
                         [i for i in range(int(self.start.toPlainText()),
                                           int(self.end.toPlainText()))],
                         pen='r')


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
