bl_info = {
    "name" : "Object Adder",
    "Author" : "ZheHua Zhang",
    "version" : {1, 0},
    "blender" : {3, 3, 1},
    "location" : "View_3D > Tool",
    "warning" : "nothing to worry about",
    "wiki_url" : "",
    "category" : "Add Mesh",
}
    




import bpy

class Panel_1(bpy.types.Panel):
    bl_label = "A Panel"
    bl_idname = "PT_Panel1"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'New Tab'
    
    def draw(self,context):
        layout = self.layout
        
        row = layout.row()
        row.label(text = "magic buttons",icon = 'OUTLINER_OB_ARMATURE')
        
        row = layout.row()
        row.label(text = "CUBE",icon = 'CUBE')
        row.operator("mesh.primitive_cube_add")
        
        row = layout.row()
        row.label(text = "SPHERE",icon = 'SPHERE')
        row.operator("mesh.primitive_uv_sphere_add")
#        row.operator("transform.rotate(value=0.918472, orient_axis='Z', orient_type='VIEW', orient_matrix=((0.410028, 0.911976, -0.0132645), (-0.401742, 0.193643, 0.895045), (0.818828, -0.361665, 0.445779)), orient_matrix_type='VIEW', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=False, use_snap_edit=False, use_snap_nonedit=False, use_snap_selectable=False)")

        
class Panel_2(bpy.types.Panel):
    bl_label = "Not A Button"
    bl_idname = "PT_Panel2"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'New Tab'
    bl_parent_id =  "PT_Panel1"
    bl_options = {"DEFAULT_CLOSED"}
    
    def draw(self,context):
        layout = self.layout
        
        row = layout.row()
        row.label(text = "no magic buttons",icon = 'OUTLINER_OB_ARMATURE')

class Panel_3(bpy.types.Panel):
    bl_label = "Not A Button As Well"
    bl_idname = "PT_Panel3"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'New Tab'
    bl_parent_id =  "PT_Panel1"
    bl_options = {"DEFAULT_CLOSED"}
    
    
    def draw(self,context):
        layout = self.layout
        
        row = layout.row()
        row.label(text = "no magic buttons",icon = 'OUTLINER_OB_ARMATURE')


def register():
    bpy.utils.register_class(Panel_1)
    bpy.utils.register_class(Panel_2)
    bpy.utils.register_class(Panel_3)
    
def unregister():
    bpy.utils.unregister_class(Panel_1)
    bpy.utils.unregister_class(Panel_2)
    bpy.utils.unregister_class(Panel_3)
    
if __name__  == "__main__":
    
    register()
    
    