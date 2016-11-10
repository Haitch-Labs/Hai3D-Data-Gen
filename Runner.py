from pyautogui import *

# Automates opening blender and running the BlenderAPIDataGen.py
# makes it faster to test each change. Editing in the window is annoying

# Open Blender and Run this script
def open_application(application_name):
    click(1375, 10, button="left")  # Click Spotlight search in the tool bar
    typewrite(application_name)     # Search for application name
    press("enter")                  # Hit "enter" to open application

open_application("Blender")
time.sleep(2)
click(150, 725, button="left")  # close the prompt screen
click(260, 60, button="left")
typewrite("sc")
press("enter")
click(325, 530, button="left")
click(330, 110, button="left")

fullpath = "/Users/jack/Desktop/Projects/Hai3D-Data-Gen/BlenderAPIDataGen.py"
typewrite(fullpath)
press("enter")
click(1380, 110, button="left")
click(300,300, button="left")
hotkey("alt", "p")
