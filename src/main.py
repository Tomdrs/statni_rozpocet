from flask import Flask, render_template, jsonify, request
from pocketbase import PocketBase

from models import Budget, Expenses, State_levies_average, Investment
from tax_math import yearly_total_tax, expenses_ratio, investitions_ratio, budget_ratio

import os

app = Flask(__name__, static_url_path = '/static', static_folder = '../static', template_folder = "../frontend")

@app.route('/')
def hello():
    return render_template("index.html")

def fetch_rozpocet_na_rok(rok):
    client = PocketBase(os.environ["POCKETBASE_URL"])

    rozpocty = client.records.get_full_list(
        "budgets",
        200,
        { "sort": "-created" }
    )

    spravny_rozpocet = next(rozpocet for rozpocet in rozpocty if rozpocet.year == rok)
    return Budget(spravny_rozpocet)

@app.route('/rozpocet/<int:rok>')
def rozpocet_na_rok(rok):
    rozpocet = fetch_rozpocet_na_rok(rok)
    return rozpocet.to_json()

def fetch_vydaje_na_rok(rok):
    client = PocketBase(os.environ["POCKETBASE_URL"])

    vydaje = client.records.get_full_list(
        "expenses",
        200,
        { "sort": "-created" }
    )

    spravny_vydaj = next(vydaj for vydaj in vydaje if vydaj.year == rok)
    return Expenses(spravny_vydaj)

@app.route('/vydaje/<int:rok>')
def vydaje_na_rok(rok):
    vydaj = fetch_vydaje_na_rok(rok)
    return vydaj.to_json()

def fetch_prumerny_obcan():
    client = PocketBase(os.environ["POCKETBASE_URL"])

    prumerni_lide = client.records.get_full_list(
        "state_levies_average",
        200,
        { "sort": "-created" }
    )

    prumer = prumerni_lide[0]
    return State_levies_average(prumer)

@app.route('/prumerny_obcan')
def prumerny_obcan():
    obcan = fetch_prumerny_obcan()
    return obcan.to_json()

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

@app.route('/vypocet/<int:rok>')
def vypocet(rok):
    prumerny_obcan_hodnoty = fetch_prumerny_obcan()

    gross_income = int(request.args.get('gross_income') or prumerny_obcan_hodnoty.gross_income)
    deti = int(request.args.get('deti') or 0)
    social_insurance = int(request.args.get('social_insurance') or prumerny_obcan_hodnoty.social_insurance)
    vat_books_music_medicine_water_accomodations = int(request.args.get('vat_books_music_medicine_water_accomodations') or prumerny_obcan_hodnoty.vat_books_music_medicine_water_accomodations)
    vat_food_mhd_medical_devices = int(request.args.get('vat_food_mhd_medical_devices') or prumerny_obcan_hodnoty.vat_food_mhd_medical_devices)
    vat_21 = int(request.args.get('vat_21') or prumerny_obcan_hodnoty.vat_21)
    capital_gains = int(request.args.get('capital_gains') or prumerny_obcan_hodnoty.capital_gains)
    gambling_tax = int(request.args.get('gambling_tax') or prumerny_obcan_hodnoty.gambling_tax)
    consumer_tax_car_fuel = int(request.args.get('consumer_tax_car_fuel') or prumerny_obcan_hodnoty.consumer_tax_car_fuel)
    consumer_tax_beer = int(request.args.get('consumer_tax_beer') or prumerny_obcan_hodnoty.consumer_tax_beer)
    consumer_tax_tobacco = int(request.args.get('consumer_tax_tobacco') or prumerny_obcan_hodnoty.consumer_tax_tobacco)
    consumer_tax_alcohol = int(request.args.get('consumer_tax_alcohol') or prumerny_obcan_hodnoty.consumer_tax_alcohol)

    celkove_odvody = yearly_total_tax(rok, gross_income, rok == 2020, deti, social_insurance, vat_21, vat_food_mhd_medical_devices, vat_books_music_medicine_water_accomodations, capital_gains, gambling_tax, consumer_tax_car_fuel, consumer_tax_beer, consumer_tax_tobacco, consumer_tax_alcohol)
    print(celkove_odvody)
    procentualni_podil_prijmy = budget_ratio(fetch_rozpocet_na_rok(rok).total_income, celkove_odvody)
    procentualni_podil_vydaje = expenses_ratio(fetch_vydaje_na_rok(rok).total_expenses, celkove_odvody)
    procentualni_podil_investice_z_celkovych_odvodu = investitions_ratio(fetch_vydaje_na_rok(rok).total_expenses, fetch_vydaje_na_rok(rok).investment_purchases, fetch_vydaje_na_rok(rok).investment_transfers_bussines, fetch_vydaje_na_rok(rok).investment_state_funds, fetch_vydaje_na_rok(rok).investment_regions, fetch_vydaje_na_rok(rok).investment_contribution, fetch_vydaje_na_rok(rok).other_investment)
    korunovy_podil_investice = (procentualni_podil_investice_z_celkovych_odvodu / 100) * celkove_odvody
    procentualni_podil_investice = korunovy_podil_investice / (fetch_vydaje_na_rok(rok).investment_purchases + fetch_vydaje_na_rok(rok).investment_transfers_bussines + fetch_vydaje_na_rok(rok).investment_state_funds + fetch_vydaje_na_rok(rok).investment_regions + fetch_vydaje_na_rok(rok).investment_contribution + fetch_vydaje_na_rok(rok).other_investment) * 100

    return jsonify(celkove_odvody = celkove_odvody, procentualni_podil_prijmy = procentualni_podil_prijmy, procentualni_podil_vydaje = procentualni_podil_vydaje, procentualni_podil_investice_z_celkovych_odvodu = procentualni_podil_investice_z_celkovych_odvodu, korunovy_podil_investice = korunovy_podil_investice, procentualni_podil_investice = procentualni_podil_investice)
