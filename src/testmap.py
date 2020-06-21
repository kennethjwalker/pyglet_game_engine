import pandas as pd



TILESET = {
    'stone_brick_1': 0,
    'closed_door': 1,
    'player': 2,
    'rect_gray_0_old': 3,
    'shaft': 4,
}

GROUNDMAP = []
ENVMAP = []
OBJMAP = []

def create_testmap():
    ground_file = r'resources/tiled_files/maps/csv/first_steps_ground_1.csv'
    env_file = r'resources/tiled_files/maps/csv/first_steps_env_1.csv'
    obj_file = r'resources/tiled_files/maps/csv/first_steps_obj_1.csv'
    ground_df = pd.read_csv(ground_file, header=None)
    env_df = pd.read_csv(env_file, header=None)
    obj_df = pd.read_csv(obj_file, header=None)

    # y data needs to be ready in backwards do to pyglet drawing from btm-left
    if(ground_df.size > 0):
        for x in range(len(ground_df)):
            col = []
            for y in range(len(ground_df[x])):
                col.append(ground_df[x][len(ground_df[x])-y-1])
            GROUNDMAP.append(col)

    if(env_df.size > 0):
        for x in range(len(env_df)):
            col = []
            for y in range(len(env_df[x])):
                col.append(env_df[x][len(env_df[x])-y-1])
            ENVMAP.append(col)

    if(obj_df.size > 0):
        for x in range(len(obj_df)):
            col = []
            for y in range(len(obj_df[x])):
                col.append(obj_df[x][len(obj_df[x])-y-1])
            OBJMAP.append(col)
