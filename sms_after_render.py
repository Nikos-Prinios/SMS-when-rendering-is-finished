bl_info = {
    "name": "SMS notification after Render",
    "description": "...",
    "author": "Nikos Priniotakis",
    "version": (1, 5),
    "blender": (2, 74, 0),
    "location": "",
    "warning": "",
    "wiki_url": "",
    "category": "Render"}

import bpy
from bpy.app.handlers import persistent
import nexmo

@persistent
def render_complete_handler(sms):
    client = nexmo.Client(key='65d96651', secret='ea592f4844728f46')
    client.send_message({'from': '+33644632797', 'to': '33781247423', 'text': 'Your render is finished, my lord.'})

def register():
    bpy.app.handlers.render_complete.append(render_complete_handler)


def unregister():
    bpy.app.handlers.render_complete.remove(render_complete_handler)

if __name__ == "__main__":
    register()
