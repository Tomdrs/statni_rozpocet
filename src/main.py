from flask import Flask, render_template, jsonify, request
from pocketbase import PocketBase

from models import Budget, Expenses, State_levies_average, Investment

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

@app.route('/investice')
def investice():
    client = PocketBase(os.environ["POCKETBASE_URL"])

    investice = client.records.get_full_list(
        "investments",
        200,
        { "sort": "-created" }
    )

    investice = list(map(lambda x: Investment(x), investice))
    investice_json = list(map(lambda x: x.to_json(), investice))
    return jsonify(investice_json = investice_json)

@app.route('/vypocet')
def vypocet():
    prumerny_obcan = prumerny_obcan()

    gross_income = request.args.get('gross_income')
    deti = request.args.get('deti')
    social_insurance = request.args.get('social_insurance')
    vat_books_music_medicine_water_accomodations = request.args.get('vat_books_music_medicine_water_accomodations')
    vat_food_mhd_medical_devices = request.args.get('vat_food_mhd_medical_devices')
    vat_21 = request.args.get('vat_21')
    capital_gains = request.args.get('capital_gains')
    gambling_tax = request.args.get('gambling_tax')
    consumer_tax_car_fuel = request.args.get('consumer_tax_car_fuel')
    consumer_tax_beer = request.args.get('consumer_tax_beer')
    consumer_tax_tobacco = request.args.get('consumer_tax_tobacco')
    consumer_tax_alcohol = request.args.get('consumer_tax_alcohol')
