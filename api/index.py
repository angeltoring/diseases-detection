import os
import time
from flask import Flask, send_file, request, jsonify
import subprocess
import shutil
from yolomodel.main import model_main

app = Flask(__name__)

def capture_image():
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    image_path = f"/home/orangepi/Desktop/capture_fswebcam/captured/image_{timestamp}.jpg"
    skip_frames = 20
    command = f"fswebcam -r 1920x1080 --no-banner -S {skip_frames} {image_path}"
    subprocess.run(command, shell=True, check=True)
    return image_path

@app.route('/capture', methods=['GET'])
def capture_and_send_image():
    image_path = capture_image()
    return send_file(image_path, mimetype="image/jpeg")

@app.route('/', methods=['GET'])
def check():
    return "SUCCESS"

@app.route('/detect', methods=['POST'])
def process_image():
    
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected for uploading'}), 400
    
    try:
        # Clear the images folder if it exists, otherwise create it
        image_folder = 'captured'
        
        if os.path.exists(image_folder):
            shutil.rmtree(image_folder)
        os.makedirs(image_folder)

        file_path = os.path.join(image_folder,'req-image.jpg')
        file.save(file_path)

        model_main()

        # Return a success response
        return jsonify({'success': 'Image processed successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500