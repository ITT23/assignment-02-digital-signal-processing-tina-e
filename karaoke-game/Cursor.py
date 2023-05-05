from pyglet import shapes


class Cursor:
    def __init__(self, gui_factor):
        self.width = 20
        self.gui_factor = gui_factor
        self.body = shapes.Rectangle(x=0, y=0, width=self.width, height=self.width, color=(156, 0, 75))

    def reset(self):
        self.body.x = 0

    def update(self, freq):
        self.body.y = freq * self.gui_factor
        self.body.x += 1

    def draw(self):
        self.body.draw()
