import bpy
import os
import math
import numpy as np

# Generate the full paths of all the .obj files in 3D Datasets
datasetDirectoryPath = "/Users/jack/Desktop/Projects/Hai3D-Data-Gen/PASCAL DATASET/"
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

# Add in an Empty at (0, 0, 0) with type Plain Axes
bpy.ops.object.empty_add(type="PLAIN_AXES", location=(0, 0, 0))

# Add in a Camera (pointing perpendicular to the Plain Axes)
bpy.ops.object.camera_add(location=(0, -10, 0), rotation=((math.pi/2), 0, 0), enter_editmode=True)
# pi/2 is equivalent to 90degrees. for some weird reson. Blender API is in rads. But GUI in degrees
                         
# Parent the Camera to the Empty
initialObjects = bpy.data.objects
empty = initialObjects['Empty']
camera = initialObjects['Camera']
camera.parent = empty

# Create Camera Animation (by rotating the Empty)
bpy.context.scene.camera = bpy.data.objects['Camera']
empty.rotation_mode = "XYZ"
frames = 20
bpy.data.scenes["Scene"].frame_end = frames
for i, rotation in enumerate(np.linspace(0,2*math.pi, frames)):          # 0 to 360 degrees in 20 frames
    empty.rotation_euler = (0, 0, x)                                     # This rotation pans the camera
    empty.keyframe_insert(data_path="rotation_euler", frame=i, index=-1) # around the empty like a turntable

# Import the .obj files and Render them.
for objFilePath in objs:

    # Import the .obj file
    bpy.ops.import_scene.obj(filepath=objFilePath)
    
    # Texture the .obj file
    """
    for area in bpy.context.screen.areas: # iterate through areas in current screen
        if area.type == 'VIEW_3D':
            for space in area.spaces: # iterate through spaces in current VIEW_3D area
                if space.type == 'VIEW_3D': # check if space is a 3D view
                    space.viewport_shade = 'TEXTURED' # set the viewport shading to rendered
    """
    
    if len(bpy.context.selected_objects) > 1: # For the moment the solution only works for .objs that are one polygon
        bpy.ops.object.delete()               # if the object has more than one poly (e.g. a poly for arms, legs, eyes,
        continue                              # wheels etc.) it doesn't resize correctly.

    # Get the name of the .obj
    for object in bpy.context.selected_objects:
        objName = object.name

    # center the .obj about the central axis
    bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN")

    # Rezize .obj to fit within the camera view
    objDimensions = bpy.data.objects[objName].dimensions
    ratio = 3.5 / max(objDimensions)
    bpy.data.objects[objName].scale = [ratio, ratio, ratio]

    # Render the Images (save them as .png in PASCAL NEW Dataset)
    newLocation = objFilePath.replace(".obj", ".pgn").replace("PASCAL DATASET", "PASCAL NEW")
    bpy.context.scene.render.filepath = newLocation
    bpy.ops.render.render(animation=True)
    
    # Delete the .obj and move onto the next .obj
    bpy.ops.object.delete()
