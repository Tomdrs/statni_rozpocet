from flask import jsonify
import json

class Budget():
    def __init__(self, record):
        print(record)
        self.year = record.year
        self.total_income = record.total_income
        self.total_expense = record.total_expense
        self.vat = record.vat
        self.consumer_taxes = record.consumer_taxes
        self.income_tax_individual = record.income_tax_individual
        self.income_tax_company = record.income_tax_company
        self.mandatory_social_insurance = record.mandatory_social_insurance
        self.other_tax = record.other_tax
        self.other_nontax_income = record.other_nontax_income
        self.consumer_tax_oils = record.consumer_tax_oils
        self.consumer_tax_tobacco = record.consumer_tax_tobacco
        self.consumer_tax_solar_energy = record.consumer_tax_solar_energy
        self.trash_fees = record.trash_fees
        self.gambling_tax = record.gambling_tax
        self.income_from_eu = record.income_from_eu
        self.income_connected_with_eu = record.income_connected_with_eu
        print(dir(self))
        print(self.total_income)
    
    def to_json(self):
        return jsonify(
            year = self.year,
            total_income = self.total_income,
            total_expense = self.total_expense,
            vat = self.vat,
            consumer_taxes = self.consumer_taxes,
            income_tax_individual = self.income_tax_individual,
            income_tax_company = self.income_tax_company,
            mandatory_social_insurance = self.mandatory_social_insurance,
            other_tax = self.other_tax,
            other_nontax_income = self.other_nontax_income,
            consumer_tax_oils = self.consumer_tax_oils,
            consumer_tax_tobacco = self.consumer_tax_tobacco,
            consumer_tax_solar_energy = self.consumer_tax_solar_energy,
            trash_fees = self.trash_fees,
            gambling_tax = self.gambling_tax,
            income_from_eu = self.income_from_eu,
            income_connected_with_eu = self.income_connected_with_eu,
        )
    
class Expenses():
    def __init__(self, record):
        self.year = record.year
        self.total_expenses = record.total_expenses
        self.salaries = record.salaries
        self.noninvestment_purchases = record.noninvestment_purchases
        self.noninvestment_bussines = record.noninvestment_bussines
        self.noninvestment_non_profit = record.noninvestment_non_profit
        self.noninvestment_state_funds = record.noninvestment_state_funds
        self.noninvestment_soc_and_health_funds = record.noninvestment_soc_and_health_funds
        self.noninvestment_regions = record.noninvestment_regions
        self.noninvestment_contribution = record.noninvestment_contribution
        self.pensions = record.pensions
        self.unemployment_help = record.unemployment_help
        self.other_social_help = record.other_social_help
        self.state_social_help = record.state_social_help
        self.building_savings = record.building_savings
        self.pension_insurance_contribution = record.pension_insurance_contribution
        self.eu_payment = record.eu_payment
        self.other_usual_expenses = record.other_usual_expenses
        self.investment_purchases = record.investment_purchases
        self.investment_transfers_bussines = record.investment_transfers_bussines
        self.investment_state_funds = record.investment_state_funds
        self.investment_regions = record.investment_regions
        self.investment_contribution = record.investment_contribution
        self.other_invetment = record.other_invetment

    def to_json(self):
        return jsonify(
            year = self.year,
            total_expenses = self.total_expenses,
            salaries = self.salaries,
            noninvestment_purchases = self.noninvestment_purchases,
            noninvestment_bussines = self.noninvestment_bussines,
            noninvestment_non_profit = self.noninvestment_non_profit,
            noninvestment_state_funds = self.noninvestment_state_funds,
            noninvestment_soc_and_health_funds = self.noninvestment_soc_and_health_funds,
            noninvestment_regions = self.noninvestment_regions,
            noninvestment_contribution = self.noninvestment_contribution,
            pensions = self.pensions,
            unemployment_help = self.unemployment_help,
            other_social_help = self.other_social_help,
            state_social_help = self.state_social_help,
            building_savings = self.building_savings,
            pension_insurance_contribution = self.pension_insurance_contribution,
            eu_payment = self.eu_payment,
            other_usual_expenses = self.other_usual_expenses,
            investment_purchases = self.investment_purchases,
            investment_transfers_bussines = self.investment_transfers_bussines,
            investment_state_funds = self.investment_state_funds,
            investment_regions = self.investment_regions,
            investment_contribution = self.investment_contribution,
            other_invetment = self.other_invetment,
        )

class State_levies_average():
    def __init__(self, record):
        self.year = record.year
        self.gross_income = record.gross_income
        self.supergross = record.supergross
        self.supergross_multiplier = record.supergross_multiplier
        self.vat_21 = record.vat_21
        self.social_insurance = record.social_insurance
        self.health_insurance = record.health_insurance
        self.capital_gains = record.capital_gains
        self.gambling_tax = record.gambling_tax
        self.consumer_tax_car_fuel = record.consumer_tax_car_fuel
        self.vat_food_mhd_medical_devices = record.vat_food_mhd_medical_devices
        self.vat_books_music_medicine_water_accomodations = record.vat_books_music_medicine_water_accomodations
        self.consumer_tax_beer = record.consumer_tax_beer
        self.consumer_tax_tobacco = record.consumer_tax_tobacco
        self.consumer_tax_alcohol = record.consumer_tax_alcohol
    
    def to_json(self):
        return jsonify(
            year = self.year,
            gross_income = self.gross_income,
            supergross = self.supergross,
            supergross_multiplier = self.supergross_multiplier,
            vat_21 = self.vat_21,
            social_insurance = self.social_insurance,
            health_insurance = self.health_insurance,
            capital_gains = self.capital_gains,
            gambling_tax = self.gambling_tax,
            consumer_tax_car_fuel = self.consumer_tax_car_fuel,
            vat_food_mhd_medical_devices = self.vat_food_mhd_medical_devices,
            vat_books_music_medicine_water_accomodations = self.vat_books_music_medicine_water_accomodations,
            consumer_tax_beer = self.consumer_tax_beer,
            consumer_tax_tobacco = self.consumer_tax_tobacco,
            consumer_tax_alcohol = self.consumer_tax_alcohol,
        )

class Investment():
    def __init__(self, record):
        self.start_year = record.start_year
        self.name = record.name
        self.cost = record.cost
        
    def to_json(self):
        return json.dumps({
            'start_year': self.start_year,
            'name': self.name,
            'cost': self.cost,
        })