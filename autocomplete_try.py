import bpy


import bpy
 
bpy.ops.mesh.primitive_cube_add(location=(0, 1, 0))
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.transform.rotate(value=0.785398,orient_axis='Z')
bpy.ops.object.mode_set(mode='OBJECT')
Obj = bpy.context.active_object
mod = Obj.modifiers.new("Bevel", 'BEVEL')
mod.segments = 3
bpy.ops.object.shade_smooth()
mod1 = Obj.modifiers.new("Array", 'ARRAY')
mod1.count = 10
mod2 = Obj.modifiers.new("Array", 'ARRAY')
mod2.relative_offset_displace[0] = 0.05
mod2.relative_offset_displace[1] = 0.5


