import pyglet
from pyglet.window import key

from testworld import TestScreen



SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600



window = pyglet.window.Window(SCREEN_WIDTH, SCREEN_HEIGHT)
screen = TestScreen()

@window.event
def on_draw():
    window.clear()
    screen.draw()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.Q:
        pyglet.app.exit()
    screen.on_key_press(symbol, modifiers)

@window.event
def on_key_release(symbol, modifiers):
    pass

def update(dt):
    screen.update()



if __name__ == '__main__':
    #event_logger = pyglet.window.event.WindowEventLogger()
    #window.push_handlers(event_logger)

    pyglet.clock.schedule_interval(update, 1/60.0) # 60 FPS
    pyglet.app.run()
