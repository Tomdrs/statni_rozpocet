// fetch rozpocet
async function fetch_rozpocet(rok) {
    let req = await fetch("/rozpocet/" + rok);
    let rozpocet = await req.json();
    return rozpocet;
}

async function fetch_vydaje(rok) {
    let req = await fetch("/vydaje/" + rok);
    let vydaje = await req.json();
    return vydaje;
}

async function fetch_prumerny_obcan() {
    let req = await fetch("/prumerny_obcan");
    let prumerny_obcan = await req.json();
    return prumerny_obcan;
}

function filter_investment_array(arr, filtr) {
    if (filtr !== '')
        return arr.filter(entry => entry.start_year.toString().indexOf(filtr) >= 0 || entry.name.toLowerCase().indexOf(filtr.toLowerCase()) >= 0);
    else return arr;
}

async function fetch_investice(filtr, extra_investice) {
    let req = await fetch("/investice");
    let investice = await req.json();
    investice = investice.investice_json.map((x) => JSON.parse(x));
    investice = investice.sort((a, b) => a.start_year - b.start_year);
    investice = filter_investment_array(investice, filtr);

    return investice;
}

async function get_form_data() {
    let prumerny_obcan = await fetch_prumerny_obcan();
    let data = { deti: 0, ...prumerny_obcan};
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
    return data;
}

function get_income_data_placeholder(rok) {
    return {
        year: rok,
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

function vypocet_placeholders() {
    return {
        celkove_odvody: 0,
        procentualni_podil_investice_z_celkovych_odvodu: 0,
        korunovy_podil_investice: 0,
        procentualni_podil_investice: 0,
        spotrebni_dan_celkem: 0,
        podil_na_dph: 0,
        spotrebni_dan_paliva: 0,
        spotrebni_dan_tabak: 0,
        dan_z_prijmu: 0,
        soc_pojistne: 0,
        dan_hazard: 0,
        podil_na_vydajich: 0,
        podil_na_platech: 0,
        neinvesticni_nakupy: 0,
        neinvesticni_transfery_pod: 0,
        neinvesticni_transfery_fondum: 0,
        neinvesticni_transfery_soc_a_zdrav: 0,
        neinvesticni_transfery_rozpoctum: 0,
        neinvesticni_transfery_pris: 0,
        neinvesticni_transfery_nezisk: 0,
        podil_na_duchodech: 0,
        podpora_v_nezamestnanosti: 0,
        ostatni_socialni_davky: 0,
        statni_socialni_podpora: 0,
        stavebni_sporeni: 0,
        duchodove_pripojisteni: 0,
        ostatni_bezne_vydaje: 0,
        platby_eu: 0,
        investicni_nakupy: 0,
        investicni_transfery_pod: 0,
        investicni_transfery_fondum: 0,
        investicni_transfery_rozpoctum: 0,
        investicni_transfery_pris: 0,
        ostatni_investice: 0
    };
}

async function calculate_dane(rok, form_data) {
    let data = await fetch_vypocet(
        rok,
        form_data.gross_income,
        form_data.deti,
        form_data.social_insurance,
        form_data.vat_books_music_medicine_water_accomodations,
        form_data.vat_food_mhd_medical_devices,
        form_data.vat_21,
        form_data.capital_gains,
        form_data.gambling_tax,
        form_data.consumer_tax_car_fuel,
        form_data.consumer_tax_beer,
        form_data.consumer_tax_tobacco,
        form_data.consumer_tax_alcohol
    );
    console.log(data);
    return data;
}

async function fetch_vypocet(rok, gross_income, deti, social_insurance, vat_books_music_medicine_water_accomodations, vat_food_mhd_medical_devices, vat_21, capital_gains, gambling_tax, consumer_tax_car_fuel, consumer_tax_beer, consumer_tax_tobacco, consumer_tax_alcohol) {
    let query = "/vypocet/"+ rok +"?";

    if (typeof gross_income !== 'undefined' && gross_income !== '') query += 'gross_income=' + gross_income + '&';
    if (typeof deti !== 'undefined' && deti !== '') query += 'deti=' + deti + '&';
    if (typeof social_insurance !== 'undefined' && social_insurance !== '') query += 'social_insurance=' + social_insurance + '&';
    if (typeof vat_books_music_medicine_water_accomodations !== 'undefined' && vat_books_music_medicine_water_accomodations !== '') query += 'vat_books_music_medicine_water_accomodations=' + vat_books_music_medicine_water_accomodations + '&';
    if (typeof vat_food_mhd_medical_devices !== 'undefined' && vat_food_mhd_medical_devices !== '') query += 'vat_food_mhd_medical_devices=' + vat_food_mhd_medical_devices + '&';
    if (typeof vat_21 !== 'undefined' && vat_21 !== '') query += 'vat_21=' + vat_21 + '&';
    if (typeof capital_gains !== 'undefined' && capital_gains !== '') query += 'capital_gains=' + capital_gains + '&';
    if (typeof gambling_tax !== 'undefined' && gambling_tax !== '') query += 'gambling_tax=' + gambling_tax + '&';
    if (typeof consumer_tax_car_fuel !== 'undefined' && consumer_tax_car_fuel !== '') query += 'consumer_tax_car_fuel=' + consumer_tax_car_fuel + '&';
    if (typeof consumer_tax_beer !== 'undefined' && consumer_tax_beer !== '') query += 'consumer_tax_beer=' + consumer_tax_beer + '&';
    if (typeof consumer_tax_tobacco !== 'undefined' && consumer_tax_tobacco !== '') query += 'consumer_tax_tobacco=' + consumer_tax_tobacco + '&';
    if (typeof consumer_tax_alcohol !== 'undefined' && consumer_tax_alcohol !== '') query += 'consumer_tax_alcohol=' + consumer_tax_alcohol;

    let result = await fetch(query);
    if (result.status != 200)
        return "error";
    else
        return (await result.json());
}


function display_number(number, zero_if_undef = true, allow_negative = false) {
    if (number)
        return (allow_negative ? number : Math.max(number, 0)).toFixed(2);
    else
        return (zero_if_undef ? 0 : "");
}

function random_string() {
    return (Math.random() + 1).toString(36).substring(7);
}

async function pb_login(email, pass) {
    console.log("login");
    return {};
}
async function pb_signup(email, pass, pass_again) {
    console.log("signup");
    return {};
}
