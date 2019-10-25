import bpy, bmesh
import mathutils

from bpy import context


verts_raw = (
    ["a0",1.0,-.0,-1.0],
    ["a1",1.0,-1.0,1.0],
    ["a2",-1.0,-1.0,-1.0],
    ["a3",-1.0,-1.0,1.0],
    ["a4",1.0,1.0,-1.0],
    ["a5",1.0,1.0,1.0],
    ["a6",-1.0,1.0,-1.0],
    ["a7",-1.0,1.0,1.0],
)

edges_raw = (
    ["a4","a0"],
    ["a4","a6"],
    ["a4","a5"],
    ["a0","a2"],
    ["a0","a1"],
    ["a2","a6"],
    ["a2","a3"],
    ["a6","a7"],
    ["a5","a1"],
    ["a5","a7"],
    ["a1","a3"],
    ["a3","a7"],
)

verts = []
for v in verts_raw:
    verts.append(v[1:])
    
edges = []
for a, b in edges_raw:
    edges.append((int(a[1:]), int(b[1:])))

me = bpy.data.meshes.new("")
me.from_pydata(verts, edges, [])
me.validate()
me.update()

ob = bpy.data.objects.new("", me)

bpy.context.collection.objects.link(ob)