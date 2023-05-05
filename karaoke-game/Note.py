from pyglet import shapes


class Note:
    def __init__(self, note_length, note_position, note_height, gui_factor):
        self.height = 25
        self.width = note_length
        self.initial_color = (255, 255, 255)
        self.hit_color = (19, 200, 10)
        self.frequency = note_height
        self.body = shapes.Rectangle(x=note_position, y=note_height * gui_factor, width=self.width, height=self.height, color=self.initial_color)
        self.is_hit = False

    def set_is_hit(self, is_hit):
        self.is_hit = is_hit

    def update(self):
        '''
        color note green if it is hit
        '''
        if self.is_hit:
            self.body.color = self.hit_color
        else:
            self.body.color = self.initial_color

    def draw(self):
        self.body.draw()
