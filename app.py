# app.py
# -*- coding: utf-8 -*-

from flask import Flask
import CodeDetector

app = Flask(__name__)
cd = CodeDetector()


@app.route('add/0', methods=['GET'])
def add_file_0():
    cd.add_file(0, content)
