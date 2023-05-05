import numpy as np
from Cursor import Cursor
from SongPattern import SongPattern
from Menu import Menu
from pyglet import text, resource, sprite


def calculate_frequency(data):
    spectrum = np.abs(np.fft.fft(data))
    freq = np.argmax(spectrum)
    return freq

# background image:
# Image by rawpixel.com on Freepik
# (https://www.freepik.com/free-photo/abstract-wallpaper-background-design-dark-design_18100738.htm#query=black%20smoke&position=46&from_view=keyword&track=ais)


class Game:
    def __init__(self, window_width, window_height):
        self.game_state = -1
        self.intro_width = window_width / 8
        self.width = window_width - self.intro_width
        self.background = sprite.Sprite(img=resource.image('assets/background.jpg'))
        self.pattern = SongPattern(self.intro_width, self.width, window_height / 100)
        self.cursor = Cursor(window_height / 100)
        self.menu = Menu(window_width, window_height, self.background)
        self.score = text.Label("Score: 0", x=window_width - 50, y=window_height - 20, anchor_x='center', anchor_y='center')

    def update(self, data):
        if self.cursor.body.x + self.cursor.body.width > self.width + self.intro_width:
            self.game_state = 0
            self.cursor.reset()
        elif self.game_state == 1:
            freq = calculate_frequency(data)
            self.cursor.update(freq)
            self.pattern.check_hit(self.cursor.body.x, freq)
            self.pattern.update()
        self.score.text = f"Score: {self.pattern.score}"

    def draw(self):
        if self.game_state == 1:
            self.background.draw()
            self.pattern.draw()
            self.cursor.draw()
        # welcome state
        elif self.game_state == 0:
            self.menu.draw(welcome=False, score=self.pattern.score)
        # end state
        elif self.game_state == -1:
            self.menu.draw(welcome=True, score=self.pattern.score)
        self.score.draw()