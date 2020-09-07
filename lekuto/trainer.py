from time import sleep

class Trainer:
    def __init__(self, preproc=False):
        self.preproc = preproc

    def run(self):
        print('Collecting data...')
        print('Start training..')
        sleep(2)
        print('Stop training.')

if __name__ == '__main__':
    Trainer().run()
