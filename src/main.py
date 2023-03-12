from flask import Flask, render_template, jsonify, request
from pocketbase import PocketBase

from models import Budget, Expenses, State_levies_average, Investment
from tax_math import yearly_total_tax, expenses_ratio, investitions_ratio, budget_ratio, consumer_tax_fuel_function, consumer_tax_beer_function, consumer_tax_tobacco_function, consumer_tax_alcohol_function, yearly_vat_21, yearly_vat_15, yearly_vat_10, yearly_income_tax, yearly_kids_discount, yearly_social_insurance, yearly_gambling_tax, yearly_capital, salaries, noninvestment_purchases, noninvestment_transfers_to_bussines, noninvestment_state_funds, noninvestment_social_and_health, noninvestment_regions, noninvestment_contributions, noninvestment_non_profit
from tax_math import pensions, unemployment_help, other_social_help, state_social_help, building_savings, pension_insurance, other_usual_expenses, payments_to_eu, investment_purchases, investment_transfers_to_bussines, investment_state_funds, investment_regions
from tax_math import investment_contribution, other_capital_expenses

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

    gross_income = float(request.args.get('gross_income') or prumerny_obcan_hodnoty.gross_income)
    deti = float(request.args.get('deti') or 0)
    social_insurance = float(request.args.get('social_insurance') or prumerny_obcan_hodnoty.social_insurance)
    vat_books_music_medicine_water_accomodations = float(request.args.get('vat_books_music_medicine_water_accomodations') or prumerny_obcan_hodnoty.vat_books_music_medicine_water_accomodations)
    vat_food_mhd_medical_devices = float(request.args.get('vat_food_mhd_medical_devices') or prumerny_obcan_hodnoty.vat_food_mhd_medical_devices)
    vat_21 = float(request.args.get('vat_21') or prumerny_obcan_hodnoty.vat_21)
    capital_gains = float(request.args.get('capital_gains') or prumerny_obcan_hodnoty.capital_gains)
    gambling_tax = float(request.args.get('gambling_tax') or prumerny_obcan_hodnoty.gambling_tax)
    consumer_tax_car_fuel = float(request.args.get('consumer_tax_car_fuel') or prumerny_obcan_hodnoty.consumer_tax_car_fuel)
    consumer_tax_beer = float(request.args.get('consumer_tax_beer') or prumerny_obcan_hodnoty.consumer_tax_beer)
    consumer_tax_tobacco = float(request.args.get('consumer_tax_tobacco') or prumerny_obcan_hodnoty.consumer_tax_tobacco)
    consumer_tax_alcohol = float(request.args.get('consumer_tax_alcohol') or prumerny_obcan_hodnoty.consumer_tax_alcohol)

    celkove_odvody = yearly_total_tax(rok, gross_income, rok == 2020, deti, social_insurance, vat_21, vat_food_mhd_medical_devices, vat_books_music_medicine_water_accomodations, capital_gains, gambling_tax, consumer_tax_car_fuel, consumer_tax_beer, consumer_tax_tobacco, consumer_tax_alcohol)
    print(celkove_odvody)
    procentualni_podil_prijmy = budget_ratio(fetch_rozpocet_na_rok(rok).total_income, celkove_odvody)
    procentualni_podil_vydaje = expenses_ratio(fetch_vydaje_na_rok(rok).total_expenses, celkove_odvody)
    procentualni_podil_investice_z_celkovych_odvodu = investitions_ratio(fetch_vydaje_na_rok(rok).total_expenses, fetch_vydaje_na_rok(rok).investment_purchases, fetch_vydaje_na_rok(rok).investment_transfers_bussines, fetch_vydaje_na_rok(rok).investment_state_funds, fetch_vydaje_na_rok(rok).investment_regions, fetch_vydaje_na_rok(rok).investment_contribution, fetch_vydaje_na_rok(rok).other_investment)
    korunovy_podil_investice = (procentualni_podil_investice_z_celkovych_odvodu / 100) * celkove_odvody
    procentualni_podil_investice = korunovy_podil_investice / (fetch_vydaje_na_rok(rok).investment_purchases + fetch_vydaje_na_rok(rok).investment_transfers_bussines + fetch_vydaje_na_rok(rok).investment_state_funds + fetch_vydaje_na_rok(rok).investment_regions + fetch_vydaje_na_rok(rok).investment_contribution + fetch_vydaje_na_rok(rok).other_investment) * 100
    spotrebni_dan_celkem = consumer_tax_fuel_function(consumer_tax_car_fuel) + consumer_tax_beer_function(consumer_tax_beer) + consumer_tax_tobacco_function(consumer_tax_tobacco) + consumer_tax_alcohol_function(consumer_tax_alcohol)
    podil_na_dph = yearly_vat_21(vat_21) + yearly_vat_15(vat_food_mhd_medical_devices) + yearly_vat_10(vat_books_music_medicine_water_accomodations)
    spotrebni_dan_paliva = consumer_tax_fuel_function(consumer_tax_car_fuel)
    spotrebni_dan_tabak = consumer_tax_tobacco_function(consumer_tax_tobacco)
    dan_z_prijmu = yearly_income_tax(gross_income, rok == 2020) - yearly_kids_discount(rok, gross_income, deti) + yearly_capital(capital_gains)
    soc_pojistne = yearly_social_insurance(gross_income, social_insurance)
    dan_hazard = yearly_gambling_tax(gambling_tax)
    podil_na_vydajich = celkove_odvody
    podil_na_platech = salaries(fetch_vydaje_na_rok(rok).total_expenses, celkove_odvody, fetch_vydaje_na_rok(rok).salaries)
    neinvesticni_nakupy = noninvestment_purchases(fetch_vydaje_na_rok(rok).total_expenses, celkove_odvody, fetch_vydaje_na_rok(rok).noninvestment_purchases)
    neinvesticni_transfery_pod = noninvestment_transfers_to_bussines(fetch_vydaje_na_rok(rok).total_expenses, celkove_odvody, fetch_vydaje_na_rok(rok).noninvestment_bussines)
    neinvesticni_transfery_fondum = noninvestment_state_funds(fetch_vydaje_na_rok(rok).total_expenses, celkove_odvody, fetch_vydaje_na_rok(rok).noninvestment_state_funds)
    neinvesticni_transfery_soc_a_zdrav = noninvestment_social_and_health(fetch_vydaje_na_rok(rok).total_expenses, celkove_odvody, fetch_vydaje_na_rok(rok).noninvestment_soc_and_health_funds)
    neinvesticni_transery_rozpoctum = noninvestment_regions(fetch_vydaje_na_rok(rok).total_expenses, celkove_odvody, fetch_vydaje_na_rok(rok).noninvestment_regions)
    neinvesticni_transery_pris = noninvestment_contributions(fetch_vydaje_na_rok(rok).total_expenses, celkove_odvody, fetch_vydaje_na_rok(rok).noninvestment_contribution)
    neinvesticni_transery_nezisk = noninvestment_non_profit(fetch_vydaje_na_rok(rok).total_expenses, celkove_odvody, fetch_vydaje_na_rok(rok).noninvestment_non_profit)
    podil_na_duchodech = pensions(fetch_vydaje_na_rok(rok).total_expenses, celkove_odvody, fetch_vydaje_na_rok(rok).pensions)
    podpora_v_nezamestnanosti = unemployment_help(fetch_vydaje_na_rok(rok).total_expenses, celkove_odvody, fetch_vydaje_na_rok(rok).unemployment_help)
    ostatni_socialni_davky = other_social_help(fetch_vydaje_na_rok(rok).total_expenses, celkove_odvody, fetch_vydaje_na_rok(rok).other_social_help)
    statni_socialni_podpora = state_social_help(fetch_vydaje_na_rok(rok).total_expenses, celkove_odvody, fetch_vydaje_na_rok(rok).state_social_help)
    stavebni_sporeni = building_savings(fetch_vydaje_na_rok(rok).total_expenses, celkove_odvody, fetch_vydaje_na_rok(rok).building_savings)
    duchodove_pripojisteni = pension_insurance(fetch_vydaje_na_rok(rok).total_expenses, celkove_odvody, fetch_vydaje_na_rok(rok).pension_insurance_contribution)
    ostatni_bezne_vydaje = other_usual_expenses(fetch_vydaje_na_rok(rok).total_expenses, celkove_odvody, fetch_vydaje_na_rok(rok).other_usual_expenses)
    platby_eu = payments_to_eu(fetch_vydaje_na_rok(rok).total_expenses, celkove_odvody, fetch_vydaje_na_rok(rok).eu_payment)
    investicni_nakupy = investment_purchases(fetch_vydaje_na_rok(rok).total_expenses, celkove_odvody, fetch_vydaje_na_rok(rok).investment_purchases)
    investicni_transfery_pod = investment_transfers_to_bussines(fetch_vydaje_na_rok(rok).total_expenses, celkove_odvody, fetch_vydaje_na_rok(rok).investment_transfers_bussines)
    investicni_transfery_fondum = investment_state_funds(fetch_vydaje_na_rok(rok).total_expenses, celkove_odvody, fetch_vydaje_na_rok(rok).investment_state_funds)
    investicni_transery_rozpoctum = investment_regions(fetch_vydaje_na_rok(rok).total_expenses, celkove_odvody, fetch_vydaje_na_rok(rok).investment_regions)
    investicni_transery_pris = investment_contribution(fetch_vydaje_na_rok(rok).total_expenses, celkove_odvody, fetch_vydaje_na_rok(rok).investment_contribution)
    ostatni_investice = other_capital_expenses(fetch_vydaje_na_rok(rok).total_expenses, celkove_odvody, fetch_vydaje_na_rok(rok).other_investment)

    return jsonify(
        celkove_odvody = celkove_odvody,
        procentualni_podil_prijmy = procentualni_podil_prijmy,
        procentualni_podil_vydaje = procentualni_podil_vydaje,
        procentualni_podil_investice_z_celkovych_odvodu = procentualni_podil_investice_z_celkovych_odvodu,
        korunovy_podil_investice = korunovy_podil_investice,
        procentualni_podil_investice = procentualni_podil_investice,
        spotrebni_dan_celkem = spotrebni_dan_celkem,
        podil_na_dph = podil_na_dph,
        spotrebni_dan_paliva = spotrebni_dan_paliva,
        spotrebni_dan_tabak = spotrebni_dan_tabak,
        dan_z_prijmu = dan_z_prijmu,
        soc_pojistne = soc_pojistne,
        dan_hazard = dan_hazard,
        podil_na_vydajich = podil_na_vydajich,
        podil_na_platech = podil_na_platech,
        neinvesticni_nakupy = neinvesticni_nakupy,
        neinvesticni_transfery_pod = neinvesticni_transfery_pod,
        neinvesticni_transfery_fondum = neinvesticni_transfery_fondum,
        neinvesticni_transfery_soc_a_zdrav = neinvesticni_transfery_soc_a_zdrav,
        neinvesticni_transery_rozpoctum = neinvesticni_transery_rozpoctum,
        neinvesticni_transery_pris = neinvesticni_transery_pris,
        neinvesticni_transery_nezisk = neinvesticni_transery_nezisk,
        podil_na_duchodech = podil_na_duchodech,
        podpora_v_nezamestnanosti = podpora_v_nezamestnanosti,
        ostatni_socialni_davky = ostatni_socialni_davky,
        statni_socialni_podpora = statni_socialni_podpora,
        stavebni_sporeni = stavebni_sporeni,
        duchodove_pripojisteni = duchodove_pripojisteni,
        ostatni_bezne_vydaje = ostatni_bezne_vydaje,
        platby_eu = platby_eu,
        investicni_nakupy = investicni_nakupy,
        investicni_transfery_pod = investicni_transfery_pod,
        investicni_transfery_fondum = investicni_transfery_fondum,
        investicni_transery_rozpoctum = investicni_transery_rozpoctum,
        investicni_transery_pris = investicni_transery_pris,
        ostatni_investice = ostatni_investice
        
        )
