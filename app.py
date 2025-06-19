from flask import Flask, request, send_file
from converter import convert_dxf_to_stl
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/convert', methods=['POST'])
def convert():
    uploaded_file = request.files['file']
    input_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
    output_path = input_path.replace(".dxf", ".stl")
    uploaded_file.save(input_path)
    convert_dxf_to_stl(input_path, output_path)
    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
