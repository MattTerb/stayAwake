# Move mouse after a specified period of inactivity to prevent computer from falling asleep

import pyautogui, time, rumps, logging, sys

from PyQt5.QtWidgets import (
    QApplication, QDialog
)

from stayAwake_ui import Ui_Dialog
 
 
class Window(QDialog, Ui_Dialog):

    logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(message)s', level=logging.DEBUG)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
       # self.connectSignalsSlots()

    
    #def connectSignalsSlots(self):
          #  self.action_Exit.triggered.connect(self.setInterval)


    def setInterval(self,sender,interval):
        self.interval = interval
        logging.debug(f'{str(self.interval)} interval set')


    # TODO: Check if no activity after specified period

    def checkActivity(self,sender,interval):
        start = time.time()
        self.running = True

        while self.running:

            if self.running == False:
                break

            position1 = pyautogui.position()
            print('Pos1 = ' + str(position1))
            logging.debug(f'Pos1 = {str(position1)}')

            time.sleep(0.5)

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

                if elapsed >= interval:
                    print('Move mouse')
                    logging.debug('Move mouse')
                    pyautogui.moveRel(100,0, duration=1)
                    pyautogui.moveRel(-100,0, duration=1)
                    start = time.time()


    def stop():
        self.running = False
        logging.debug('Stop')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())