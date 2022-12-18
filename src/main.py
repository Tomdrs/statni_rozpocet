from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"

@app.route('/na_druhou/<int:cislo>')
def ahoj(cislo):
    return str(cislo * cislo)