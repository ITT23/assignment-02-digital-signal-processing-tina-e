from pyglet import shapes
import numpy as np


def calculate_frequency(data):
    spectrum = np.abs(np.fft.fft(data))
    # get major frequency of spectrum
    freq = np.argmax(spectrum)
    return freq


class Menu:
    def __init__(self, window_width, window_height):
        self.direction_flag_up = None
        self.silence = 0
        self.frequencies = []
        self.menu_items = []
        self.registration = []
        self.item_count = 5
        self.item_width = window_width
        self.item_height = window_height / self.item_count
        self.initial_item_color = (255, 255, 255)
        self.selected_item_color = (156, 0, 75)
        self.selected_item = 0
        self.init_items()

    def init_items(self):
        for i in range(0, self.item_count):
            item = shapes.BorderedRectangle(x=0, y=i * self.item_height, width=self.item_width, height=self.item_height,
                                            border=5, border_color=(0, 0, 0))
            self.menu_items.append(item)

    def up(self):
        if self.selected_item < self.item_count:
            self.selected_item += 1

    def down(self):
        if self.selected_item > 0:
            self.selected_item -= 1

    def analyze_data(self, data):
        current_freq = calculate_frequency(data)
        len_frequencies = len(self.frequencies)
        #self.frequencies.append(current_freq)

        # filter silence
        if current_freq <= 15 or current_freq > 100:
            self.silence += 1
            # print(f'silence: {current_freq}')
            self.registration = []
            return

        # no frequency captured yet
        if len_frequencies == 0:
            self.frequencies.append(current_freq)
            return

        # if frequency higher than before
        if current_freq > self.frequencies[-1]:
            self.registration.append('h')
            self.frequencies.append(current_freq)
            #if not self.direction_flag_up:
            #    self.frequencies = []
            #self.direction_flag_up = True
            self.handle_data_change()
            return

        # if frequency lower than before
        if current_freq < self.frequencies[-1]:
            self.registration.append('l')
            self.frequencies.append(current_freq)
            #if self.direction_flag_up:
            #    self.frequencies = []
            #self.direction_flag_up = False
            self.handle_data_change()
            return

        # if frequency same as before
        if current_freq == self.frequencies[-1]:
            self.registration.append('s')
            self.frequencies.append(current_freq)
            #if self.direction_flag_up:
            #    self.frequencies = []
            #self.direction_flag_up = False
            self.handle_data_change()
            return

    def handle_data_change(self):
        len_registration = len(self.registration)
        if self.silence >= 5:
            occurrence_lower = self.registration.count('l')
            occurrence_higher = self.registration.count('h')

            # detect decreasing frequency
            if occurrence_lower >= (0.6 * len_registration):
                print("---------------------------------UP------------------------------")
                self.up()  # todo: check difference up/down
                self.registration = []
            elif occurrence_higher >= (0.6 * len_registration):
                print("---------------------------------DOWN------------------------------")
                self.down()
                self.registration = []
            self.silence = 0

    def update(self, data):
        self.analyze_data(data)
        for i, item in enumerate(self.menu_items):
            if i == self.selected_item:
                item.color = self.selected_item_color
            else:
                item.color = self.initial_item_color

    def draw(self):
        for item in self.menu_items:
            item.draw()
