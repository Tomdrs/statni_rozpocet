from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def hello():
    index = str(open("frontend/index.html").read())
    return index

@app.route('/rozpocet/<int:rok>')
def rozpocet_na_rok(rok):
    if rok == 2020:
        return "23321847747474747"
    elif rok == 2021:
        return "2498743219982"
    elif rok == 2022:
        return "3"
    else:
        return "0"

@app.route('/na_druhou/<int:cislo>')
def ahoj(cislo):
    return str(cislo * cislo)