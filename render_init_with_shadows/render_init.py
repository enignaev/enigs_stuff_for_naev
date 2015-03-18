#/usr/bin/env python

import math
import bpy
import os

def Initialize( intensity=1., resolution=512 ):
   # variables to use
   scn = bpy.context.scene
   ctxt = scn.render

   # unlink stuff we don't want
   for obj in bpy.data.objects:
      if obj.type in ('CAMERA','LAMP'):
         scn.objects.unlink(obj)
   scn.update()

   # set the camera up
   cam = bpy.data.cameras.new('ORTHO')
   cam.type = 'ORTHO'
   cam.ortho_scale = 10.
   camobj = bpy.data.objects.new(name="Camera1", object_data=cam)
   camobj.location = -9.0, 0.0, 9.0
   camobj.rotation_mode = 'XYZ'
   camobj.rotation_euler = math.pi / 4., 0.0, -math.pi / 2.
   scn.objects.link(camobj)
   scn.update()
   scn.camera = camobj

   # Overhead Spot
   sun = bpy.data.lamps.new('Spot0','SPOT')
   sun.use_specular = False
   sun.energy = 32.8*intensity
   sun.color = 1.000, 1.000, 1.000
   sun.distance = 25
   sunobj = bpy.data.objects.new(name='MyLamp1', object_data=sun)
   sunobj.location = 9.0, -9.0, 14.0
   sunobj.rotation_mode = 'XYZ'
   sunobj.rotation_euler = 0.0, math.pi / 4., - math.pi / 4.
   scn.objects.link(sunobj)
   scn.update()
   
   # Overhead Spot 2
   sun = bpy.data.lamps.new('Spot9','SPOT')
   sun.use_specular = False
   sun.energy = 10.8*intensity
   sun.color = 0.900, 0.900, 1.000
   sun.distance = 25
   sunobj = bpy.data.objects.new(name='MyLamp1', object_data=sun)
   sunobj.location = -9.0, 9.0, 14.0
   sunobj.rotation_mode = 'XYZ'
   sunobj.rotation_euler = 0.0, math.pi / -4., - math.pi / 4.
   scn.objects.link(sunobj)
   scn.update()

   # Forward Upper Spot
   sun = bpy.data.lamps.new('Spot1','SPOT')
   sun.energy = 5.32*intensity
   sun.color = 0.900, 0.900, 1.000
   sunobj = bpy.data.objects.new(name='MyLamp2', object_data=sun)
   sunobj.location = 0.0, -15.0, 7.0
   sunobj.rotation_mode = 'XYZ'
   sunobj.rotation_euler = 1.13446, 0.0, 0.0
   scn.objects.link(sunobj)
   scn.update()
   
   # Forward Lower Spot
   sun = bpy.data.lamps.new('Spot2','SPOT')
   sun.energy = 2.08*intensity
   sun.color = 0.900, 0.900, 1.000
   sunobj = bpy.data.objects.new(name='MyLamp3', object_data=sun)
   sunobj.location = 0.0, -15.0, -7.0
   sunobj.rotation_mode = 'XYZ'
   sunobj.rotation_euler = 2.00712, 0.0, 0.0
   scn.objects.link(sunobj)
   scn.update()
   
   # Back Middle spot
   sun = bpy.data.lamps.new('Spot3','SPOT')
   sun.energy = 2.08*intensity
   sun.color = 0.900, 0.900, 1.000
   sunobj = bpy.data.objects.new(name='MyLamp5', object_data=sun)
   sunobj.location = 0.0, 15.0, -3.5
   sunobj.rotation_mode = 'XYZ'
   sunobj.rotation_euler = 4.71238, 0.0, 0.0
   scn.objects.link(sunobj)
   scn.update()
   
   # Left Middle spot
   sun = bpy.data.lamps.new('Spot4','SPOT')
   sun.energy = 2.08*intensity
   sun.color = 0.900, 0.900, 1.000
   sunobj = bpy.data.objects.new(name='MyLamp6', object_data=sun)
   sunobj.location = -15.0, 0.0, -3.5
   sunobj.rotation_mode = 'XYZ'
   sunobj.rotation_euler = 0.0, 1.57079, 3.14159
   scn.objects.link(sunobj)
   scn.update()

   # Right Middle spot
   sun = bpy.data.lamps.new('Spot5','SPOT')
   sun.energy = 2.08*intensity
   sun.color = 0.900, 0.900, 1.000
   sunobj = bpy.data.objects.new(name='MyLamp7', object_data=sun)
   sunobj.location = 15.0, 0.0, -3.5
   sunobj.rotation_mode = 'XYZ'
   sunobj.rotation_euler = 0.0, -1.57079, 3.14159
   scn.objects.link(sunobj)
   scn.update()

   # set the rendering context up
   ctxt.image_settings.file_format = 'PNG';
   ctxt.image_settings.color_mode = 'RGBA';
   ctxt.alpha_mode = 'PREMUL'
   ctxt.resolution_x = resolution
   ctxt.resolution_y = resolution
   ctxt.threads = 5
   ctxt.use_antialiasing = True
   ctxt.filepath = os.getcwd() + "/"

if __name__ == "__main__":
   Initialize()