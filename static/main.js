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