import pyglet
from pyglet.window import key

from world import World



class Screen:
    def __init__(self, width=800, height=600, world=None):
        self.width = width
        self.height = height
        print(world)
        self.world = world



    def update(self):
        self.world.update()

    def draw(self):
        self.world.draw()
