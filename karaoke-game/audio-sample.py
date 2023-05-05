import pyaudio
import numpy as np
from matplotlib import pyplot as plt
import pyglet
import sys

# Set up audio stream
# reduce chunk size and sampling rate for lower latency
CHUNK_SIZE = 1024  # Number of audio frames per buffer
FORMAT = pyaudio.paInt16  # Audio format
CHANNELS = 1  # Mono audio
RATE = 44100  # Audio sampling rate (Hz)
p = pyaudio.PyAudio()

##############
C2 = 65.41
E2 = 82.41
G2 = 98.00
##############

# print info about audio devices
# let user select audio device
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')

for i in range(0, numdevices):
    if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
        print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))

print('select audio device:')
input_device = int(input())

# open audio input stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK_SIZE,
                input_device_index=input_device)


WINDOW_WIDTH = 600
WINDOW_HEIGHT = 780

window = pyglet.window.Window(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
pyglet.gl.glClearColor(0.1, 0.6, 0.2, 0)
rect = pyglet.shapes.Rectangle(x=50, y=50, width=50, height=50, color=(10,10,10))
rectC4 = pyglet.shapes.Rectangle(x=150, y=C2*2, width=50, height=50, color=(100,10,10))
rectE4 = pyglet.shapes.Rectangle(x=300, y=E2*2, width=50, height=50, color=(100,10,10))
rectG4 = pyglet.shapes.Rectangle(x=450, y=G2*2, width=50, height=50, color=(100,10,10))

@window.event
def on_draw():
    window.clear()
    data = stream.read(CHUNK_SIZE)
    # Convert audio data to numpy array
    data = np.frombuffer(data, dtype=np.int16)

    rect.draw()
    rectC4.draw()
    rectE4.draw()
    rectG4.draw()
    spectrum = np.abs(np.fft.fft(data))
    freq = np.argmax(spectrum) * 10

    print(freq)

    rect.y = freq * 2
    rect.x += 1
    if (C2 + 5) >= freq >= (C2 - 5) and rectC4.x <= rect.x <= (rectC4.x + rectC4.width):
        rectC4.color = (10, 200, 10)
    if (E2 + 5) >= freq >= (E2 - 5) and rectE4.x <= rect.x <= (rectE4.x + rectE4.width):
        rectE4.color = (10, 200, 10)
    if (G2 + 5) >= freq >= (G2 - 5) and rectG4.x <= rect.x <= (rectG4.x + rectG4.width):
        rectG4.color = (10, 200, 10)


@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.Q:
        sys.exit(0)


pyglet.app.run()
