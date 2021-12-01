# Move mouse after a specified period of inactivity to prevent computer from falling asleep

from PyQt5 import QtGui
import pyautogui, time, rumps, logging, sys

from PyQt5.QtWidgets import (
    QApplication, QDialog
)

from stayAwake_ui import Ui_Dialog
 
 
class Window(QDialog, Ui_Dialog):


    logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(message)s', level=logging.DEBUG)
    logging.disable(logging.CRITICAL)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.minBox.valueChanged.connect(self.setMinInterval)
        self.secBox.valueChanged.connect(self.setSecInterval)
        self.startStopBtn.clicked.connect(self.buttonPush)

        self.btnState = False
        self.interval = 5
        self.running = False
        self.minInterval = 0
        self.secInterval = 0
        



    def setMinInterval(self):
        self.minInterval = self.minBox.value()
        logging.debug(f'{str(self.interval)} interval set')

    def setSecInterval(self):
        self.secInterval = self.secBox.value()
        logging.debug(f'{str(self.interval)} interval set')


    def buttonPush(self):

        if self.btnState == False:
            self.btnState = True
            self.statusLabel.setStyleSheet("background-color: rgba(3, 201, 169, 1);")
            self.statusLabel.setText("ON")
            self.startStopBtn.setText("Stop")
            self.checkActivity()
            print('Track on')
        else:
            self.btnState = False
            self.statusLabel.setStyleSheet("background-color: rgba(249, 14, 49, 153);")
            self.statusLabel.setText("OFF")
            self.startStopBtn.setText("Start")
            print('Track off')

            self.stop()



    # TODO: Check if no activity after specified period

    def checkActivity(self):

        self.interval = self.minInterval*60 + self.secInterval
        start = time.time()
        self.running = True


        while self.running:


            QtGui.QGuiApplication.processEvents()
            if self.running == False:
                break

            position1 = pyautogui.position()
            print('Pos1 = ' + str(position1))
            logging.debug(f'Pos1 = {str(position1)}')

            #time.sleep(0.5)

            position2 = pyautogui.position()
            print('Pos2 = ' + str(position2))
            logging.debug(f'Pos2 = {str(position2)}')


            if position1 != position2:
                print('Active')
                logging.debug('Active')
                start = time.time()
            else:
                print('Inactive')
                logging.debug('Inactive')

                end = time.time()
                elapsed = end - start
                print('Elapsed time: ' + str(elapsed))
                logging.debug(f'Elapsed time: {str(elapsed)}')

                if elapsed >= self.interval:
                    print('Move mouse')
                    logging.debug('Move mouse')
                    pyautogui.moveRel(100,0, duration=1)
                    pyautogui.moveRel(-100,0, duration=1)
                    start = time.time()


    def stop(self):
        self.running = False
        logging.debug('Stop')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())