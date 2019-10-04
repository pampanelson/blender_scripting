import bpy
mats_dict = {} # don't need to record materil , use bpy.data.materials['matName']  instead


# select a mesh =================
# bpy.data.objects['Cube'].select_set(True)


# select and set material ============= 
mat = bpy.data.materials["mat300"] # for test only ------
obj = bpy.data.objects['Cube']
if len(obj.material_slots) == 0:
    obj.select_set(True)
    bpy.ops.object.material_slot_add()

obj.material_slots[0].material = mat
obj.select_set(False)


# for i in range(1000):
#     key = "mat" + str(i)
#     mat = bpy.data.materials.new(key)
#     # set base color 
#     mat.diffuse_color = (i/1000,0.0,0.0,1.0)



