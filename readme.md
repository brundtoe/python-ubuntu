# Installation og konfiguration af ubuntu

Enkeltstående scripts til brug ved konfiguration af et Ubuntu eller Kubuntu image.

Efterfølgende skal de laves som en helhed

## Forbered installationen

- Der oprettes i mappen infile filen **.env.develop** med password til** wdmycloud**
- filen infile/config.ini her opdateres alle elementer i afsnittene 

    - Common
    - ekstra.programs

## ParseConfig

Der anvendes ExtendedInterpolation i moduler/fetch_config

# Udfør installationen

    sudo apt install -y python3-pip
    sudo pip3 install request
    sudo pip2 install jinja2
    cd directory med instalationsscriptet
    sudo ./install_kubuntu.py
    
Herefter kan følgende installeres  

**Med root access**

- vbox_ext_pack.py 
- groups.py


**Uden root access**

- install_jetbrains.py
- install_vagrant.py
- install_packer.py
- install_postman.py
- install_freefilesync.py
- install_nosqlbooster.py

- desktopfiles.py for FreeFileSync og NoSQLBooster

**med root efter ovenstående**
- chown.py (ændrer rettigheder rekursivt for et directory)
