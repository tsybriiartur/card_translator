import open3d as o3d

def show_model(path):
    mesh = o3d.io.read_triangle_mesh(path)
    mesh.compute_vertex_normals()
    o3d.visualization.draw_geometries([mesh])
