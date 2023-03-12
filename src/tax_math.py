SUPERGROSS_MULTIPLIER = 1.338
income_tax_multiplier = 0.15
budgetary_determination = 0.6438

#daň z příjmu:
def yearly_income_tax(gross, is_supergross):
    if is_supergross == True:
        super_gross = gross * SUPERGROSS_MULTIPLIER
        return (income_tax_multiplier * super_gross - 2570) * 12 * budgetary_determination
    else:
        return (income_tax_multiplier * gross - 2570) * 12 * budgetary_determination

#sleva na poplatníka podle počtu dětí:
def yearly_kids_discount(rok, gross, kids):
        if rok == 2020 and gross >= 7300:
            if kids == 1:
                return 15204
            elif kids == 2:
                return 15204 + 22320
            elif kids > 2:
                return 60300
            else:
                return 0
        elif rok == 2021 and gross >= 7600:
            if kids == 1:
                return 15204
            elif kids == 2:
                return 15204 + 22320
            elif kids > 2:
                return 60300
            else:
                return 0
        elif rok == 2022 and gross >= 8100:
            if kids == 1:
                return 15204
            elif kids == 2:
                return 15204 + 22320
            elif kids > 2:
                return 15204 + 22320 + (kids - 2) * 27840
            else:
                return 0
        else:
            return 0


#výše platby na sociální zabezpečení:
def yearly_social_insurance(gross, social_insurance):
    if social_insurance == 0:
        return gross * 0.065 * 12 + gross * 0.248
    else:
        return social_insurance

#výše odvedené daně z přidané hodnoty základní sazby:
def yearly_vat_21(vat_21):
    return vat_21 * 0.21 * 12 * budgetary_determination

#výše odvedené daně z přidané hodnoty první snížené sazby:
def yearly_vat_15(vat_15):
    return vat_15 * 0.15 * 12 * budgetary_determination

#výše odvedené daně z přidané hodnoty druhé snížené sazby:
def yearly_vat_10(vat_10):
    return vat_10 * 0.10 * 12 * budgetary_determination

#výše odvedené daně z kapitálových příjmů:
def yearly_capital(capital_gains):
    if capital_gains >= 8333:
        return capital_gains * 0.15 * 12
    else:
        return 0

#výše odvedené daně z neúspěšného hazardu:
def yearly_gambling_tax(gamble):
    return gamble * 0.23 * 12 * 0.7

#výše odvedené spotřební daně z pohonných hmot (průměrná cena 38 kč/l):
def consumer_tax_fuel_function(consumer_fuel):
    return (consumer_fuel / 38) * 11.5 * 12

#výše odvedené spotřební daně z piva (objem litrů násobený daní):
def consumer_tax_beer_function(consumer_beer):
    return consumer_beer * 0.32 * 12

#výše odvedené spotřební daně z tabáku (krabička cigaret - 20 kusů - násobené daní):
def consumer_tax_tobacco_function(consumer_tobacco):
    return consumer_tobacco * 29.2 * 12

#výše odvedené spotřební daně z pohonných hmot (objel litrů ethanulu násobený daní):
def consumer_tax_alcohol_function(consumer_alcohol):
    return consumer_alcohol * 285 * 12

#celková částka korun odvedených skrze daně do státního rozpočtu
def yearly_total_tax(rok, gross, is_supergross, kids, social_insurance, vat_21, vat_15, vat_10, capital_gains, gamble, consumer_fuel, consumer_beer,consumer_tobacco, consumer_alcohol):
    return yearly_income_tax(gross, is_supergross) \
        - yearly_kids_discount(rok, gross, kids) \
        + yearly_social_insurance(gross, social_insurance) \
        + yearly_vat_21(vat_21) \
        + yearly_vat_15(vat_15) \
        + yearly_vat_10(vat_10) \
        + yearly_capital(capital_gains) \
        + yearly_gambling_tax(gamble) \
        + consumer_tax_fuel_function(consumer_fuel) \
        + consumer_tax_beer_function(consumer_beer) \
        + consumer_tax_tobacco_function(consumer_tobacco) \
        + consumer_tax_alcohol_function(consumer_alcohol)

#procento podílu odvedených daní na státním rozpočtu
def expenses_ratio(total_expenses, yearly_total_tax):
    return (yearly_total_tax / total_expenses) * 100

def budget_ratio(total_income, yearly_total_tax):
    return (yearly_total_tax / total_income) * 100

def investitions_ratio(total_expenses, inv_purchases, inv_tansfers, inv_state_funds, inv_regions, inv_contribution, oth_investments):
    return (inv_purchases + inv_tansfers + inv_state_funds + inv_regions + inv_contribution + oth_investments) / total_expenses * 100


#částka a procento přispěné z odvedených daní na platy
def salaries(total_expenses, yearly_total_tax, salarie):
    return (salarie/total_expenses) * yearly_total_tax

def salariesp(total_expenses, salarie):
    return (salarie/total_expenses) * 100

#částka a procento přispěné z odvedených daní na neinvestční nákupy
def noninvestment_purchases(total_expenses, yearly_total_tax, non_purchases):
    return (non_purchases/total_expenses) * yearly_total_tax

def noninvestment_purchasesp(total_expenses, non_purchases):
    return (non_purchases/total_expenses) * 100

#částka a procento přispěné z odvedených daní na neinvestiční transfery podnikatelům
def noninvestment_transfers_to_bussines(total_expenses, yearly_total_tax, non_transfers):
    return (non_transfers/total_expenses) * yearly_total_tax

def noninvestment_transfers_to_bussinesp(total_expenses, non_transfers):
    return (non_transfers/total_expenses) * 100

#částka a procento přispěné z odvedených daní na neinvestiční transfery neziskovým organizacím
def noninvestment_non_profit(total_expenses, yearly_total_tax, non_non_profit):
    return (non_non_profit/total_expenses) * yearly_total_tax

def noninvestment_non_profitp(total_expenses, non_non_profit):
    return (non_non_profit/total_expenses) * 100

#částka a procento přispěné z odvedených daní na neinvestiční transfery státním fondům
def noninvestment_state_funds(total_expenses, yearly_total_tax, non_state):
    return (non_state/total_expenses) * yearly_total_tax

def noninvestment_state_fundsp(total_expenses, non_state):
    return (non_state/total_expenses) * 100

#částka a procento přispěné z odvedených daní na neinvestiční transfery fondům sociálního a zdravotního zabezpečení
def noninvestment_social_and_health(total_expenses, yearly_total_tax, non_social):
    return (non_social/total_expenses) * yearly_total_tax

def noninvestment_social_and_healthp(total_expenses, non_social):
    return (non_social/total_expenses) * 100

#částka a procento přispěné z odvedených daní na neinvestiční transfery rozpočtům územní úrovně
def noninvestment_regions(total_expenses, yearly_total_tax, non_regions):
    return (non_regions/total_expenses) * yearly_total_tax

def noninvestment_regionsp(total_expenses, non_regions):
    return (non_regions/total_expenses) * 100

#částka a procento přispěné z odvedených daní na neinvestiční transfery příspěvkovým organizacím
def noninvestment_contributions(total_expenses, yearly_total_tax, non_contributions):
    return (non_contributions/total_expenses) * yearly_total_tax

def noninvestment_contributionsp(total_expenses, non_contributions):
    return (non_contributions/total_expenses) * 100

#částka a procento přispěné z odvedených danína důchody
def pensions(total_expenses, yearly_total_tax, pension):
    return (pension/total_expenses) * yearly_total_tax

def pensionsp(total_expenses, pension):
    return (pension/total_expenses) * 100

#částka a procento přispěné z odvedených daní na podporu v nezaměstnanosti 
def unemployment_help(total_expenses, yearly_total_tax, unemployment):
    return (unemployment/total_expenses) * yearly_total_tax

def unemployment_helpp(total_expenses, unemployment):
    return (unemployment/total_expenses) * 100

#částka a procento přispěné z odvedených daní na ostatní sociální dávky
def other_social_help(total_expenses, yearly_total_tax, social_help):
    return (social_help/total_expenses) * yearly_total_tax

def other_social_helpp(total_expenses, social_help):
    return (social_help/total_expenses) * 100

#částka a procento přispěné z odvedených danína státní sociální dávky
def state_social_help(total_expenses, yearly_total_tax, state_help):
    return (state_help/total_expenses) * yearly_total_tax

def state_social_helpp(total_expenses, state_help):
    return (state_help/total_expenses) * 100

#částka a procento přispěné z odvedených danína stavební spoření
def building_savings(total_expenses, yearly_total_tax, buildings):
    return (buildings/total_expenses) * yearly_total_tax

def building_savingsp(total_expenses, buildings):
    return (buildings/total_expenses) * 100

#částka a procento přispěné z odvedených daní na důchodové připojištění
def pension_insurance(total_expenses, yearly_total_tax, pension_ins):
    return (pension_ins/total_expenses) * yearly_total_tax

def pension_insurancep(total_expenses, pension_ins):
    return (pension_ins/total_expenses) * 100

#částka a procento přispěné z odvedených daní na platby Evropské unii
def payments_to_eu(total_expenses, yearly_total_tax, eu_pay):
    return (eu_pay/total_expenses) * yearly_total_tax

def payments_to_eup(total_expenses, eu_pay):
    return (eu_pay/total_expenses) * 100

#částka a procento přispěné z odvedených daní na ostatní běžné výdaje
def other_usual_expenses(total_expenses, yearly_total_tax, other_expenses):
    return (other_expenses/total_expenses) * yearly_total_tax

def other_usual_expensesp(total_expenses, other_expenses):
    return (other_expenses/total_expenses) * 100

#částka a procento přispěné z odvedených daní na investiční nákupy
def investment_purchases(total_expenses, yearly_total_tax, inv_purchases):
    return (inv_purchases/total_expenses) * yearly_total_tax

def investment_purchasesp(total_expenses, inv_purchases):
    return (inv_purchases/total_expenses) * 100

#částka a procento přispěné z odvedených daní na investiční transfery podnikatelům
def investment_transfers_to_bussines(total_expenses, yearly_total_tax, inv_tansfers):
    return (inv_tansfers/total_expenses) * yearly_total_tax

def investment_transfers_to_bussinesp(total_expenses, inv_tansfers):
    return (inv_tansfers/total_expenses) * 100

#částka a procento přispěné z odvedených daní na investiční transfery státním fondům
def investment_state_funds(total_expenses, yearly_total_tax, inv_state_funds):
    return (inv_state_funds/total_expenses) * yearly_total_tax

def investment_state_fundsp(total_expenses, inv_state_funds):
    return (inv_state_funds/total_expenses) * 100

#částka a procento přispěné z odvedených daní na investiční transfery rozpočtům územní úrovně
def investment_regions(total_expenses, yearly_total_tax, inv_regions):
    return (inv_regions/total_expenses) * yearly_total_tax

def investment_regionsp(total_expenses, inv_regions):
    return (inv_regions/total_expenses) * 100

#částka a procento přispěné z odvedených daní na investiční transfery příspěvkovým organizacím
def investment_contribution(total_expenses, yearly_total_tax, inv_contribution):
    return (inv_contribution/total_expenses) * yearly_total_tax

def investment_contributionp(total_expenses, inv_contribution):
    return (inv_contribution/total_expenses) * 100

#částka a procento přispěné z odvedených daní na ostatní kapitálové výdaje
def other_capital_expenses(total_expenses, yearly_total_tax, other_capital):
    return (other_capital/total_expenses) * yearly_total_tax

def other_capital_expensesp(total_expenses, other_capital):
    return (other_capital/total_expenses) * 100

#částka a procento přispěné z odvedených daní na jiné investice
def other_investment(total_expenses, yearly_total_tax, oth_investments):
    return (oth_investments/total_expenses) * yearly_total_tax

def other_investmentp(total_expenses, oth_investments):
    return (oth_investments/total_expenses) * 100