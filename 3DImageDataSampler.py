from pyautogui import *
import pyautogui
import time
import os
import pyperclip

# Things to do:
#    - Fix the bug for the rendering of the man
#    - Fix the bug for the colour
#    - Improve rotation algorithm, so he moves in blocks
#    - Allow it to do render more than one image in many file locations
#    - Make a branch with the Blender API approach



# Note: Only works on MAC OSX Macbook Air
# Blender was chosen because it could open
# much faster in comparison to CAD

width, height = size() # returns width and height of my screen (this is never used)

def open_application(application_name):
    click(1375, 10, button="left")  # Click Spotlight search in the tool bar
    typewrite(application_name)     # Search for application name
    press("enter")                  # Hit "enter" to open application

def begin_recording(startX, startY, finishX, finishY):
    open_application("QuickTime Player")
    hotkey("ctrl", "command", 'n')  # Keyboard shortcut for beginning screen recording
    time.sleep(1)                   # Wait 0.5s to confirm box has appeared (can go to 0.2)  
    click(195, 205, button="left")  # Press Record
    time.sleep(1)
    click()
    """
    Record Segment of Screen:
        moveTo(startX,startY)
        dragTo(finishX, finishY)
        time.sleep(3)
        startButtonX = finishX-startX
        startButtonY = finishY-startY
        press(startButtonX, startButtonY)
    """
def end_recording(recording_name=None):
    click(1120, 10, button="left")  # Press 'stop' button in toolbar to stop recording
    time.sleep(1)
    click(63,33, button="left")     # Click the window's red cross
    time.sleep(1)
    typewrite(recording_name)
    click(900, 160, button="left")  # open drop down arrow and save to Desktop
    time.sleep(1)
    click(400, 270, button="left")    # click desktop
    click(1000, 525, button="left")   # click save

def main():

        # OPEN BLENDER
    open_application("Blender")
    time.sleep(2)
    click(150, 725, button="left")  # close the prompt screen
    moveTo(700,400)                 # move to the middle of the screen
    
        # CREATE PLAIN AXIS
    hotkey("shift", "a")            # Open the Menu
    moveTo(690, 550, duration=0.2)  # Got to Create Empty
    moveTo(790, 550, duration=0.2)  # Go to Plain Axes
    click(button="left")            # Select 'Plain Axes'

        # SELECT THE CAMERA AND PARENT IT TO THE MAIN AXIS
    click(410, 290, button="right") # Select the Camera
    keyDown("shift")                # hold shift
    click(1300, 177)                # click the Plain Axes we just (in the top right menu)
    keyUp("shift")
    moveTo(700,400)                 # just move to within the window
    hotkey("ctrl","p")              # bring up the parent controls
    click()                         # click 'object' to select the object's parenting

        # CHANGE CAMERA SETTINGS TO HAVE PERPENDICULAR VIEW OF PLAIN AXES
    click(410, 290, button="right") # Select the Camera
    click(1240, 100, button="left") # Drag out the transform menu
    moveTo(1070, 100)
    click()

    click(1150, 175, button="left") # Set the Z location to 0
    typewrite("0")
    press("enter")

    click(1150, 215, button="left") # Set the X rotation to 90
    typewrite("90")
    press("enter")

        # ROTATE THE CAMERA AROUND THE PLAIN AXIS 360 DEGREES x10 in total of 100 frames
    num_rotations = 10
    click(1300, 160, button="left") # Select the created Empty in the menu

                                     # note: menu already dragged out from above ^^
    click(1150, 255, button="right") # Right Click the Z rotation to bring up the menu
    click(1150, 280, button="left")  # Go Down and click insert single keyframe. This inserts
                                     # the initial camera position for keyframe 1
    click(577, 780, button="left")  # Click 100th frame in the timeline
    click(500,815, button="left")   # Set the timeline to only go for 100 frames
    typewrite("100")
    press("enter")                  

    click(1150, 255, button="left")    # Left Click the Z rotation.
    typewrite(str(360*num_rotations))  # 360 will move the camera around 360 degrees (back to where it started)
    press("enter")

    click(1150, 255, button="right") # Right Click the Z rotation to bring up the menu
    click(1150, 255, button="left")  # Go Down and click insert single keyframe (note it has moved slightly higher)

            # DELETE THE DEFAULT CUBE
    click(600, 400, button="right")
    press("x")
    click()
    
        # GET THE NAMES OF ALL OUR IMAGES
    objPaths  = ["/Users/jack/Desktop/Projects/3DImageDataSampler/3D Dataset/People/Person1.obj"] #, "/Users/jack/Desktop/Datasets/3D Dataset/Pokemon/Charmander.obj"]

    for objPath in objPaths:
                    
                # IMPORT THE IMAGE
        click(60,60, button="left")      # click 'File'
        moveTo(60,420, duration=0.2)     # go down to 'Import'
        moveTo(350,420, duration=0.2)    # go accross to the right
        click(350, 540, button="left")   # Select (Wavefront .obj)
                                         # This ^ opens a new window
        click(350, 110, button="left")   # Select the directory
        typewrite(objPath)
        press("enter")
        click(1400, 110, button="left")
        click(1400, 110, button="left")

            # CENTER THE IMAGE TO FIT TO CAMERA
        time.sleep(1)
        click(1300, 150, button="left")      # select the imported image (from the top right menu) (could have been right clicked
                                             # in the window but, they all change.
        moveTo(700, 400)                     # just move to within the window
        hotkey("shift", "ctrl", "alt", "c")  # hotkey to put the 3D image into center of axes.
        click()
        
            # GET THE CURRENT DIMENTIONS
        # current X
        click(1200, 400, button="left")
        hotkey("command", "c")
        X = float(str(pyperclip.paste()))
        
        # current Y
        click(1200, 420, button="left")
        hotkey("command", "c")
        Y = float(str(pyperclip.paste()))
        
        # current Z
        click(1200, 440, button="left")
        hotkey("command", "c")
        Z = float(str(pyperclip.paste()))

        ratio = 3.5 / max(X,Y,Z)  # we want to find the largest of the dimentions
                                  # and change it's dimention to 3.5 so it fits the camera (found this number by trial and error)
                                  # we want all the other choords to go down by the same ratio

            # UPDATE DIMENTIONS
        # update X
        newX = pyperclip.copy(str(X*ratio))
        click(1200, 400, button="left")
        hotkey("command", "v")
        press("enter")
        
        # update Y
        newX = pyperclip.copy(str(Y*ratio))
        click(1200, 420, button="left")
        hotkey("command", "v")
        press("enter")

        # update Z
        newX = pyperclip.copy(str(Z*ratio))
        click(1200, 440, button="left")
        hotkey("command", "v")
        press("enter")

            # ROTATE THE 3D MODEL
        # set the first frame to 0degrees
        click(217, 780, button="left")  # click the frame number down the bottom to the left of the play button
        click()
        click(1150, 235, button="left") # set y-rotation to 0
        typewrite("0")
        press("enter")
        
        click(1150, 235, button="right") # Save the keyframe
        moveTo(1150, 260)
        click()

        # set the last frame to 360degrees
        click(577, 780, button="left")  # click the frame number down the bottom to the left of the play button
        click()
        moveTo(1150, 235)
        doubleClick(1150, 235)  # set y-rotation to 360
        typewrite("360")
        press("enter")

        click(1150, 235, button="right") # Save the keyframe
        click()
        
            # PLAY THE VIDEO
        click(715, 815, button="left")  # Click Play
        time.sleep(4.2)
        click(715, 815, button="left")  # Click Pause
        
            # RENDER THE IMAGE AND SAVE THEM
        directory = "/Users/jack/Desktop/Projects/3DImageDataSampler/"
        outputImageName = "Man"

        moveTo(1428, 440) # move to within the right scroll bar
        dragRel(0, 150)
        click(1350, 645, button="left")  # click on the output box and write the path (note: last is a file)
        typewrite(directory + outputImageName)
        press("enter")

        click(1300, 720, button="left")     # click on the output format
        moveTo(1000, 585, duration = 0.2)   # select PNG
        click()

        click(1375, 715, button="left")   # click RGB format
        moveTo(1428, 440)                     # scroll back up to the top
        dragRel(0, -150)
        click(1335, 300, button="left")   # click 'animation' to render the images and save them.
        """
        # click animation
        # wait until finished rendering
        # escape the rendering window

            # DELETE THE 3D IMAGE
        #click(1300, 150, button="left") # Select the 3D object
        #moveTo(700,400)                 # just move to within the window
        #press("x")                      # Short cut to delete 3D image
        #click()                         # Press Delete
            
       """

        

main()

