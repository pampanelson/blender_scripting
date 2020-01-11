import bpy, bmesh
import random
 
startFrame = 0
endFrame = 5

scene = bpy.context.scene
fp = scene.render.filepath # get existing output path
scene.render.image_settings.file_format = 'PNG' # set output format to .png

obj = bpy.context.object                  # Reference to selected object
all_materials   = obj.data.materials      # All the materials of the selected object
no_of_materials = len(all_materials) # Number of materials on the sel. object
 

for frame_nr in range(startFrame,endFrame):

 
    # set current frame to frame 5
    scene.frame_set(frame_nr)

    bpy.ops.object.mode_set(mode = 'EDIT')  # Go to edit mode to create bmesh
    ob = bpy.context.object                 # Reference to selected object
    
    bm = bmesh.from_edit_mesh(ob.data)      # Create bmesh object from object mesh
    
    bm.select_mode = {'FACE'}               # Go to face selection mode
    # bm.faces[0].select_set(True)            # Select   face 0
    # bm.faces[1].select_set(False)           # Deselect face 1  

            # Create bmesh object from object mesh
    
    for face in bm.faces:        # Iterate over all of the object's faces
        face.material_index = random.randint(0, no_of_materials - 1)  # Assing random material to face
    
    ob.data.update()                            # Update the mesh from the bmesh data
    bpy.ops.object.mode_set(mode = 'OBJECT')    # Return to object mode</pre>


    # ==========  set output path so render won't get overwritten
    scene.render.filepath = fp + str(frame_nr)
    bpy.ops.render.render(write_still=True) # render still
