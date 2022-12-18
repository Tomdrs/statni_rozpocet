{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
    buildInputs = [
        pkgs.coreutils-full
        pkgs.python3Full
        pkgs.python310Packages.flask
        pkgs.python3.pkgs.virtualenv
        pkgs.pocketbase
    ];
    shellHook = ''
        source env/bin/activate
    '';
    FLASK_APP="src/main.py";
}
