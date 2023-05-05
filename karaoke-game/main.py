import numpy as np
import pyglet
import sys
import pyaudio
from setup import setup
from Game import Game

# reduce chunk size and sampling rate for lower latency
CHUNK_SIZE = 1024  # Number of audio frames per buffer
FORMAT = pyaudio.paInt16  # Audio format
CHANNELS = 1  # Mono audio
RATE = 44100  # Audio sampling rate (Hz)

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400

stream = setup(CHUNK_SIZE, FORMAT, CHANNELS, RATE)
window = pyglet.window.Window(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
game = Game(WINDOW_WIDTH, WINDOW_HEIGHT)


@window.event
def on_draw():
    window.clear()
    # Convert audio data to numpy array
    data = np.frombuffer(stream.read(CHUNK_SIZE), dtype=np.int16)
    game.update(data)
    game.draw()


@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.SPACE:
        game.game_state = 1
        game.pattern.score = 0
    elif symbol == pyglet.window.key.Q:
        sys.exit(0)


pyglet.app.run()
