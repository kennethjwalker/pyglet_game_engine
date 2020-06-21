import pyglet

from resources import Resources



class Character(pyglet.sprite.Sprite):
    def __init__(self, index_x, index_y, tile_size=32, screen_x=0, screen_y=0, *args, **kwargs):
        self.index_x = index_x
        self.index_y = index_y
        self.tile_size = tile_size # in pixels squared

        super(Character, self).__init__(x=(self.index_x * self.tile_size) - (-screen_x * self.tile_size), y=(self.index_y * self.tile_size) - (-screen_y * self.tile_size), *args, **kwargs)



    def get_x(self):
        return self.index_x

    def get_y(self):
        return self.index_y

    def move(self, x, y):
        self.index_x += x
        self.index_y += y



    def update(self, screen_x, screen_y):
        self.x = (self.index_x * self.tile_size) - (-screen_x * self.tile_size)
        self.y = (self.index_y * self.tile_size) - (-screen_y * self.tile_size)
