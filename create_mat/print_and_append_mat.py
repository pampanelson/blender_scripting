# import bpy
 

from pathlib import Path
directory_in_str = "/Volumes/data/blenderdata/EEVEE-Materials"
pathlist = Path(directory_in_str).glob('**/*.blend')
for path in pathlist:
     # because path is object not string
     path_in_str = str(path)
     print(path_in_str)


# print ()
# print ('List of all materials')
# print ()

# pymat = bpy.data.materials
# print('material_library = ', pymat)
# for idx, i in enumerate(pymat):
#     print ( 'i=',i)
#     name = i.name 
#     print(name)
  
# print ()



# path = "/Users/SOMEONE/Desktop/import-material_test/test1.blend\\Material\\"
# material_name = "test_material1"
# bpy.ops.wm.append(filename=material_name, directory=path)
