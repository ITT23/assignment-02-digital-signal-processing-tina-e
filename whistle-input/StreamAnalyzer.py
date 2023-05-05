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
        current_freq = self.calculate_frequency(data)
        len_frequencies = len(self.frequencies)

        # filter silence
        if current_freq <= 15 or current_freq > 100:
            self.silence += 1
            self.registration = []
            return

        # skip comparison if no frequency captured before
        if len_frequencies != 0:
            # if frequency higher than before
            if current_freq > self.frequencies[-1]:
                self.registration.append('h')
            # if frequency lower than before
            elif current_freq < self.frequencies[-1]:
                self.registration.append('l')
            # if frequency same as before
            else:
                self.registration.append('s')

        self.frequencies.append(current_freq)
        return self.handle_data_change()

    def handle_data_change(self):
        len_registration = len(self.registration)
        if self.silence >= 5:
            self.silence = 0
            print(self.registration)
            occurrence_lower = self.registration.count('l')
            occurrence_higher = self.registration.count('h')

            # detect increasing frequency
            if occurrence_lower >= (0.6 * len_registration):
                self.frequencies = []
                self.registration = []
                return 'UP'
            # detect decreasing frequency
            elif occurrence_higher >= (0.6 * len_registration):
                self.frequencies = []
                self.registration = []
                return 'DOWN'
        return 'NONE'

