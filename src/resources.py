import pyglet



class Resources:
    def __init__(self):
        pyglet.resource.path = [r'resources/tiled_files/tiles']
        pyglet.resource.reindex()



    def anchor_center(self, image):
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2

    def anchor_topright(self, image):
        image.anchor_x = 0
        image.anchor_y = 0



class MenuResources(Resources):
    def __init__(self):
        super().__init__()

        self.menu_pointer = pyglet.resource.image("menu/pointer.png")
        self.anchor_center(self.menu_pointer)
        self.menu_pointer_flip = pyglet.resource.image('menu/pointer.png', flip_x=True)
