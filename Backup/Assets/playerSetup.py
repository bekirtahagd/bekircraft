from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

def generatePlayer():
    player = FirstPersonController(position=(10,100,10))
    player.cursor.visible = True
    player.cursor.scale *= 10
    player.cursor.color = color.white
    player.cursor.texture = "Assets/Textures/Crosshair.png"
    return player