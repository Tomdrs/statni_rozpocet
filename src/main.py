from flask import Flask, render_template, jsonify
from pocketbase import PocketBase

from models import Budget, Expenses, State_levies_average

import os

app = Flask(__name__, static_url_path = '/static', static_folder = '../static', template_folder = "../frontend")

@app.route('/')
def hello():
    return render_template("index.html")

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
    return Budget(spravny_rozpocet).to_json()

@app.route('/vydaje/<int:rok>')
def vydaje_na_rok(rok):
    client = PocketBase(os.environ["POCKETBASE_URL"])

    vydaje = client.records.get_full_list(
        "expenses",
        200,
        { "sort": "-created" }
    )

    spravny_vydaj = next(vydaj for vydaj in vydaje if vydaj.year == rok)
    return Expenses(spravny_vydaj).to_json()

@app.route('/prumerny_obcan')
def prumerny_obcan():
    client = PocketBase(os.environ["POCKETBASE_URL"])

    prumerni_lide = client.records.get_full_list(
        "state_levies_average",
        200,
        { "sort": "-created" }
    )

    prumer = prumerni_lide[0]
    return State_levies_average(prumer).to_json()