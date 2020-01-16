import bpy


startFrame = 1
endFrame = 462
scene = bpy.context.scene
fp = scene.render.filepath # get existing output path
scene.render.image_settings.file_format = 'PNG' # set output format to .png


for frame_nr in range(startFrame,endFrame):

 
    # set current frame 
    scene.frame_set(frame_nr)
       # ==========  set output path so render won't get overwritten
    scene.render.filepath = fp + str(frame_nr)
    bpy.ops.render.render(write_still=True) # render still





