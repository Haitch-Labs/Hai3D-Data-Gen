# Create Plain axis
# Select the Camera and parent it to the main axis
# Change the camera settings to have perpendicular view of plain axes
# Rotate the Camera around the plain axis 360 degrees x10 in total of 100frames
# Delete the Default Cube
# Get the names of all our images
# Import an image                             |
# Center the image to fit the camera (ratio)  | - Repeated for each image in the dataset
# Rotate the 3D model (in increments)         |
# Render and save the image                   |

import bpy
import os
import math

# Generate the full paths of all the .obj files in 3D Datasets
datasetDirectoryPath = "/Users/jack/Desktop/Projects/Hai3D-Data-Gen/3D Datasets/"
objs = []
for folderName, subFolders, fileNames in os.walk(datasetDirectoryPath):
    for fileName in fileNames:
        if fileName.endswith(".obj"):
            objFile = os.path.join(folderName, fileName)
            objs.append(objFile)


# Delete Everything From the Scene
scene = bpy.context.scene
for ob in scene.objects:
    bpy.data.objects[ob.name].select = True
    bpy.ops.object.delete()

# Add in a the Plain Axes and Camera (give them settings)
bpy.ops.object.empty_add(type="PLAIN_AXES", location=(0, 0, 0))
bpy.ops.object.camera_add(location=(0, -10, 0), rotation=((math.pi/2), 0, 0)) # pi/2 is equivalent to 90degrees
                                                                              # for some weird reson. Blender API is in rads. But GUI in degrees
                         
# Parent the Empty to the Camera 
objects = bpy.data.objects
a = objects['Empty']
b = objects['Camera']
b.parent = a
 
                          
    
