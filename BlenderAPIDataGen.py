import bpy
import os
import math
import time
import numpy as np

# Generate the full paths of all the .obj files in 3D Datasets
datasetDirectoryPath = "/Users/jack/Desktop/Projects/Hai3D-Data-Gen/3D Datasets/"
objs = []
for folderName, subFolders, fileNames in os.walk(datasetDirectoryPath):
    for fileName in fileNames:
        if fileName.endswith(".obj"):
            objFilePath = os.path.join(folderName, fileName)
            objs.append(objFilePath)

# Delete Everything From the Scene
scene = bpy.context.scene
for ob in scene.objects:
    bpy.data.objects[ob.name].select = True
    bpy.ops.object.delete()

# Add in a the Plain Axes at (0, 0, 0)
bpy.ops.object.empty_add(type="PLAIN_AXES", location=(0, 0, 0))

# Add in a Camera (pointing at the Plain Axes)
bpy.ops.object.camera_add(location=(0, -10, 0), rotation=((math.pi/2), 0, 0), enter_editmode=True)
# pi/2 is equivalent to 90degrees. for some weird reson. Blender API is in rads. But GUI in degrees
                         
# Parent the Camera to the Empty
objects = bpy.data.objects
empty = objects['Empty']
camera = objects['Camera']
camera.parent = empty

# Import the .obj files and Render them.
for objFilePath in objs:
    
    if "Person1.obj" in objFile: # only practicing on one for now.

        # Import the obj. file (and give it texture *currently doesn't do this)
        bpy.ops.import_scene.obj(filepath=objFilePath)

        # centeter the 3D .obj about the central axis
        bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN")

        # Rezize .obj to fit within the camera view
        objDimensions = bpy.data.objects["CH_MNPCBotStreetGangSoldier01"].dimensions
        ratio = 3.5 / max(objDimensions)
        bpy.data.objects["CH_MNPCBotStreetGangSoldier01"].scale = [ratio, ratio, ratio]

        # Rotate the Camera and add in the KeyFrames
        bpy.context.scene.camera = bpy.data.objects['Camera']
        empty.rotation_mode = "XYZ"

        for i, x in enumerate(np.linspace(0,2*math.pi, 20)):
            empty.rotation_euler = (0, 0, x)
            empty.keyframe_insert(data_path="rotation_euler", frame=i, index=-1)

            bpy.context.scene.render.filepath = "/Users/jack/Desktop/Cube/%s%d.png" % (objectName, i)
            bpy.ops.render.render(scene="Scene", write_still = True, use_viewport=True)
        
        # Delete the .obj and move onto the next .obj
        # bpy.ops.object.delete()






## Scraps code ##################

""" This code should have worked but, scale worked instead :D
objDimensions[0] *= ratio  # updates the x-axis
objDimensions[1] *= ratio  # updates the y-axis
objDimensions[2] *= ratio  # updates the z-axis
"""
"""
for area in bpy.context.screen.areas:
    if area.type == 'VIEW_3D':
        for region in area.regions:
            if region.type == 'WINDOW':
                override = {'area': area, 'region': region, 'edit_object': bpy.context.edit_object}
                bpy.ops.view3d.camera_view_all(override)
"""
#import bpy
#from bpy import context

# Select objects that will be rendered
##for obj in scene.objects:
##    obj.select = False
##for obj in context.visible_objects:
##    if not (obj.hide or obj.hide_render):
##        obj.select = True

#bpy.ops.view3d.view_all()
#camera_to_view_selected()
#bpy.ops.view3d.camera.view_all() 

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


"""
num_frames = 90
gamma = math.pi * 2 / num_frames
for i in range(1, num_frames+1):
    empty.rotation_euler[2] = gamma * i
    empty.keyframe_insert(data_path="rotation_euler", frame=i, index=-1)

    bpy.context.scene.render.filepath = "/Users/jack/Desktop/Cube/Cube%d.png" % i
    bpy.ops.render.render(write_still = True, use_viewport=True)
"""



# Move the Camera around (not moving the camera any more. Moving the cube and rotating it
#if(len(bpy.data.cameras) == 1):
#obj = bpy.data.objects['Camera'] # bpy.types.Camera
#obj.rotation_euler[2] = 0.0
#obj.keyframe_insert(data_path="rotation", index = 1, frame=1.0)
#obj.rotation_euler[2] = 4 * math.pi
#obj.keyframe_insert(data_path="rotation", index = 2, frame=20.0)


"""
        for i, dimension in enumerate(objDimensions):
            newDimension = dimension * ratio
            bpy.data.objects["CH_MNPCBotStreetGangSoldier01"].dimensions[i] = newDimension

...     thelist[i] = number * 10

        x = bpy.data.objects["CH_MNPCBotStreetGangSoldier01"].dimensions[0]
        y = bpy.data.objects["CH_MNPCBotStreetGangSoldier01"].dimensions[1]
        z = bpy.data.objects["CH_MNPCBotStreetGangSoldier01"].dimensions[2]

        ratio = 3.5 / max(x,y,z)

        x *= ratio
        y *= ratio
        z *= ratio

        bpy.data.objects["CH_MNPCBotStreetGangSoldier01"].dimensions[0] = x
        bpy.data.objects["CH_MNPCBotStreetGangSoldier01"].dimensions[1] = y
        bpy.data.objects["CH_MNPCBotStreetGangSoldier01"].dimensions[2] = z
        
        
        # Give it texture
        # Render it (and save in desired Location)
        # Delete it

        for i in bpy.data.objects:
            if i not in objects:
                objectName = i.name
    """
