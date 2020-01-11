import bpy
 
path = "/Users/SOMEONE/Desktop/import-material_test/test1.blend\\Material\\"
material_name = "test_material1"
bpy.ops.wm.append(filename=material_name, directory=path)


print ()
print ('List of all materials')
print ()

pymat = bpy.data.materials
print('material_library = ', pymat)
for idx, i in enumerate(pymat):
    print ( 'i=',i)
    name = i.name 
    print(name)
  
print ()