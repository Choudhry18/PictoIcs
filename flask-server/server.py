from flask import Flask,jsonify,request
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_cors import CORS

#This had to be changed in flaskuploads.py |from werkzeug import secure_filename,FileStorage|
#from werkzeug.utils import secure_filename
#from werkzeug.datastructures import  FileStorage

app = Flask(__name__)
# Configure the uploaded images storage
photos = UploadSet('photos', IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'  # Destination folder for uploaded files
configure_uploads(app, photos)

CORS(app)
@app.route("/members")
def members():
    return jsonify({"members": ["Member1", "Member2", "Member3"]})


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return 'No file part', 400
    
    file = request.files['image']
    if file.filename == '':
        print(2)
        return 'No selected file', 400

    if file:
        filename = photos.save(file)
        return f'File {filename} uploaded successfully', 200

if __name__ == "__main__":
    app.run(debug = True)

