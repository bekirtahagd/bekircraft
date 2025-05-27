from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina() # We need to setup Ursina prior to importing the other files because otherwise the needed functions wont be created -> error

# Import other scripts
from playerSetup import *
from worldGeneration import *

# Play background music
background_music = Audio("Assets/SFX/Minecraft-Background-Music.mp3", loop=True, autoplay=True)

# Rerender World when moving?
reRender = True

# Generate the basic Sky, the world and the player character
sky = generate_sky()
generate_world(100, 100, 0)
player = generatePlayer()

# Keep track of players last position to be able to figure out when he moves
previous_pos = player.position
position_ask_timer = 0
position_ask_delay = 1 # seconds

def update():
    global previous_pos, position_ask_timer

    # If Esc Key gets pressed, leave the programm
    if held_keys["escape"]:
        application.quit()
    
    position_ask_timer += time.dt


    # Check whether player has moved
    if player.position != previous_pos and position_ask_timer >= position_ask_delay and reRender:
        reRenderWorld(player_pos=player.position, distance=10)

        previous_pos = player.position
        position_ask_timer = 0

if __name__ == "__main__":
    app.run(info=False)
