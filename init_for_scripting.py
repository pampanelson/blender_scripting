import sys
import os
import bpy


# add system lib path into blender
# lib path set by pyenv 
sys.path.append("/Users/pampanie/.pyenv/versions/3.7.0/envs/python_blender_3_7_0/lib/python3.7/site-packages")

# get current blender file path
#  for example  '/Users/pampanie/app/blendproj/scripting/external_python_init.blend'
filepath = bpy.data.filepath

# get current working path
# /Users/pampanie/app/blendproj/scripting
directory = os.path.dirname(filepath)


