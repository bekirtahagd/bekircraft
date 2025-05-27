from ursina import *
from ursina.prefabs import *
from Block import *
from perlin_noise import PerlinNoise

# Generate Sky
class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = "sphere",
            texture=load_texture("Assets/Textures/Sky.png"),
            scale=500,
            double_sided = True
        )

def generate_sky():
    return Sky()



# Save all the changed Blocks in an Dictionary. Key: Position, Block: BlockType
changed_blocks = {}

lowest_point = 0
highest_point = 100
surfaceLevel = 50

noise = PerlinNoise(octaves=6, seed=0)
noise_scaling = 0.005
amplitude = 30
def generate_world(width, depth, seed):    
    global noise, noise_scaling, amplitude

    # Set Perlin Noise Seed
    noise.seed = seed
    amount = width * depth * (highest_point - lowest_point)

    i = 0
    print("Generating")
    for z in range(int(-width/2), int(width/2)):
        for x in range(int(-depth/2), int(depth/2)):
            # Spawn Terrain
            rendered_positions.add((x,z)) 
            for y in range(lowest_point, highest_point):
                # Progress
                i += 1
                progress = i/amount
                print(progress)

                # Blocks
                block = getBlock(position=(x, y, z))
                if block != None:
                    block.enable()
            
            # Try to spawn tree
            try_place_tree(x, z)
    

treeProbability = 0.005
def generate_tree(origin):
    x, y, z = origin

    # Zufällige Höhe des Stamms
    trunk_height = random.randint(4, 5)

    # Stamm bauen
    for i in range(trunk_height):
        height = y + i
        if getBlock((x, height, z), checkFaces=False) == None:
            changed_blocks[(x, height, z)] = "Trunk"
            Block(position=(x, height, z),
                  texture=textures['Wood'],
                  mesh=generate_cube_mesh(visible_faces={"front", "back", "left", "right"}),
                  enabled=True)

    # Blätter bauen (eine einfache kugelartige Krone)
    crown_base = y + trunk_height
    for h in range(4):  # Höhe der Blätter
        radius = 2 - h  # Oben wird es schmaler
        for dx in range(-radius, radius + 1):
            for dz in range(-radius, radius + 1):
                for dy in range(0, 2):  # Zwei Lagen pro Ebene
                    px = x + dx
                    py = crown_base + h + dy
                    pz = z + dz
                    if getBlock((px, py, pz), checkFaces=False) == None:      
                        changed_blocks[(x, height, z)] = "Leave"
                        Block(position=(px, py, pz),
                              texture=textures['Leaves'],
                              mesh=generate_cube_mesh(),
                              enabled=True)

def try_place_tree(x, z):
    # Try probability
    rand = random.random()
    if rand < treeProbability:
        y = getMaxHeightAtPos(x,z)
        generate_tree((x, y, z))


def getMaxHeightAtPos(x, z):
    # Scaled Position for noise
    nx = x * noise_scaling
    nz = z * noise_scaling
    
    # Check whether to return a block or air
    noise_value = noise([nx, nz])
    max_height = surfaceLevel + int(amplitude * noise_value)
    return max_height


def getBlock(position, checkFaces=True):
    global noise, noise_scaling

    # Position and scaled coordinates
    x,y,z = position

    # Check whether the block was changed from standards
    if changed_blocks.get((x, y, z)) != None:
        return changed_blocks.get((x, y, z))

    if y > getMaxHeightAtPos(x, z):
        return None
    
    # To not reach infinite recursion, we're not always checking the faces
    if checkFaces == False:
        return True

    # Check which faces of the block need to be rendered
    visible_faces = []

    # Top
    if getBlock((x, y+1, z), checkFaces=False) == None:
        visible_faces.append("top")
    # Bottom
    if getBlock((x, y-1, z), checkFaces=False) == None:
        visible_faces.append("bottom")
    # Front
    if getBlock((x, y, z+1), checkFaces=False) == None:
        visible_faces.append("front")
    # Back
    if getBlock((x, y, z-1), checkFaces=False) == None:
        visible_faces.append("back")
    # Left
    if getBlock((x-1, y, z), checkFaces=False) == None:
        visible_faces.append("left")
    # Right
    if getBlock((x+1, y, z), checkFaces=False) == None:
        visible_faces.append("right")

    # If none of the faces are visible, return nothing
    if len(visible_faces) == 0:
        return None

    # Select Texture
    texture = 0
    if ('top' in visible_faces):
        texture = textures["Grass"]
    else:
        texture = textures["Dirt"]

    return Block(position=(x, y, z), texture=texture, mesh=generate_cube_mesh(visible_faces=visible_faces), enabled=False)

# Rendered Positions save the x,z coordinates of all the blocks that are rendered. Therefore we know whether coordinates are rendered or not
rendered_positions = set()
def reRenderWorld(player_pos, distance):
    # Get distance back, and distance left
    start_pos = [round(player_pos.x - distance), round(player_pos.z - distance)]
    end_pos = [start_pos[0] + 2*distance, start_pos[1] + 2*distance]

    new_positions  = [(x, z) for x in range(start_pos[0], end_pos[0]) for z in range(start_pos[1], end_pos[1]) if (x,z) not in rendered_positions]

    def render_next(i=0):
        if i >= len(new_positions):
            return
        
        x, z = new_positions[i]
        y = getMaxHeightAtPos(x, z)
        block=getBlock(position=(x, y, z))
        block2=getBlock(position=(x, y-1, z))
        if block:
            block.enable()
        if block2:
            block2.enable()
        rendered_positions.add((x, z))

        # Generate Tree
        invoke(try_place_tree, x, z, delay=0.01)

        invoke(render_next, i+1, delay=0.005)
    
    render_next()

        
    