#!/usr/bin/env python3

from os import path
from flask import Flask, render_template
app = Flask(__name__, template_folder='/home/didik/FGA-final-project/flask/')

# app.config['DEBUG'] = True

@app.route('/')
def home():
    return render_template('web.html')

if __name__ =='__main__':
    app.run()