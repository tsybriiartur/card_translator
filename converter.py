import ezdxf
import trimesh
import open3d as o3d

def convert_dxf_to_stl(input_path: str, output_path: str):
    doc = ezdxf.readfile(input_path)
    msp = doc.modelspace()
    vertices = []
    faces = []
    for entity in msp:
        if entity.dxftype() == 'LINE':
            start = list(entity.dxf.start)
            end = list(entity.dxf.end)
            idx = len(vertices)
            vertices.extend([start, end, [(s + e)/2 for s, e in zip(start, end)]])
            faces.append([idx, idx+1, idx+2])
    if vertices:
        mesh = trimesh.Trimesh(vertices=vertices, faces=faces)
        mesh.export(output_path)

def convert_trimesh_to_format(mesh: trimesh.Trimesh, output_path: str):
    mesh.export(output_path)
