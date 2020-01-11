import bpy
from pathlib import Path

# get all blender files from materials pack
target_directory_in_str = "/Volumes/data/blenderdata/EEVEE-Materials"
pathlist = Path(target_directory_in_str).glob('**/*.blend')


for path in pathlist:
    # because path is object not string
    path_in_str = str(path)
    # print(path)

    # read material data from each target blend file
    with bpy.data.libraries.load(path_in_str) as (data_from, data_to):
        # if has material
        if len(data_from.materials) > 0:
            for matName in data_from.materials:

                # print(mat)

                # append to current object material slot
                
                path_in_str += "\\Material\\"  # material path under blend file

                bpy.ops.wm.append(filename=matName, directory=path_in_str)  # append to current project file
                mat = bpy.data.materials.get(matName) 
                bpy.context.active_object.data.materials.append(mat) # append into current object material slot
