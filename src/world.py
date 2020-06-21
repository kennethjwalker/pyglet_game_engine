import math
import pyglet

from resources import Resources



class WorldResources(Resources):
    def __init__(self):
        super().__init__()



class GroundTiles(pyglet.sprite.Sprite):
    def __init__(self, index_x, index_y, tile_size=32, screen_x=0, screen_y=0, *args, **kwargs):
        self.index_x = index_x
        self.index_y = index_y
        self.tile_size = tile_size # in pixels squared

        super(GroundTiles, self).__init__(x=(self.index_x * self.tile_size) - (-screen_x * self.tile_size), y=(self.index_y * self.tile_size) - (-screen_y * self.tile_size), *args, **kwargs)


    def update(self, screen_x, screen_y):
        self.x = (self.index_x * self.tile_size) - (-screen_x * self.tile_size)
        self.y = (self.index_y * self.tile_size) - (-screen_y * self.tile_size)



class EnvironmentTiles(pyglet.sprite.Sprite):
    def __init__(self, index_x, index_y, env_type=None, tile_size=32, screen_x=0, screen_y=0, *args, **kwargs):
        self.env_type = env_type
        self.index_x = index_x
        self.index_y = index_y
        self.tile_size = tile_size # in pixels squared

        super(EnvironmentTiles, self).__init__(x=(self.index_x * self.tile_size) - (-screen_x * self.tile_size), y=(self.index_y * self.tile_size) - (-screen_y * self.tile_size), *args, **kwargs)


    def update(self, screen_x, screen_y):
        self.x = (self.index_x * self.tile_size) - (-screen_x * self.tile_size)
        self.y = (self.index_y * self.tile_size) - (-screen_y * self.tile_size)



class World:
    def __init__(self, resources, screen_width=800, screen_height=600, tiles_x=10, tiles_y=10, tile_size=32, starting_tile_x=0, starting_tile_y=0, offset_x=0, offset_y=0):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.num_tiles_x = tiles_x
        self.num_tiles_y = tiles_y
        self.tile_size = tile_size # in pixels squared
        self.screen_view_x = starting_tile_x # top left tile x index
        self.screen_view_y = starting_tile_y # top left tile y index
        self.screen_tiles_x = self.screen_width // self.tile_size
        self.screen_tiles_y = self.screen_height // self.tile_size
        self.screen_offset_x = math.floor((self.screen_tiles_x / self.num_tiles_x)*(self.num_tiles_x // 2))
        self.screen_offset_y = math.floor((self.screen_tiles_y / self.num_tiles_y)*(self.num_tiles_y // 2))

        #print(math.floor((self.screen_tiles_x / self.num_tiles_x)*(self.num_tiles_x // 2)))

        self.resources = resources
        self.ground_batch = pyglet.graphics.Batch()
        self.env_batch = pyglet.graphics.Batch()
        self.obj_batch = pyglet.graphics.Batch()
        self.npc_batch = pyglet.graphics.Batch()
        self.pc_batch = pyglet.graphics.Batch()

        self.ground_tiles = [] # [x][y]
        self.env_tiles = [] # [x][y]
        self.obj_tiles = [] # [x][y]


    def build_world(self):
        pass

    def draw(self):
        self.ground_batch.draw()
        self.env_batch.draw()
        self.obj_batch.draw()
        self.npc_batch.draw()
        self.pc_batch.draw()

    def update(self):
        # update all the ground tiles
        for tile in self.ground_tiles:
            tile.update(self.screen_view_x, self.screen_view_y)

        # update all the environment tiles
        for tile in self.env_tiles:
            tile.update(self.screen_view_x, self.screen_view_y)

        # update all the environment tiles
        for tile in self.obj_tiles:
            tile.update(self.screen_view_x, self.screen_view_y)
