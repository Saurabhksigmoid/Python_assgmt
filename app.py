from operator import methodcaller
import os
from flask import Flask, render_template, request, redirect, send_file
from resources import list_all_files, download, upload, show_bucket, buck_create

app = Flask(__name__)
UPLOAD_FOLDER = "upload_files"
BUCKET = "ks17"

@app.route('/')
def start():
    return "APP RUNNING!!!\n Use '/home'to list all files in bucket"
    
@app.route("/home")
def home():
    contents = list_all_files(BUCKET)
    return render_template('index.html', contents=contents)

@app.route("/upload", methods=['POST'])
def upload_files():
    if request.method == "POST":
        f = request.files['file']
        f.save(os.path.join(UPLOAD_FOLDER, f.filename))
        upload(f"upload_files/{f.filename}", BUCKET, f.filename)
        return redirect("/home")


@app.route("/download/<filename>", methods=['GET'])
def download_files(filename):
    if request.method == 'GET':
        output = download(filename, BUCKET)
        return send_file(output, as_attachment=True)

@app.route("/createbucket")
def create_bucket():
    buck_create('name')
    contents = show_bucket()
    return render_template('files.html', contents=contents)

@app.route('/delete', methods=['GET'])
def delete():
    key = request.form['key']
    my_bucket = BUCKET
    output = delete(my_bucket, key)
    return redirect("/home")

    # contents = show_bucket()
    # return render_template('index.html', contents=contents)


@app.route("/bucket")
def bucket():
    contents = show_bucket()
    return render_template('files.html', contents=contents)


if __name__ == '__main__':
    app.run(debug=True)