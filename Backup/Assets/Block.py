from ursina import *

# The sound that gets played whenever you build or destroy a cube
build_sound = Audio("Assets/SFX/Build_Sound.wav", loop=False, autoplay=False)

# The textures of the different blocks
textures = {
    "Grass": load_texture("Assets/Textures/Grass.png"),
    "Dirt": load_texture("Assets/Textures/Dirt.png"),
    "Brick": load_texture("Assets/Textures/Brick.png"),
    "Wood": load_texture("Assets/Textures/Wood.png"),
    "Stone": load_texture("Assets/Textures/Stone.png"),
}


class Block(Button):
    def __init__(self, mesh, position=(0, 0, 0), texture=textures["Grass"], breakable=True):
        super().__init__(
            parent=scene,
            position=position,
            model=mesh,
            texture = texture,
            origin_y = 0.5,
            color=color.hsv(0, 0, random.uniform(0.9, 1)),
            highlight_color = color.light_gray,
        )
        self.breakable = breakable

    # Input Function calls everytime a key was pressed
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                build_sound.play()
                Block(position=self.position + mouse.normal, texture=textures["Grass"])
            elif key == "right mouse down" and self.breakable:
                build_sound.play()
                destroy(self)


def getBlockType():
    return 0

def generate_cube_mesh(visible_faces=('top', 'bottom', 'left', 'right', 'front', 'back')):
    verts = []
    tris = []
    uvs = []

    # Hardcoded UVS of our textures
    custom_uvs = [
        (0.375, 0.0), (0.625, 0.0), (0.625, 0.25), (0.375, 0.25), # Front, Back, Left, Right
        (0.125, 0.5), (0.375, 0.5), (0.375, 0.75), (0.125, 0.75), # Bottom
        (0.625, 0.5), (0.875, 0.5), (0.875, 0.75), (0.625, 0.75)  # Top
    ]

    # Define coordinats of each face
    def add_face(vs, uv_coords):
        i = len(verts)
        verts.extend(vs)
        uvs.extend(uv_coords)
        tris.extend([i, i+1, i+2, i, i+2, i+3])

    # Texture-Dictionary: Which Uvs are for which Sides
    face_uv_map = {
        'top': custom_uvs[8:12],    # Top
        'bottom': custom_uvs[4:8], # Bottom
        'facet': custom_uvs[0:4],  # Front, Back, Left, Right
    }

    # Create each sides
    if 'top' in visible_faces:
        add_face(
            [Vec3(0,1,0), Vec3(1,1,0), Vec3(1,1,1), Vec3(0,1,1)],
            face_uv_map['top']
        )
    if 'bottom' in visible_faces:
        add_face(
            [Vec3(0,0,0), Vec3(0,0,1), Vec3(1,0,1), Vec3(1,0,0)],
            face_uv_map['bottom']
        )
    if 'left' in visible_faces:
        add_face(
            [Vec3(0,0,0), Vec3(0,1,0), Vec3(0,1,1), Vec3(0,0,1)],
            face_uv_map['facet']
        )
    if 'right' in visible_faces:
        add_face(
            [Vec3(1,0,1), Vec3(1,1,1), Vec3(1,1,0), Vec3(1,0,0)],
            face_uv_map['facet']
        )
    if 'front' in visible_faces:
        add_face(
            [Vec3(0,0,1), Vec3(0,1,1), Vec3(1,1,1), Vec3(1,0,1)],
            face_uv_map['facet']
        )
    if 'back' in visible_faces:
        add_face(
            [Vec3(1,0,0), Vec3(1,1,0), Vec3(0,1,0), Vec3(0,0,0)],
            face_uv_map['facet']
        )

    # Generate Mesh
    mesh = Mesh(vertices=verts, triangles=tris, uvs=uvs)
    mesh.generate()

    return mesh
