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
- <https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask>
- <https://flask.palletsprojects.com/en/2.2.x/>
- <https://flask.palletsprojects.com/en/2.2.x/quickstart/#routing>
- <https://pocketbase.io/>
- <https://en.wikipedia.org/wiki/Representational_state_transfer>
- <https://unix.stackexchange.com/questions/519110/how-to-install-python-pip-on-nixos>
- <https://www.codesuji.com/2020/10/25/Nix-For-Development/>
- <https://pypi.org/project/pocketbase/>
- <https://www.youtube.com/watch?v=r5iWCtfltso>
- <https://www.youtube.com/watch?v=M3fY0E60cM0>
- <https://www.markdownguide.org/cheat-sheet>
- <https://alpinejs.dev/>
- Budget spreadsheets in resources/

