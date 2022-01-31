import os
import string
import random
import json
import datetime
from flask import Flask, flash, request, redirect, url_for,jsonify
from werkzeug.utils import secure_filename

# initializing size of string
N = 21

res = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k = N))
UPLOAD_FOLDER = '/tmp/' + res + '/'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
           # img = Image.open(BytesIO(file.stream.read())
            os.mkdir(UPLOAD_FOLDER)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            time = datetime.datetime.now()
            data = {
                     "id": res,
                     "name": filename,
                     "image": os.path.getsize(UPLOAD_FOLDER + '/' + filename),
                     "timestamp": time.isoformat()
                    }
            return jsonify(data)  #"hello" #redirect(url_for('uploaded_file', filename=filename))

    return redirect(request.url)

@app.route('/image/<word>', methods=['GET'])
def get_file(word):
    if request.method == 'GET':
        UPLOAD_WORD = '/tmp/' + word
        if os.path.isdir(UPLOAD_WORD):
            time = datetime.datetime.now()
            filename = os.listdir(UPLOAD_WORD)[0]
            data = {
                     "id": word,
                     "name": filename,
                     "image": os.path.getsize(UPLOAD_WORD + '/' + filename),
                     "timestamp": time.isoformat()
                    }
            return jsonify(data)

    return redirect(request.url)

@app.route('/healthy')
def healthy():
    return 'healthy'

if __name__ == "__main__":
  app.run(host ='0.0.0.0', port = 8080, debug = True)
