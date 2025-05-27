from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina() # We need to setup Ursina prior to importing the other files because otherwise the needed functions wont be created -> error

# Import other scripts
from playerSetup import *
from worldGeneration import *

# Play background music
background_music = Audio("Assets/SFX/Minecraft-Background-Music.mp3", loop=True, autoplay=True)

# Generate the basic Sky, the world and the player character
sky = generateSky()
generateWorld(50, 50, 0)
player = generatePlayer()


def update():
    # If Esc Key gets pressed, leave the programm
    if held_keys["escape"]:
        application.quit()

if __name__ == "__main__":
    app.run(info=False)
