from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def hello():
    index = str(open("frontend/index.html").read())
    return index

@app.route('/na_druhou/<int:cislo>')
def ahoj(cislo):
    return str(cislo * cislo)