# Installation og konfiguration af Ubuntu

Enkeltstående scripts til brug ved konfiguration af et Ubuntu eller Kubuntu image.

Detaljer fremgår af dokumentationen i mappen docs.

## Forbered installationen

- Der oprettes i mappen **infile** filen **.env.develop** med password til**wdmycloud**
- filen **infile/config.ini** her opdateres alle elementer i afsnittene 

    - Common (her findes parametre som anvendes i de efterfølgende afsnit)
    - ekstra.programs

## ParseConfig

Der anvendes ExtendedInterpolation i moduler/fetch_config

# Udfør installationen

    cd /home/{user}/sourcecode/
    git clone git@github.com:brundtoe/python-ubuntu.git
    cd /python-ubuntu
    sudo apt install -y python3-pip
    sudo pip install -r requirements.txt

requirements.txt indeholder pt. 

- requests og 
- jinja2
- Sphinx
    
Herefter kan følgende scripts udføres  

**Med root access**

* 01_prepare_install.py
* 02_install_requirements
* 03_install_repositories
* 04_install_extra

- vbox_ext_pack.py 
- groups.py


**Uden root access**

- install_jetbrains.py
- install_vagrant.py
- install_packer.py
- install_postman.py
- install_freefilesync.py
- install_nosqlbooster.py
- desktopfiles.py /FreeFileSync, NoSQLBooster og Postman) 

**med root efter ovenstående**
- chown.py (ændrer rettigheder rekursivt for et directory)
