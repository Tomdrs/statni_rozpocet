// fetch rozpocet
async function fetch_rozpocet(rok) {
    let req = await fetch("/rozpocet/" + rok);
    let rozpocet = await req.json();
    console.log(rozpocet);
    return rozpocet;
}

async function fetch_vydaje(rok) {
    let req = await fetch("/vydaje/" + rok);
    let vydaje = await req.json();
    console.log(vydaje);
    return vydaje;
}

async function fetch_prumerny_obcan() {
    let req = await fetch("/prumerny_obcan");
    let prumerny_obcan = await req.json();
    console.log(prumerny_obcan);
    return prumerny_obcan;
}

async function fetch_investice() {
    let req = await fetch("/investice");
    let investice = await req.json();
    investice = investice.investice_json.map((x) => JSON.parse(x));
    console.log(investice);
    return investice;
}

async function get_form_data() {
    let prumerny_obcan = await fetch_prumerny_obcan();
    let data = { deti: 0, ...prumerny_obcan};
    console.log(data);
    return data;
}

function get_form_data_placeholder() {
    return {
        deti: '',
        gross_income: '',
        social_insurance: '',
        vat_books_music_medicine_water_accomodations: '',
        vat_food_mhd_medical_devices: '',
        vat_21: '',
        capital_gains: '',
        gambling_tax: '',
        consumer_tax_car_fuel: '',
        consumer_tax_beer: '',
        consumer_tax_tobacco: '',
        consumer_tax_alcohol: ''
    };
}

async function get_income_data(rok) {
    let data = await fetch_rozpocet(rok);
    console.log(data);
    return data;
}

function get_income_data_placeholder() {
    return {
        year: '',
        total_income: '',
        total_expense: '',
        vat: '',
        consumer_taxes: '',
        income_tax_individual: '',
        income_tax_company: '',
        mandatory_social_insurance: '',
        other_tax: '',
        other_nontax_income: '',
        consumer_tax_oils: '',
        consumer_tax_tobacco: '',
        consumer_tax_solar_energy: '',
        trash_fees: '',
        gambling_tax: '',
        income_from_eu: '',
        income_connected_with_eu: '',
    };
}

async function get_expense_data(rok) {
    let data = await fetch_vydaje(rok);
    console.log(data);
    return data;
}

function get_expense_data_placeholder() {
    return {
        year: '',
        total_expenses: '',
        salaries: '',
        noninvestment_purchases: '',
        noninvestment_bussines: '',
        noninvestment_non_profit: '',
        noninvestment_state_funds: '',
        noninvestment_soc_and_health_funds: '',
        noninvestment_regions: '',
        noninvestment_contribution: '',
        pensions: '',
        unemployment_help: '',
        other_social_help: '',
        state_social_help: '',
        building_savings: '',
        pension_insurance_contribution: '',
        eu_payment: '',
        other_usual_expenses: '',
        investment_purchases: '',
        investment_transfers_bussines: '',
        investment_state_funds: '',
        investment_regions: '',
        investment_contribution: '',
        other_investment: '',
    };
}

async function fetch_vypocet(rok, gross_income, deti, social_insurance, vat_books_music_medicine_water_accomodations, vat_food_mhd_medical_devices, vat_21, capital_gains, gambling_tax, consumer_tax_car_fuel, consumer_tax_beer, consumer_tax_tobacco, consumer_tax_alcohol) {
    let query = "/vypocet/"+ rok +"?";
    if (typeof gross_income !== 'undefined') query += 'gross_income=' + gross_income + '&';
    if (typeof deti !== 'undefined') query += 'deti=' + deti + '&';
    if (typeof social_insurance !== 'undefined') query += 'social_insurance=' + social_insurance + '&';
    if (typeof vat_books_music_medicine_water_accomodations !== 'undefined') query += 'vat_books_music_medicine_water_accomodations=' + vat_books_music_medicine_water_accomodations + '&';
    if (typeof vat_food_mhd_medical_devices !== 'undefined') query += 'vat_food_mhd_medical_devices=' + vat_food_mhd_medical_devices + '&';
    if (typeof vat21 !== 'undefined') query += 'vat_21=' + vat_21 + '&';
    if (typeof capital_gains !== 'undefined') query += 'capital_gains=' + capital_gains + '&';
    if (typeof gambling_tax !== 'undefined') query += 'gambling_tax=' + gambling_tax + '&';
    if (typeof consumer_tax_car_fuel !== 'undefined') query += 'consumer_tax_car_fuel=' + consumer_tax_car_fuel + '&';
    if (typeof consumer_tax_beer !== 'undefined') query += 'consumer_tax_beer=' + consumer_tax_beer + '&';
    if (typeof consumer_tax_tobacco !== 'undefined') query += 'consumer_tax_tobacco=' + consumer_tax_tobacco + '&';
    if (typeof consumer_tax_alcohol !== 'undefined') query += 'consumer_tax_alcohol=' + consumer_tax_alcohol;

    let result = await fetch(query);
}