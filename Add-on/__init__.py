
import bpy

class ExportSceneGraphFromCollection(bpy.types.Operator):
    """Export this collection as a scene graph json file."""

    bl_idname = "blender_scene_exporter.export_scene_graph_from_collection"
    bl_label = "Export as Scene Graph (.json)"
    bl_options = {'REGISTER'}

    def execute(self, context):
        # TODO: Implement.
        return {'FINISHED'}

def menu_func_collection(self, context):
    self.layout.separator()
    self.layout.operator("blender_scene_exporter.export_scene_graph_from_collection")

my_classes = (
    ExportSceneGraphFromCollection,
)

def register():
    for my_class in my_classes:
        bpy.utils.register_class(my_class)
    bpy.types.OUTLINER_MT_collection.append(menu_func_collection)

def unregister():
    for my_class in my_classes:
        bpy.utils.unregister_class(my_class)
    bpy.types.OUTLINER_MT_collection.remove(menu_func_collection)
