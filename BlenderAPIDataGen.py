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

