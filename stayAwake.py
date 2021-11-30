# Move mouse after a specified period of inactivity to prevent computer from falling asleep

import pyautogui, time, rumps, logging

 
 
class stayAwakeApp(object):

    logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(message)s', level=logging.DEBUG)

    def __init__(self):
        self.app = rumps.App("StayAwake","🐭")
        self.interval = 5 # seconds
        self.running = True
        self.fiveSecBtn = rumps.MenuItem(title="5 seconds",callback=lambda _: self.setInterval(_, 5)) 
        self.thirtyeSecBtn = rumps.MenuItem(title="30 seconds",callback=lambda _: self.setInterval(_, 30)) 
        self.oneMinBtn = rumps.MenuItem(title="1 minute",callback=lambda _: self.setInterval(_, 1*60)) 
        self.fiveMinBtn = rumps.MenuItem(title="5 minutes",callback=lambda _: self.setInterval(_, 5*60)) 
        self.tenMinBtn = rumps.MenuItem(title="10 minutes",callback=lambda _: self.setInterval(_, 10*60)) 
        self.fifteenMinBtn = rumps.MenuItem(title="15 minutes",callback=lambda _: self.setInterval(_,15*60)) 
        self.startBtn = rumps.MenuItem(title="Start",callback=lambda _: self.checkActivity(_, self.interval))
        self.stopBtn = rumps.MenuItem(title="Stop",callback=lambda _: self.stop)

        self.app.menu = [self.fiveSecBtn, self.thirtyeSecBtn, self.oneMinBtn, self.fiveMinBtn, self.tenMinBtn, self.fifteenMinBtn, self.startBtn, self.stopBtn]

        logging.debug('App Initialised')

    def run(self):
        self.app.run()



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


if __name__ == '__main__':
    app = stayAwakeApp()
    app.run()