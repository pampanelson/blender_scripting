import bpy, bmesh
import mathutils

from bpy import context

obj = context.active_object
# v = obj.data.vertices[0]

print(str(len(obj.data.vertices)))

if obj.mode == 'EDIT':
    # this works only in edit mode,
    bm = bmesh.from_edit_mesh(obj.data)
    vertices = bm.verts

else:
    # this works only in object mode,
    vertices = obj.data.vertices

#  set location of vertices
for vert in vertices:
    vert.co += mathutils.Vector((1,1,0))

# set origin after change location of vertices
bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')

vertsLocal = [vert.co for vert in vertices]
vertsGlobal = [obj.matrix_world @ vert.co for vert in vertices]  # USE @ for matrix multiplication

# coordinates as tuples
plain_vertsLocal = [vert.to_tuple() for vert in vertsLocal]
plain_vertsGlobal = [vert.to_tuple() for vert in vertsGlobal]
print('local')
print(plain_vertsLocal)
print('global')
print(plain_vertsGlobal)

print('------------')


