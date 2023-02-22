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
        health_insurance: '',
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