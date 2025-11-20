import eel
from engine.features import *
from engine.command import *

def start():
    eel.init('www')
    playAssistantSound()  # Play the sound
    eel.start('index.html',mode='brave-app',port=5500)
