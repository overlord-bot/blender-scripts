bl_info = {
    "name": "New Object",
    "author": "Your Name Here",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Adds a new Mesh Object",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh",
}

import bpy

class ShaderPanel(bpy.types.Panel):
    
    bl_label = "ShaderLib"
    bl_idname = "Shader_PT_Main"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "ShaderLib"

    def draw(self, context):
        layout = self.layout
        
        row = layout.row
        row.label(text = "select a shader")
        row.operator('')

 
class SimpleOperator(bpy.types.Operator):
    bl_idname = "object.simple_operator"
    bl_label = "Tool Name"
 
    def execute(self, context):
        print("Hello World")
        return {'FINISHED'}
 

        
def register():
    bpy.utils.register_class(ShaderPanel)
    bpy.utils.register_class(SimpleOperator)

def unregister():
    bpy.utils.unregister_class(ShaderPanel)
    bpy.utils.unregister_class(SimpleOperator)

if __name__ == "__main__":
    register()
