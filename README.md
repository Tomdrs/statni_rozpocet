# statni_rozpocet
To get requirements and run the project, install [Nix](https://nixos.org/).

Check shellhook and variables in `shell.nix`:

```nix
    shellHook = ''
        virtualenv -p python3 env
        source env/bin/activate
        pip install -r requirements.txt
    '';
    FLASK_APP="src/main.py";
    POCKETBASE_URL="https://pocketbase.gjk.cat/";
```

Use local pocketbase if you don't have access to **pocketbase.gjk.cat**.

```sh
# in different terminal
pocketbase serve
```

Import schema into pocketbase via **Settings -> Import collections** (use `pb_schema.json`).

To run app:

```sh
nix-shell
flask run
```

# Technologies:
- Backend:
    - Python
    - [Flask](https://flask.palletsprojects.com/en/2.2.x/) - lightweight web framework
    - [PocketBase](https://pocketbase.io/) - open-source backend -> database and user management/authentication
- Frontend:
    - JS in markup with Alpine
    - CSS
    - [AlpineJS](https://alpinejs.dev) - Javascript framework to avoid NodeJS and writing Javascript

# Zdroje
- <https://www.mfcr.cz/cs/o-ministerstvu/vzdelavani/rozpocet-v-kostce/statni-rozpocet-v-kostce-2022-47759>
- <https://www.finance.cz/533787-dan-z-prijmu-a-prumerna-mzda/>
- <https://learnpython.com/blog/how-to-use-virtualenv-python/>
- <https://flexboxsheet.com/>
- <https://grid.layoutit.com/>
- <https://coryrylan.com/blog/how-to-center-in-css-with-flexbox>
- <https://stackoverflow.com/questions/73164546/error-file-nixpkgs-was-not-found-in-the-nix-search-path-add-it-using-nix-pa>
- <https://stackoverflow.com/questions/12433604/how-can-i-find-matching-values-in-two-arrays>
- <https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask>
- <https://flask.palletsprojects.com/en/2.2.x/>
- <https://flask.palletsprojects.com/en/2.2.x/quickstart/#routing>
- <https://pocketbase.io/>
- <https://github.com/pocketbase/js-sdk>
- <https://en.wikipedia.org/wiki/Representational_state_transfer>
- <https://unix.stackexchange.com/questions/519110/how-to-install-python-pip-on-nixos>
- <https://www.codesuji.com/2020/10/25/Nix-For-Development/>
- <https://pypi.org/project/pocketbase/>
- <https://www.youtube.com/watch?v=r5iWCtfltso>
- <https://www.youtube.com/watch?v=M3fY0E60cM0>
- <https://www.markdownguide.org/cheat-sheet>
- <https://alpinejs.dev/>
- <https://picocss.com/>
- <https://www.czso.cz/csu/czso/spotrebni-vydaje-domacnosti-2021>
- <https://www.financnisprava.cz/assets/cs/prilohy/d-kraje-a-obce/Schema_rozpoctoveho_urceni_dani_2022.pdf>
- <https://money.cz/novinky-a-tipy/mzdy-a-personalistika/konec-superhrube-mzdy-co-to-udela-s-vyplatou-zamestnancu/>
- <https://www.czso.cz/csu/czso/cri/prumerne-mzdy-3-ctvrtleti-2022>
- <https://www.podnikatel.cz/zakony/zakon-c-235-2004-sb-o-dani-z-pridane-hodnoty/uplne/#prilohy>
- <https://cs.wikipedia.org/wiki/Spot%C5%99ebn%C3%AD_da%C5%88>
- <https://www.businessinfo.cz/navody/provozovani-hazardnich-her-ppbi/3/>
- <https://www.vlada.cz/assets/media-centrum/aktualne/Narodni-investicni-plan-CR-2020_2050.pdf>
- <https://medium.com/@Mikepicker/build-a-multi-user-todo-list-app-with-pocketbase-in-a-single-html-file-8734bfb882fd>
- <https://www.kurzy.cz/mzda/socialni-pojisteni/>
- <https://www.finance.cz/503335-deti-a-dane/?_fid=m8yg#survey-place>
- <https://vimjakna.cz/dane/zakladni-danova-sleva/>
- <https://www.mpsv.cz/socialni-pojisteni>
- <https://flask.palletsprojects.com/en/2.2.x/tutorial/deploy/>
- <https://flask.palletsprojects.com/en/2.2.x/deploying/>
- <https://zpravy.aktualne.cz/ekonomika/spotreba-piva-loni-klesla-na-258-piv-na-obyvatele-snizila-se/r~5e67f25cc15411ecb13cac1f6b220ee8/>
- <https://www.czso.cz/csu/czso/graf-spotreba-cigaret-na-1-obyvatele-v-ceske-republice>
- <https://www.vlada.cz/cz/ppov/protidrogova-politika/media/alkohol-_-dobry-sluha-nebo-zly-pan--prvni-vladni-zprava-o-alkoholu-v-ceske-republice--195338/>
- <https://www.idnes.cz/ekonomika/domaci/hazard-zprava-protidrogovy-odbor-vedralova-automaty.A200721_123720_eko-doprava_fih>
- Budget spreadsheets in resources/

