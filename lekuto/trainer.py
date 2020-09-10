from time import sleep

class Trainer:
    def __init__(self, preproc=False):
        self.preproc = preproc

    def run(self):
        print('Collecting data...')
        print('Drop missing values.')
        print('Robust scaling.')
        print('Start training..')
        sleep(2)
        print('Stop training.')
        print('Deploy model')
        print('Done')

if __name__ == '__main__':
    Trainer().run()
