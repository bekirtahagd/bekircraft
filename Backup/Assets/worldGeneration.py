from ursina import *
from ursina.prefabs import *
from Block import *
from perlin_numpy import generate_perlin_noise_2d


# Generate Sky
class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = "sphere",
            texture=load_texture("Assets/Textures/Sky.png"),
            scale=150,
            double_sided = True
        )

def generateSky():
    return Sky()


def generateWorld(width, depth, seed):    
    # Generate Perlin Noise for World Generation
    shape = (width, depth)
    res = (2,2)
    noise = generate_perlin_noise_2d(shape,res)

    for z in range(width):
        for x in range(depth):
            y = round(10 * noise[z, x])
            Block(position=(x, y, z), texture=textures["Grass"], mesh=generate_cube_mesh())
