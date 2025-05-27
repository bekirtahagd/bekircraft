from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

def generateEditor():
    camera_editor = EditorCamera()
    camera_editor.rotation_speed = 100    # Optional: Geschwindigkeit der Mausrotation
    camera_editor.move_speed = 10         # Optional: Geschwindigkeit der Bewegung
    return camera_editor

def generatePlayer():
    player = FirstPersonController(position=(10,100,10))
    player.cursor.visible = True
    player.cursor.scale *= 10
    player.cursor.color = color.white
    player.cursor.texture = "Assets/Textures/Crosshair.png"
    return player
