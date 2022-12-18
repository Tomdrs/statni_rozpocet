{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
    buildInputs = [
        pkgs.coreutils-full
        pkgs.python3Full
        pkgs.python310Packages.flask
        pkgs.pocketbase
    ];
}