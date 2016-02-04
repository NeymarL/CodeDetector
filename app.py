# /usr/bin/python2
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from flask import Flask
from flask import render_template, request
import CodeDetector

ALLOWED_EXTENSIONS = set(['txt', 'c'])

app = Flask(__name__)
cd = CodeDetector.CodeDetector()


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/upload_file/<int:index>', methods=['POST'])
def upload_file(index):
    file = request.files['file']
    print 'File : ' + file.read()
    if file and allowed_file(file.filename) and index >= 0 and index <= 1:
        cd.add_file(index, file.stream.read())
        return "Upload Success!"
    return 'Upload Failed!'


@app.route('/run', methods=['POST'])
def run():
    files = ['', '']
    files[0] = request.files['file1']
    files[1] = request.files['file2']
    for i in range(2):
        if files[i] and allowed_file(files[i].filename):
            # print files[i].stream.read()
            cd.add_file(i, files[i].read())
        else:
            return 'File Type Error'
    result = cd.run()
    return result


if __name__ == '__main__':
    app.debug = True
    app.run()
