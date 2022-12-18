from flask import Flask, render_template
from pocketbase import PocketBase

import os

app = Flask(__name__)

@app.route('/')
def hello():
    index = str(open("frontend/index.html").read())
    return index

# Potreba vlozit testovaci data
@app.route('/rozpocet/<int:rok>')
def rozpocet_na_rok(rok):
    client = PocketBase(os.environ["POCKETBASE_URL"])

    rozpocty = client.records.get_full_list(
        "budgets",
        200,
        { "sort": "-created" }
    )

    spravny_rozpocet = next(rozpocet for rozpocet in rozpocty if rozpocet.year == rok)

    return str(spravny_rozpocet.total_income)

@app.route('/na_druhou/<int:cislo>')
def ahoj(cislo):
    return str(cislo * cislo)