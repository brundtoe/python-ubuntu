# Installation og konfiguration af Ubuntu

Projektet indeholder scripts til brug ved installation af software på Debina og archLinux distributioner.

Repositoriet clones fra::

    https://github.com/brundtoe/python-demo.git

## Forbered installationen

Der oprettes i mappen **config** filen **.env.develop**::

    cd config
    cp env.template .env.develop

Opdater med de relevante passwords


Filen **config/config.ini** her opdateres alle elementer i afsnittene 

    - Common (her findes parametre som anvendes i de efterfølgende afsnit)
    - ekstra.programs
    - manjaro-programs

## Python requirements

Følgende skal være installeret::

    python3-pip
    python3-setuptools
    python3-venv
    cd python-demo
    pip3 install -r requirements-global.txt
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements-local.txt
    python3 setup.py develop

## Installationen

På Ubuntu anvendes::

    cd python-demo
    sudo ./install_ubuntu.py

På Manjaro/Archlinux anvendes::

    cd python-demo
    sudo ./install_manjaro.py

En række programmer, som kun anvendes på instanser med en desktop GUI:

    ./install_desktop.py

## Programmer, der kan installeres

Programmerne fremgår af menuerne som vises i installationsscriptene.

