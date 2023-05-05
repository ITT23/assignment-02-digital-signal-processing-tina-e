from pyglet import text


class Menu:
    def __init__(self, win_w, win_h, background):
        self.win_score = 300
        self.background = background
        self.welcome = text.Label('WELCOME!', font_size=40, x=win_w / 2, y=win_h / 1.8, anchor_x='center', anchor_y='center')
        self.winner = text.Label('YOU ROCK!', font_size=40, x=win_w / 2, y=win_h / 1.8, anchor_x='center', anchor_y='center')
        self.loser = text.Label('YOU SUCK!', font_size=40, x=win_w / 2, y=win_h / 1.8, anchor_x='center', anchor_y='center')
        self.instructions_start = text.Label('Start: SPACE', x=win_w / 2, y=win_h / 4, anchor_x='center', anchor_y='center')
        self.instructions_exit = text.Label('Exit: Q', x=win_w / 2, y=win_h / 5, anchor_x='center', anchor_y='center')

    def draw(self, welcome, score):
        self.background.draw()
        if welcome:
            self.welcome.draw()
        else:
            if score >= self.win_score:
                self.winner.draw()
            else:
                self.loser.draw()
        self.instructions_start.draw()
        self.instructions_exit.draw()
