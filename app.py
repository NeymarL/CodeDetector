# /usr/bin/python2
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from flask import Flask
from flask import render_template, request
import CodeDetector

ALLOWED_EXTENSIONS = set(['c'])

app = Flask(__name__)
cd = CodeDetector.CodeDetector()
index = 0


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET'])
def home():
    global index
    index = 0
    return render_template('index.html')


@app.route('/upload_file', methods=['POST'])
def upload_file():
    global index
    file = request.files['upl']
    if file and allowed_file(file.filename) and index < 2:
        cd.add_file(index, file.read())
        index = index + 1


@app.route('/run', methods=['GET'])
def run():
    global index
    index = 0
    try:
        result = cd.run()
    except ValueError, e:
        return str(e)
    return render_template('result.html', result=result)


if __name__ == '__main__':
    app.debug = True
    app.run()
