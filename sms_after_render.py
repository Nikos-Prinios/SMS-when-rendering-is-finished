bl_info = {
    "name": "SMS notification after Render",
    "description": "...",
    "author": "--",
    "version": (1, 0),
    "blender": (2, 74, 0),
    "location": "",
    "warning": "",
    "wiki_url": "",
    "category": "Render"}

import bpy
import os
import urllib
import urllib.request
from bpy.app.handlers import persistent

@persistent
def render_complete_handler(sms):
    # The following line has to be changed to match your SMS API protocol
    x = urllib.request.urlopen('https://smsapi.free-mobile.fr/sendmsg?user=your_login&pass=your_password&msg=Render%20Finished%20!')

def register():
    bpy.app.handlers.render_complete.append(render_complete_handler)


def unregister():
    bpy.app.handlers.render_complete.remove(render_complete_handler)

if __name__ == "__main__":
    register()
