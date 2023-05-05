from Menu import Menu
import pyglet
import sys


WINDOW_WIDTH = 300
WINDOW_HEIGHT = 500

window = pyglet.window.Window(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
menu = Menu(WINDOW_WIDTH, WINDOW_HEIGHT)


@window.event
def on_draw():
    window.clear()
    menu.update()
    menu.draw()


@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.UP:
        menu.up()
    elif symbol == pyglet.window.key.DOWN:
        menu.down()
    elif symbol == pyglet.window.key.Q:
        sys.exit(0)


pyglet.app.run()
