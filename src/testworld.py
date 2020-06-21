import pyglet
from pyglet.window import key

from characters import Character
#from objects import IngameObjects
from screen import *
from world import *

from testmap import *



ACTIONS = {
    'move': 10,
}

ENV_TYPE = {
    'impassable': 10,
    'door': 20,
    'trap': 30,
}



class TestScreen(Screen):
    def __init__(self):
        super().__init__(world=TestWorld())

    def on_key_press(self, symbol, modifiers):
        self.world.on_key_press(symbol, modifiers)

    def on_key_release(self, symbol, modifiers):
        self.world.on_key_release(symbol, modifiers)



class TestWorldResources(WorldResources):
    def __init__(self):
        super().__init__()

        self.tileset_error = pyglet.resource.image(r'error/error.png')
        self.stone_brick_1 = pyglet.resource.image(r'walls/stone_brick_1.png')
        self.closed_door = pyglet.resource.image(r'doors/closed_door.png')
        self.player = pyglet.resource.image(r'characters/player.png')
        self.rect_gray_0_old = pyglet.resource.image(r'floors/rect_gray_0_old.png')
        self.shaft = pyglet.resource.image(r'traps/shaft.png')



class TestWorld(World):
    def __init__(self, screen_width=800, screen_height=600, tiles_x=20, tiles_y=20, starting_tile_x=8, starting_tile_y=4):
        super().__init__(TestWorldResources(), screen_width, screen_height, tiles_x=tiles_x, tiles_y=tiles_y, starting_tile_x=starting_tile_x, starting_tile_y=starting_tile_y)

        create_testmap()
        self.ground_map = GROUNDMAP
        self.env_map = ENVMAP
        self.obj_map = OBJMAP

        self.ai_character = None
        self.player_character = None
        self.enemies = []
        self.food = []

        self.build_world()



    def build_world(self):
        # clear to be safe
        self.ground_tiles = []
        self.env_tiles = []
        self.obj_tiles = []

        for x in range(10):
            for y in range(10):
                # process ground
                if self.ground_map[x][y] == TILESET['rect_gray_0_old']:
                    tile = GroundTiles(x, y, img=self.resources.rect_gray_0_old, batch=self.ground_batch)
                    self.ground_tiles.append(tile)
                else:
                    if(self.ground_map[x][y] != -1):
                        tile = GroundTiles(x, y, img=self.resources.tileset_error, batch=self.ground_batch)
                        self.ground_tiles.append(tile)

                # process environment
                if self.env_map[x][y] == TILESET['stone_brick_1']:
                    tile = EnvironmentTiles(x, y, env_type=ENV_TYPE['impassable'], img=self.resources.stone_brick_1, batch=self.env_batch)
                    self.env_tiles.append(tile)
                elif self.env_map[x][y] == TILESET['closed_door']:
                    tile = EnvironmentTiles(x, y, env_type=ENV_TYPE['door'], img=self.resources.closed_door, batch=self.env_batch)
                    self.env_tiles.append(tile)
                elif self.env_map[x][y] == TILESET['shaft']:
                    tile = EnvironmentTiles(x, y, env_type=ENV_TYPE['trap'], img=self.resources.shaft, batch=self.env_batch)
                    self.env_tiles.append(tile)
                else:
                    if(self.env_map[x][y] != -1):
                        tile = EnvironmentTiles(x, y, img=self.resources.tileset_error, batch=self.env_batch)
                        self.env_tiles.append(tile)

                # process objects
                if self.obj_map[x][y] == TILESET['player']:
                    # TODO: Make this into a charater sprite
                    self.player_character = Character(x, y, img=self.resources.player, batch=self.obj_batch)
                    self.obj_tiles.append(self.player_character)
                else:
                    if(self.obj_map[x][y] != -1):
                        tile = EnvironmentTiles(x, y, img=self.resources.tileset_error, batch=self.obj_batch)
                        self.obj_tiles.append(tile)

    def update(self):
        super().update()



    def on_key_press(self, symbol, modifiers):
        if self.player_character:
            if symbol == key.DOWN:
                self.index_check(self.player_character, ACTIONS['move'], x_move=0, y_move=-1)
                #self.player_character.move(0, -1)
            elif symbol == key.UP:
                self.index_check(self.player_character, ACTIONS['move'], x_move=0, y_move=1)
                #self.player_character.move(0, 1)
            elif symbol == key.LEFT:
                self.index_check(self.player_character, ACTIONS['move'], x_move=-1, y_move=0)
                #self.player_character.move(-1, 0)
            elif symbol == key.RIGHT:
                self.index_check(self.player_character, ACTIONS['move'], x_move=1, y_move=0)
                #self.player_character.move(1, 0)

    def on_key_release(self, symbol, modifiers):
        pass


    def index_check(self, character, action, x=0, y=0, x_move=0, y_move=0):
        # TODO: better system
        if(action == ACTIONS['move']):
            x = character.index_x
            y = character.index_y

            for env_obj in self.env_tiles:
                if(env_obj.index_x == x+x_move and env_obj.index_y == y+y_move):
                    if(env_obj.env_type == ENV_TYPE['impassable']):
                        print('Impassable @ {}, {}'.format(x+x_move, y+y_move))
                        return None
                    elif(env_obj.env_type == ENV_TYPE['door']):
                        print('Door @ {}, {}'.format(x+x_move, y+y_move))
                        print('You WIN!')
                        pyglet.app.exit()
                        return None
                    elif(env_obj.env_type == ENV_TYPE['trap']):
                        print('Trap @ {}, {}'.format(x+x_move, y+y_move))
                        print('You LOSE!')
                        pyglet.app.exit()
        character.move(x_move, y_move)
