import bpy
import math

# constants + variables
theta = math.pi/3
FACES = [
    (0, 1, 2, 3),
    (0, 3, 7, 4),
    (7, 6, 5, 4),
    (5, 6, 2, 1),
    (3, 2, 6, 7),
    (4, 5, 1, 0),
]

def define_origin_vertices(theta):
    cos_angle = math.cos(theta)
    sin_angle = math.sin(theta)
    
    return [
        [1, 0, 0],
        [cos_angle, sin_angle, 0],
        [cos_angle, (cos_angle - (cos_angle ** 2))/sin_angle, (math.sqrt(1 - 3 * cos_angle ** 2 + 2 * cos_angle**3))/sin_angle]
    ]

def create_rhombohedron(new_x, new_y, new_z, new_size):
    origin_vertices = define_origin_vertices(theta)
    
    vertices = [
        [new_x, new_y, new_z], 
        [new_x + new_size * origin_vertices[1][0], new_y + new_size * origin_vertices[1][1], new_z + new_size * origin_vertices[1][2]],
        [new_x + new_size * (origin_vertices[0][0] + origin_vertices[1][0]), new_y + new_size * (origin_vertices[0][1] + origin_vertices[1][1]), new_z + new_size * (origin_vertices[0][2] + origin_vertices[1][2])],
        [new_x + new_size * origin_vertices[0][0], new_y + new_size * origin_vertices[0][1], new_z + new_size * origin_vertices[0][2]],
        [new_x + new_size * origin_vertices[2][0], new_y + new_size * origin_vertices[2][1], new_z + new_size * origin_vertices[2][2]],
        [new_x + new_size * (origin_vertices[1][0] + origin_vertices[2][0]), new_y + new_size * (origin_vertices[1][1] + origin_vertices[2][1]), new_z + new_size * (origin_vertices[1][2] + origin_vertices[2][2])],
        [new_x + new_size * (origin_vertices[0][0] + origin_vertices[1][0] + origin_vertices[2][0]), new_y + new_size * (origin_vertices[0][1] + origin_vertices[1][1] + origin_vertices[2][1]), new_z + new_size * (origin_vertices[0][2] + origin_vertices[1][2] + origin_vertices[2][2])],
        [new_x + new_size * (origin_vertices[0][0] + origin_vertices[2][0]), new_y + new_size * (origin_vertices[0][1] + origin_vertices[2][1]), new_z + new_size * (origin_vertices[0][2] + origin_vertices[2][2])]
    ]
             
    mesh_data = bpy.data.meshes.new("rhombohedron_data")
    mesh_data.from_pydata(vertices, [], FACES)
    mesh_data.update()
    
    mesh_obj = bpy.data.objects.new("rhombohedron_object", mesh_data)
    bpy.context.collection.objects.link(mesh_obj)

def calculate_new_coordinates(x, y, z, dimension_x, dimension_y, dimension_z, new_size):
    origin_vertices = define_origin_vertices(theta)
    
    new_x = x + new_size * (dimension_x * origin_vertices[0][0] + dimension_y * origin_vertices[1][0] + dimension_z * origin_vertices[2][0])
    new_y = y + new_size * (dimension_x * origin_vertices[0][1] + dimension_y * origin_vertices[1][1] + dimension_z * origin_vertices[2][1])
    new_z = z + new_size * (dimension_x * origin_vertices[0][2] + dimension_y * origin_vertices[1][2] + dimension_z * origin_vertices[2][2])
    return new_x, new_y, new_z
    
def generate_fractal(x, y, z, rhombohedron_size, max_level):
    if max_level == 0:
        create_rhombohedron(x, y, z, rhombohedron_size)
        return
    
    new_size = rhombohedron_size/3
    inverse_fractal = bpy.context.scene.fractal_properties.inverse_fractal
    
    for dimension_x in range(3):
        for dimension_y in range(3):
            for dimension_z in range(3):
                middle_shape_condition = (dimension_x == 1 and dimension_y == 1) or (dimension_y == 1 and dimension_z == 1) or (dimension_x == 1 and dimension_z == 1)
                
                if (not inverse_fractal and not middle_shape_condition) or (inverse_fractal and middle_shape_condition):
                    new_x, new_y, new_z = calculate_new_coordinates(x, y, z, dimension_x, dimension_y, dimension_z, new_size)
                    generate_fractal(new_x, new_y, new_z, new_size, max_level - 1)

def delete_previous_fractal():
    rotation = None 
    
    for obj in bpy.data.objects:
        if obj.name.startswith("rhombohedron_object"):
            rotation = obj.rotation_euler.copy()
            bpy.data.objects.remove(obj, do_unlink = True)
    
    return rotation

def join_rhombohedron_objects(rotation, context):
    """Join objects into one object, place pivot point in centre of object & restore rotation and colors"""
    
    new_obj = bpy.data.objects.get("rhombohedron_object")
    
    bpy.context.view_layer.objects.active = new_obj
    bpy.ops.object.select_all(action = 'SELECT')
    
    if (len(bpy.data.objects) > 1):
        bpy.ops.object.join()
        
    bpy.ops.object.origin_set(type = 'ORIGIN_GEOMETRY')
    
    if rotation:
        new_obj.rotation_euler = rotation
        
    update_rgb_colors(new_obj, context)
    
def update_fractal(self, context):
    rotation = delete_previous_fractal()
    
    generate_fractal(0, 0, 0, 10, self.max_level)
    
    join_rhombohedron_objects(rotation, context)
    
def update_angle(self, context):
    global theta
    theta = math.radians(self.acute_angle)

    update_fractal(self, context)
    
def update_rgb_colors(self, context):
    obj = context.object
    
    if not obj.active_material:
        rgb_color = bpy.data.materials.new(name = "RGBColor")
        rgb_color.use_nodes = True
        obj.active_material = rgb_color
    else:
        rgb_color = obj.active_material
    
    bsdf_node = rgb_color.node_tree.nodes.get('Principled BSDF')
    if not bsdf_node:
        bsdf_node = rgb_color.node_tree.nodes.new(type = 'ShaderNodeBsdfPrincipled')
    
    rgb_node = rgb_color.node_tree.nodes.get('Combine Color')
    if not rgb_node:
        rgb_node = rgb_color.node_tree.nodes.new(type = 'ShaderNodeCombineColor')
    
    rgb_color.node_tree.links.new(rgb_node.outputs[0], bsdf_node.inputs[0])
 
    rgb_node.inputs[0].default_value = context.scene.mesh_properties.red_value
    rgb_node.inputs[1].default_value = context.scene.mesh_properties.green_value
    rgb_node.inputs[2].default_value = context.scene.mesh_properties.blue_value

class FractalProperties(bpy.types.PropertyGroup):
    max_level : bpy.props.IntProperty(
        name = "Max level",
        description = "Set max level",
        min = 0,
        max = 2,
        default = 0,
        update = update_fractal
    )
    acute_angle : bpy.props.IntProperty(
        name = "Angle",
        description = "Set acute angle of rhombus face",
        min = 10,
        max = 90,
        default = 60,
        update = update_angle
    )
    inverse_fractal : bpy.props.BoolProperty(
        name = "Inverse fractal",
        description = "Determine which shapes should be visible. If enabled, the middle shapes are displayed and the other shapes not",
        default = False,
        update = update_fractal
    )
   
class MeshProperties(bpy.types.PropertyGroup):
    red_value : bpy.props.FloatProperty(
        name = "Red value",
        min = 0.0,
        max = 1.0,
        default = 0.0,
        update = update_rgb_colors
    )
    green_value : bpy.props.FloatProperty(
        name = "Green value",
        min = 0.0,
        max = 1.0,
        default = 0.0,
        update = update_rgb_colors
    )
    blue_value : bpy.props.FloatProperty(
        name = "Blue value",
        min = 0.0,
        max = 1.0,
        default = 0.0,
        update = update_rgb_colors
    )

class OBJECT_PT_fractal_panel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_fractal_panel"
    bl_label = "My Fractal Panel"
    bl_category = "Fractal"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        object = context.object
        
        layout.prop(scene.fractal_properties, "max_level")
        
        if not object:
            layout.alert = True
            layout.label(text = "Change level to add fractal to scene!")
        else:   
            layout.prop(scene.fractal_properties, "acute_angle")
            layout.prop(scene.fractal_properties, "inverse_fractal")
            add_color_layout(layout, scene)
            layout.prop(object, "rotation_euler", text = "Rotation")
            
def add_color_layout(layout, scene):
    box = layout.box()
    box.label(text = "RGB Color")
    split = box.split()
    
    labels = [ "Red", "Green", "Blue"]
    props = ["red_value", "green_value", "blue_value"]
    
    for i in range(3):
        col = split.column()
        col.label(text = labels[i])
        col.prop(scene.mesh_properties, props[i])

classes = (
    FractalProperties,
    MeshProperties,
    OBJECT_PT_fractal_panel
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        
    bpy.types.Scene.fractal_properties = bpy.props.PointerProperty(type = FractalProperties)
    bpy.types.Scene.mesh_properties = bpy.props.PointerProperty(type = MeshProperties)
        
def unregister():
    del bpy.types.Scene.fractal_properties
    del bpy.types.Scene.mesh_properties
    for cls in classes:
        bpy.utils.unregister_class(cls)
        
if __name__ == "__main__":
    register()