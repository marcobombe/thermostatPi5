from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtCore import QFile, QTextStream

target_temp = 0.0

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('thermostatPi5.ui', self)

        self.button = self.findChild(QtWidgets.QPushButton, 'printButton')
        #self.button.clicked.connect(self.printButtonPressed)

        self.quitButton = self.findChild(QtWidgets.QPushButton, 'quitButton')
        self.quitButton.clicked.connect(self.quitButtonPressed)

        self.incButton = self.findChild(QtWidgets.QPushButton, 'incButton')
        self.incButton.clicked.connect(self.incButtonPressed)

        self.decButton = self.findChild(QtWidgets.QPushButton, 'decButton')
        self.decButton.clicked.connect(self.decButtonPressed)

        #self.input = self.findChild(QtWidgets.QLineEdit, 'input')

        self.actualTempLabel = self.findChild(QtWidgets.QLabel, 'actualTempLabel')

        self.showFullScreen()

    def location_on_the_screen(self):
        x = 0
        y = 0
        self.move(x, y)

    #def printButtonPressed(self):
        # This is executed when the button is pressed
        #print('Input text:' + self.input.text())

    def quitButtonPressed(self):
        # This is executed when the button is pressed
        print('Quit!')
        sys.exit()

    def incButtonPressed(self):
        global target_temp
        # This is executed when the button is pressed
        print('Inc pressed!')
        target_temp = target_temp + 1.0
        print('Target temp is ' + str(target_temp))
        self.actualTempLabel.setText(str(target_temp))

    def decButtonPressed(self):
        global target_temp
        # This is executed when the button is pressed
        print('dec pressed!')
        target_temp = target_temp - 1.0
        print('Target temp is ' + str(target_temp))
        self.actualTempLabel.setText(str(target_temp))
        print ('Label text = ' + self.actualTempLabel.text())


app = QtWidgets.QApplication(sys.argv)
file = QFile("style.qss")
file.open(QFile.ReadOnly | QFile.Text)
stream = QTextStream(file)
app.setStyleSheet(stream.readAll())
window = Ui()
window.location_on_the_screen()
app.exec_()
