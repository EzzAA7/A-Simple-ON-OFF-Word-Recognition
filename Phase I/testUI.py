from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from recordTest import recordTest

class Ui_MainWindow(recordTest):
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.setupUi(MainWindow)
        super(Ui_MainWindow, self).__init__()
        self.labelAvgOn_2.setText(str(self.energyOFF))
        self.labelAvgOn_3.setText(str(self.energyON))
        self.accuray=0
        MainWindow.show()
        sys.exit(app.exec_())

        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 602)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.labelAvgOn = QtWidgets.QLabel(self.centralwidget)
        self.labelAvgOn.setGeometry(QtCore.QRect(80, 20, 271, 31))
        self.labelAvgOn.setStyleSheet('color: white')
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelAvgOn.setFont(font)
        self.labelAvgOn.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAvgOn.setObjectName("labelAvgOn")

        self.labelAvgOff = QtWidgets.QLabel(self.centralwidget)
        self.labelAvgOff.setGeometry(QtCore.QRect(80, 60, 271, 21))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelAvgOff.setFont(font)
        self.labelAvgOff.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAvgOff.setObjectName("labelAvgOff")
        self.labelAvgOff.setStyleSheet('color: white')
        self.labelAvgOn_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelAvgOn_2.setGeometry(QtCore.QRect(350, 20, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelAvgOn_2.setFont(font)
        self.labelAvgOn_2.setText("")
        self.labelAvgOn_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAvgOn_2.setObjectName("labelAvgOn_2")
        self.labelAvgOn_3 = QtWidgets.QLabel(self.centralwidget)
        self.labelAvgOn_3.setGeometry(QtCore.QRect(360, 50, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelAvgOn_3.setFont(font)
        self.labelAvgOn_3.setText("")
        self.labelAvgOn_3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAvgOn_3.setObjectName("labelAvgOn_3")

        self.picSpeak = QtWidgets.QLabel(self.centralwidget)
        self.picSpeak.setGeometry(QtCore.QRect(570, 10, 221, 101))
        self.picSpeak.setText("")
        self.picSpeak.setPixmap(QtGui.QPixmap("speech-recognition.png"))
        self.picSpeak.setScaledContents(True)
        self.picSpeak.setObjectName("picSpeak")
        self.groupBox1 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox1.setGeometry(QtCore.QRect(70, 160, 141, 171))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox1.setFont(font)
        self.groupBox1.setObjectName("groupBox1")
        self.picVoice1 = QtWidgets.QLabel(self.groupBox1)
        self.picVoice1.setGeometry(QtCore.QRect(30, 30, 81, 61))
        self.picVoice1.setText("")
        self.picVoice1.setPixmap(QtGui.QPixmap("recording-ico.png"))
        self.picVoice1.setScaledContents(True)
        self.picVoice1.setObjectName("picVoice1")
        self.label = QtWidgets.QLabel(self.groupBox1)
        self.label.setGeometry(QtCore.QRect(20, 100, 111, 21))
        self.label.setObjectName("label")
        self.labelAnswer1 = QtWidgets.QLabel(self.groupBox1)
        self.labelAnswer1.setGeometry(QtCore.QRect(10, 120, 111, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelAnswer1.setFont(font)
        self.labelAnswer1.setText("")
        self.labelAnswer1.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAnswer1.setObjectName("labelAnswer1")
        self.groupBox2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox2.setGeometry(QtCore.QRect(210, 160, 141, 171))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(10)
        self.groupBox2.setFont(font)
        self.groupBox2.setObjectName("groupBox2")
        self.picVoice1_2 = QtWidgets.QLabel(self.groupBox2)
        self.picVoice1_2.setGeometry(QtCore.QRect(20, 30, 81, 61))
        self.picVoice1_2.setText("")
        self.picVoice1_2.setPixmap(QtGui.QPixmap("recording-ico.png"))
        self.picVoice1_2.setScaledContents(True)
        self.picVoice1_2.setObjectName("picVoice1_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox2)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 111, 21))
        self.label_3.setObjectName("label_3")
        self.labelAnswer2 = QtWidgets.QLabel(self.groupBox2)
        self.labelAnswer2.setGeometry(QtCore.QRect(10, 120, 111, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelAnswer2.setFont(font)
        self.labelAnswer2.setText("")
        self.labelAnswer2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAnswer2.setObjectName("labelAnswer2")
        self.groupBox3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox3.setGeometry(QtCore.QRect(350, 160, 141, 171))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(10)
        self.groupBox3.setFont(font)
        self.groupBox3.setObjectName("groupBox3")
        self.picVoice1_3 = QtWidgets.QLabel(self.groupBox3)
        self.picVoice1_3.setGeometry(QtCore.QRect(20, 30, 81, 61))
        self.picVoice1_3.setText("")
        self.picVoice1_3.setPixmap(QtGui.QPixmap("recording-ico.png"))
        self.picVoice1_3.setScaledContents(True)
        self.picVoice1_3.setObjectName("picVoice1_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox3)
        self.label_5.setGeometry(QtCore.QRect(20, 100, 111, 21))
        self.label_5.setObjectName("label_5")
        self.labelAnswer3 = QtWidgets.QLabel(self.groupBox3)
        self.labelAnswer3.setGeometry(QtCore.QRect(10, 120, 111, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelAnswer3.setFont(font)
        self.labelAnswer3.setText("")
        self.labelAnswer3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAnswer3.setObjectName("labelAnswer3")
        self.groupBox4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox4.setGeometry(QtCore.QRect(490, 160, 141, 171))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(10)
        self.groupBox4.setFont(font)
        self.groupBox4.setObjectName("groupBox4")
        self.picVoice1_4 = QtWidgets.QLabel(self.groupBox4)
        self.picVoice1_4.setGeometry(QtCore.QRect(20, 30, 81, 61))
        self.picVoice1_4.setText("")
        self.picVoice1_4.setPixmap(QtGui.QPixmap("recording-ico.png"))
        self.picVoice1_4.setScaledContents(True)
        self.picVoice1_4.setObjectName("picVoice1_4")
        self.label_7 = QtWidgets.QLabel(self.groupBox4)
        self.label_7.setGeometry(QtCore.QRect(20, 100, 111, 21))
        self.label_7.setObjectName("label_7")
        self.labelAnswer4 = QtWidgets.QLabel(self.groupBox4)
        self.labelAnswer4.setGeometry(QtCore.QRect(10, 120, 111, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelAnswer4.setFont(font)
        self.labelAnswer4.setText("")
        self.labelAnswer4.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAnswer4.setObjectName("labelAnswer4")
        self.groupBox4_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox4_2.setGeometry(QtCore.QRect(630, 160, 141, 171))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(10)
        self.groupBox4_2.setFont(font)
        self.groupBox4_2.setObjectName("groupBox4_2")
        self.picVoice1_5 = QtWidgets.QLabel(self.groupBox4_2)
        self.picVoice1_5.setGeometry(QtCore.QRect(20, 30, 81, 61))
        self.picVoice1_5.setText("")
        self.picVoice1_5.setPixmap(QtGui.QPixmap("recording-ico.png"))
        self.picVoice1_5.setScaledContents(True)
        self.picVoice1_5.setObjectName("picVoice1_5")
        self.label_10 = QtWidgets.QLabel(self.groupBox4_2)
        self.label_10.setGeometry(QtCore.QRect(20, 100, 111, 21))
        self.label_10.setObjectName("label_10")
        self.labelAnswer5 = QtWidgets.QLabel(self.groupBox4_2)
        self.labelAnswer5.setGeometry(QtCore.QRect(10, 120, 111, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelAnswer5.setFont(font)
        self.labelAnswer5.setText("")
        self.labelAnswer5.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAnswer5.setObjectName("labelAnswer5")
        self.radioButtonON = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonON.setGeometry(QtCore.QRect(250, 80, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(10)
        self.radioButtonON.setFont(font)
        self.radioButtonON.setObjectName("radioButtonON")
        self.radioButtonOFF = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonOFF.setGeometry(QtCore.QRect(400, 80, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(10)
        self.radioButtonOFF.setFont(font)
        self.radioButtonOFF.setObjectName("radioButtonOFF")
        self.labelAvgOff_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelAvgOff_2.setGeometry(QtCore.QRect(50, 90, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelAvgOff_2.setFont(font)
        self.labelAvgOff_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAvgOff_2.setObjectName("labelAvgOff_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 520, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lblAccuracy = QtWidgets.QLabel(self.centralwidget)
        self.lblAccuracy.setGeometry(QtCore.QRect(170, 520, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(10)
        self.lblAccuracy.setFont(font)
        self.lblAccuracy.setText("")
        self.lblAccuracy.setObjectName("lblAccuracy")
        self.btnReset = QtWidgets.QPushButton(self.centralwidget)
        self.btnReset.setGeometry(QtCore.QRect(610, 530, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(10)
        self.btnReset.setFont(font)
        self.btnReset.setCheckable(False)
        self.btnReset.setObjectName("btnReset")
        self.btnStart1 = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart1.setGeometry(QtCore.QRect(90, 320, 93, 41))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        self.btnStart1.setFont(font)
        self.btnStart1.setObjectName("btnStart1")
        self.btnStart2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart2.setGeometry(QtCore.QRect(240, 320, 93, 41))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        self.btnStart2.setFont(font)
        self.btnStart2.setObjectName("btnStart2")
        self.btnStart3 = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart3.setGeometry(QtCore.QRect(370, 320, 93, 41))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        self.btnStart3.setFont(font)
        self.btnStart3.setObjectName("btnStart3")
        self.btnStart4 = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart4.setGeometry(QtCore.QRect(510, 320, 93, 41))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        self.btnStart4.setFont(font)
        self.btnStart4.setObjectName("btnStart4")
        self.btnStart5 = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart5.setGeometry(QtCore.QRect(650, 320, 93, 41))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        self.btnStart5.setFont(font)
        self.btnStart5.setObjectName("btnStart5")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(40, 380, 731, 91))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("Voice.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, -10, 811, 621))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Telegram.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.label_4.raise_()
        self.labelAvgOn.raise_()
        self.labelAvgOff.raise_()
        self.picSpeak.raise_()
        self.groupBox1.raise_()
        self.groupBox2.raise_()
        self.groupBox3.raise_()
        self.groupBox4.raise_()
        self.groupBox4_2.raise_()
        self.radioButtonON.raise_()
        self.radioButtonOFF.raise_()
        self.labelAvgOff_2.raise_()
        self.label_2.raise_()
        self.lblAccuracy.raise_()
        self.btnReset.raise_()
        self.btnStart1.raise_()
        self.btnStart2.raise_()
        self.btnStart3.raise_()
        self.btnStart4.raise_()
        self.btnStart5.raise_()
        self.label_9.raise_()
        self.labelAvgOn_2.raise_()
        self.labelAvgOn_3.raise_()
        self.labelAvgOff_2.setStyleSheet('color: white')
        self.labelAvgOn_2.setStyleSheet('color: white')
        self.labelAvgOn_3.setStyleSheet('color: white')
        self.lblAccuracy.setStyleSheet('color: white')
        self.label_2.setStyleSheet('color: white')

        MainWindow.setCentralWidget(self.centralwidget)

        #self.btnReset.clicked.connect(self.Reset)
        self.btnStart1.clicked.connect(self.StartBtn1)
        self.btnStart2.clicked.connect(self.StartBtn2)
        self.btnStart3.clicked.connect(self.StartBtn3)
        self.btnStart4.clicked.connect(self.StartBtn4)
        self.btnStart5.clicked.connect(self.StartBtn5)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    # def Reset(self):
    #     ui2=Ui_MainWindow()
    
    # def updateAccuray(self):
    #     self.accuray +=1 

    def StartBtn1(self):
        if(self.radioButtonON.isChecked()):
            movie = QtGui.QMovie("gif.gif")
            self.picVoice1.setMovie(movie)
            self.picVoice1.setScaledContents(True)
            self.picVoice1.setWordWrap(False)
            movie.start()
            i=1
            self.recordTestON(self.cwdOG)
            self.labelAnswer1.setText(self.compareEnergyON(self.energyOFF,self.energyON,i))
            self.picVoice1.setPixmap(QtGui.QPixmap("recording-ico.png"))
            self.picVoice1.setScaledContents(True)

        elif(self.radioButtonOFF.isChecked()):
            movie = QtGui.QMovie("gif.gif")
            self.picVoice1.setMovie(movie)
            self.picVoice1.setScaledContents(True)
            self.picVoice1.setWordWrap(False)
            movie.start()
            i=1
            self.recordTestOFF(self.cwdOG)
            self.labelAnswer1.setText(self.compareEnergyOFF(self.energyOFF,self.energyON,i))

    def StartBtn2(self):
        if(self.radioButtonON.isChecked()):
            movie = QtGui.QMovie("gif.gif")
            self.picVoice1_2.setMovie(movie)
            self.picVoice1_2.setScaledContents(True)
            self.picVoice1_2.setWordWrap(False)
            movie.start()
            i=2
            self.recordTestON(self.cwdOG)
            self.labelAnswer2.setText(self.compareEnergyON(self.energyOFF,self.energyON,i))

        elif(self.radioButtonOFF.isChecked()):
            movie = QtGui.QMovie("gif.gif")
            self.picVoice1_2.setMovie(movie)
            self.picVoice1_2.setScaledContents(True)
            self.picVoice1_2.setWordWrap(False)
            movie.start()
            i=2
            self.recordTestOFF(self.cwdOG)
            self.labelAnswer2.setText(self.compareEnergyOFF(self.energyOFF,self.energyON,i))

    def StartBtn3(self):
        if(self.radioButtonON.isChecked()):
            movie = QtGui.QMovie("gif.gif")
            self.picVoice1_3.setMovie(movie)
            self.picVoice1_3.setScaledContents(True)
            self.picVoice1_3.setWordWrap(False)
            movie.start()
            i=3
            self.recordTestON(self.cwdOG)
            self.labelAnswer3.setText(self.compareEnergyON(self.energyOFF,self.energyON,i))

        elif(self.radioButtonOFF.isChecked()):
            movie = QtGui.QMovie("gif.gif")
            self.picVoice1_3.setMovie(movie)
            self.picVoice1_3.setScaledContents(True)
            self.picVoice1_3.setWordWrap(False)
            movie.start()
            i=3
            self.recordTestOFF(self.cwdOG)
            self.labelAnswer3.setText(self.compareEnergyOFF(self.energyOFF,self.energyON,i))

    def StartBtn4(self):
        if(self.radioButtonON.isChecked()):
            movie = QtGui.QMovie("gif.gif")
            self.picVoice1_4.setMovie(movie)
            self.picVoice1_4.setScaledContents(True)
            self.picVoice1_4.setWordWrap(False)
            movie.start()
            i=4
            self.recordTestON(self.cwdOG)
            self.labelAnswer4.setText(self.compareEnergyON(self.energyOFF,self.energyON,i))

        elif(self.radioButtonOFF.isChecked()):
            movie = QtGui.QMovie("gif.gif")
            self.picVoice1_4.setMovie(movie)
            self.picVoice1_4.setScaledContents(True)
            self.picVoice1_4.setWordWrap(False)
            movie.start()
            i=4
            self.recordTestOFF(self.cwdOG)
            self.labelAnswer4.setText(self.compareEnergyOFF(self.energyOFF,self.energyON,i))

    def StartBtn5(self):
        if(self.radioButtonON.isChecked()):
            movie = QtGui.QMovie("gif.gif")
            self.picVoice1_5.setMovie(movie)
            self.picVoice1_5.setScaledContents(True)
            self.picVoice1_5.setWordWrap(False)
            movie.start()
            i=5
            self.recordTestON(self.cwdOG)
            self.labelAnswer5.setText(self.compareEnergyON(self.energyOFF,self.energyON,i))

        elif(self.radioButtonOFF.isChecked()):
            movie = QtGui.QMovie("gif.gif")
            self.picVoice1_5.setMovie(movie)
            self.picVoice1_5.setScaledContents(True)
            self.picVoice1_5.setWordWrap(False)
            movie.start()
            i=5
            self.recordTestOFF(self.cwdOG)
            self.labelAnswer5.setText(self.compareEnergyOFF(self.energyOFF,self.energyON,i))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelAvgOn.setText(_translate("MainWindow", "The Average for ON sounds :"))
        self.labelAvgOff.setText(_translate("MainWindow", "The Average for OFF sounds :"))
        self.groupBox1.setTitle(_translate("MainWindow", "1st Voice Test"))
        self.label.setText(_translate("MainWindow", "Recognised As"))
        self.groupBox2.setTitle(_translate("MainWindow", "2nd Voice Test"))
        self.label_3.setText(_translate("MainWindow", "Recognised As"))
        self.groupBox3.setTitle(_translate("MainWindow", "3rd Voice Test"))
        self.label_5.setText(_translate("MainWindow", "Recognised As"))
        self.groupBox4.setTitle(_translate("MainWindow", "4th Voice Test"))
        self.label_7.setText(_translate("MainWindow", "Recognised As"))
        self.groupBox4_2.setTitle(_translate("MainWindow", "5th Voice Test"))
        self.label_10.setText(_translate("MainWindow", "Recognised As"))
        self.radioButtonON.setText(_translate("MainWindow", "ON"))
        self.radioButtonOFF.setText(_translate("MainWindow", "OFF"))
        self.labelAvgOff_2.setText(_translate("MainWindow", "Let\'s TEST :"))
        self.label_2.setText(_translate("MainWindow", "Accuracy:"))
        self.btnReset.setText(_translate("MainWindow", "Reset"))
        self.btnStart1.setText(_translate("MainWindow", "Start"))
        self.btnStart2.setText(_translate("MainWindow", "Start"))
        self.btnStart3.setText(_translate("MainWindow", "Start"))
        self.btnStart4.setText(_translate("MainWindow", "Start"))
        self.btnStart5.setText(_translate("MainWindow", "Start"))


if __name__ == "__main__":

    ui = Ui_MainWindow()


