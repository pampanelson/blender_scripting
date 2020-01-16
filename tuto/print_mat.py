import bpy
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