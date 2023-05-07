import numpy as np


class StreamAnalyzer:
    def __init__(self):
        self.silence = 0
        self.frequencies = []
        self.registration = []
    def calculate_frequency(self, data):
        spectrum = np.abs(np.fft.fft(data))
        # get major frequency of spectrum
        freq = np.argmax(spectrum)
        return freq

    def analyze_data(self, data):
        '''
        capture current frequency and compare it to previous
        :param data: audio stream data
        :return: (UP, DOWN or NONE) detected frequency change
        '''
        current_freq = self.calculate_frequency(data)
        # filter silence / non-typical whistling frequencies
        if current_freq <= 15 or current_freq > 100:
            self.silence += 1
            self.registration = []
            return

        # skip comparison if no frequency captured before
        if len(self.frequencies) != 0:
            # if frequency higher than before
            if current_freq > self.frequencies[-1]:
                self.registration.append('h')
            # if frequency lower than before
            elif current_freq < self.frequencies[-1]:
                self.registration.append('l')

        self.frequencies.append(current_freq)
        return self.handle_data_change()

    def handle_data_change(self):
        '''
        analyze registered frequency change patterns
        as soon as there is an isolated sound with changing frequency
        :return: (UP, DOWN or NONE) detected frequency change
        '''
        len_registration = len(self.registration)
        if self.silence >= 10 and len_registration >= 3:
            self.silence = 0
            occurrence_lower = self.registration.count('l')
            occurrence_higher = self.registration.count('h')

            # detect decreasing frequency (most of the frequency changes were 'lower f than before')
            if occurrence_lower >= (0.6 * len_registration):
                self.frequencies = []
                self.registration = []
                return 'DOWN'
            # detect increasing frequency (most of the frequency changes were 'higher f than before')
            elif occurrence_higher >= (0.6 * len_registration):
                self.frequencies = []
                self.registration = []
                return 'UP'
        return 'NONE'

