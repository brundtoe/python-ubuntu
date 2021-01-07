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

    
## software requirements

Et af de tre scripts:

- before_archlinux.sh
- before_manjaro.sh
- before_ubuntu.sh

udføres for at installere og konfigurere forudsætningerne for installationen af softwarepakker med Python

Det virtuelle environment opbygges:

```
sudo pip install -r requirements-global.txt        
virtualenv venv
source venv/bin/activate
pip install -r requirements-local.txt
python setup.py develop
```

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

