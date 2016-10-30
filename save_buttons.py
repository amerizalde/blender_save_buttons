# https://www.blender.org/api/blender_python_api_current/bpy.ops.paint.html?highlight=bpy%20ops%20paint#module-bpy.ops.paint

import bpy
from bpy.types import Operator, Header, Panel

bl_info = {
        "name" : "Save Buttons",
        "author" : "Andrew Merizalde <andrewmerizalde@hotmail.com>",
        "version" : (1, 0, 0),
        "blender" : (2, 7, 8),
        "location" : "Text Editor > Tools > Save, Text Editor > Header",
        "description" :
            "Adds a save button to the Text Editor header, and panel",
        "warning" : "",
        "wiki_url" : "https://github.com/amerizalde/blender_save_buttons",
        "tracker_url" : "",
        "category" : "Text Editor"}

# callback
class SaveOperator(Operator):
    # the callback name
    bl_idname = "alm.save_text"
    bl_label = "SaveText"
    
    def execute(self, context):
        text = context.space_data.text
        
        if text.filepath:
            if text.is_dirty:
                bpy.ops.text.save()
            else:
                # no unnecessary actions
                pass
        else:
            bpy.ops.text.save_as()

        self.report({'INFO'}, "Done!")        
        return {"FINISHED"}

class SaveHeader(Header):
    bl_space_type = 'TEXT_EDITOR'
    bl_region_type = 'UI'
    bl_label = "Save"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("alm.save_text", text="Save", icon='TEXT')

class SavePanel(Panel):
    bl_space_type = 'TEXT_EDITOR'
    bl_region_type = 'UI'
    bl_label = "Save"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("alm.save_text", text="Save", icon='TEXT')
        

def register():
    bpy.utils.register_class(SaveOperator)
    bpy.utils.register_class(SaveHeader)
    bpy.utils.register_class(SavePanel)

    bpy.types.TEXT_HT_header.append(SaveHeader)
    
def unregister():
    bpy.types.TEXT_HT_header.remove(SaveHeader)

    bpy.utils.unregister_class(SaveHeader)
    bpy.utils.unregister_class(SavePanel)
    bpy.utils.unregister_class(SaveOperator)


if __name__ == "__main__":
    register()
