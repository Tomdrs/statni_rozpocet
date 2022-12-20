// fetch rozpocet
async function fetch_rozpocet(rok) {
    let req = await fetch("/rozpocet/" + rok);
    return await req.text()
}
