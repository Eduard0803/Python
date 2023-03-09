from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# define the folder
app.config['UPLOAD_FOLDER'] = 'uploads'

# define allowed extensions
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}

# check the file extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# display the form
@app.route('/')
def index():
    return render_template('index.html')

# print the data
@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    date = request.form['date']
    site = request.form['site']

    if 'file' not in request.files:
        return 'file not uploaded!'
    file = request.files['file']

    if file.filename == '':
        return 'file name invalid!'
    # check the file extension is allowed
    if not allowed_file(file.filename):
        return 'file extension invalid!'
    # save the files in folder
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    # display the file 'result.html' rendered
    return render_template('result.html', name=name, date=date, email=email, site=site, file=file.filename)

# create the local ip
if __name__ == '__main__':
    app.run(debug=True)
