from converter import convert_dxf_to_stl
from visualizer import show_model

# шлях до вхідного та вихідного файлу
input_dxf = "sample.dxf"
output_stl = "sample.stl"

# конвертація
convert_dxf_to_stl(input_dxf, output_stl)

# візуалізація
show_model(output_stl)
