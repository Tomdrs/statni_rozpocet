{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell rec {
  POCKETBASE_URL = "https://pocketbase.gjk.cat/";
  FLASK_APP = "src/main.py";

  buildInputs = [
    pkgs.coreutils-full
    pkgs.python3Full
    #pkgs.python310Packages.flask
    pkgs.python3.pkgs.virtualenv
    pkgs.python310Packages.waitress
    pkgs.pocketbase
  ];
  shellHook = ''
    virtualenv -p python3 env
    source env/bin/activate
    pip install -r requirements.txt
    echo 'let POCKETBASE_URL = "${POCKETBASE_URL}";' > static/config.js
  '';
}
