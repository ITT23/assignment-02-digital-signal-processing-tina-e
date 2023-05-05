from StreamAnalyzer import StreamAnalyzer
from pynput.keyboard import Key, Controller


class WhistlingInputDevice:
    def __init__(self):
        self.analyzer = StreamAnalyzer()
        self.keyboard = Controller()

    def update(self, data):
        '''
        handle frequency change by updating simulating key events
        :param data: audio stream data
        '''
        analyzer_result = self.analyzer.analyze_data(data)
        if analyzer_result == 'UP':
            self.keyboard.press(Key.up)
            self.keyboard.release(Key.up)
        elif analyzer_result == 'DOWN':
            self.keyboard.press(Key.down)
            self.keyboard.release(Key.down)
