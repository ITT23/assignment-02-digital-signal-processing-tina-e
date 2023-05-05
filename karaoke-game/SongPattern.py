from Note import Note

# https://pages.mtu.edu/~suits/notefreqs.html
FREQUENCY_D = 36.71
FREQUENCY_C = 32.70
FREQUENCY_A = 27.5
FREQUENCY_H = 30.87
FREQUENCY_G = 24.50

# you don't have to exactly hit the note:)
ACCEPTED_DIFF = 2


class SongPattern:
    def __init__(self, x, width, gui_factor):
        # 4/4 rhythm
        self.bar_width = (width - x) / 4
        self.beat_width = self.bar_width / 4
        self.pattern = []
        self.pattern.append(Note(note_length=3 * self.beat_width, note_position=x + 1 * self.beat_width, note_height=FREQUENCY_D, gui_factor=gui_factor))
        self.pattern.append(Note(note_length=1 * self.beat_width, note_position=x + 4 * self.beat_width, note_height=FREQUENCY_A, gui_factor=gui_factor))
        self.pattern.append(Note(note_length=3 * self.beat_width, note_position=x + 5 * self.beat_width, note_height=FREQUENCY_C, gui_factor=gui_factor))
        self.pattern.append(Note(note_length=1 * self.beat_width, note_position=x + 8 * self.beat_width, note_height=FREQUENCY_A, gui_factor=gui_factor))
        self.pattern.append(Note(note_length=3 * self.beat_width, note_position=x + 9 * self.beat_width, note_height=FREQUENCY_H, gui_factor=gui_factor))
        self.pattern.append(Note(note_length=1 * self.beat_width, note_position=x + 12 * self.beat_width, note_height=FREQUENCY_G, gui_factor=gui_factor))
        self.pattern.append(Note(note_length=4 * self.beat_width, note_position=x + 13 * self.beat_width, note_height=FREQUENCY_A, gui_factor=gui_factor))
        self.score = 0

    def check_hit(self, cursor_x, freq):
        '''
        check if correct note is hit at the right time
        :param cursor_x: to make sure you hit the note at the right time
        :param freq: detected frequency of audio input
        '''
        for note in self.pattern:
            if (note.frequency + ACCEPTED_DIFF) >= freq >= (note.frequency - ACCEPTED_DIFF) and note.body.x <= cursor_x <= (note.body.x + note.width):
                note.set_is_hit(True)
                self.score += 1
            else:
                note.set_is_hit(False)

    def update(self):
        for note in self.pattern:
            note.update()

    def draw(self):
        for note in self.pattern:
            note.draw()