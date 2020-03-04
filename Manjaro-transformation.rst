.. index: Manjaro
    :pair: Manjaro; Python

==========================
Transformation til Manjaro
==========================

Manjaro anvendes i virtuelle maskiner (VMWare og VirtualBox) men ej på host

vmware er ikke supporteret på Manjaro

På Manjaro virtuelle maskiner anvendes kun docker ej virtualbox med vagrant. 

Alternativet er at anvende den virtuelle maskine med Manajro som host.

installation af sw foretages med Pacman

- et programs dependencies findes i appen der anvendes til program adminsitratiopn og på archlinux.org/packages  

hvad svarer til apt install -y

pacman -S --noconfirm gcc installation uden confirmation anvendes i scripts


pacman -Syu # svarer til apt update && apt upgrade

pacman Si <packagename> viser detaljeret info om en package

    hvis pacman Si returnerer 1 så findes pakken ikke

pacman -Qe [packagename] lister alle de explicit installerede packages

pacman -S packagename installation

hvis en pakke ikke er installeret returnerer pacman -Qe statuskode 1

.. todo oplysningerne kan let filtreres med grep eller awk 

- pamac manager eller pamac CLI anvendes ved installation af AUR packages

- pamac -h viser optionerne


Installation via script
=======================

Se Se filerne bash programs.sh og php.sh for hvilke programmer, der skal installeres

- MongoDB findes grundet licens issues ikke i repository
    - https://stackoverflow.com/questions/59455725/install-mongodb-on-manjaro

Følgende Findes i AUR alternativ download

- FreeFileSync
- jetbrains toolbox
- postman
- nosqlbooster
- virtualbox extension Pack 
- (se vc code på Komplett for installation af guest additions)
- mysql-server er blot mysql (mariadb findes i repo extra)
- openresty
- hplip findes på extra i en minimal version

Hvad anvendes - hvis nødvendigt - i stedet for nedenstående

- g++
- build-essential
- gdebi (Ikke relevant da det er debian pakke værktøj=)
- libsqlite-dev
- libmysqlclient-dev=
- apt-transport-http (er det til nodejs download som er overflødig)
- software-properties-common


TODO Ændringer i Python scripts
===============================

01-prepare
    - apt-update.py vil ikke fungere da Manjaro anvender pacman
    - husk når der pulles så skal der oprettes en .env_develop med pwd til wdmycloud
    - /home/{user}/bin skal tilføjes til ...
02-installation
    - bash scriptet programs.sh anvendes
03-install repositories
    - de pågældende repositories er opdateret i Manjaro
    - ej relevant for Manjaro
04-install-extra indgår i programs.sh
    - ej relevant for Manjaro

De resterende

følgende indgår i bash script
- packer
- php 
- vagrant

Følgende installationsscripts kan udføres

- jetbrains-toolbox
- freefilesync
- nosqlbooster
- postman

desktop items tilføjes med desktopfile.py

- smartgit skal have et desktop item

SmartGit Linux (tar.gz bundle)

    unpack the downloaded file into a directory of your choice:
    tar xzf <smartgit*.tar.gz>
    start SmartGit: invoke bin/smartgit.sh
    create SmartGit menu item: invoke
    bin/add-menuitem.sh
    remove SmartGit menu item: invoke
    bin/remove-menuitem.sh

afsluttende konfig
- xdebug.ini
- groups
- desktopfile (Tilføj smartgit item og jinja2 template)
- chown
- vbox_ext_pack kun relevant for host ej for virtuel maskine

DEBIAN_FRONTEND=nointeraction
Indsættes foran eksempelvis sudo apt update    

Konfigurationsfiler
===================

PHP
- xdebug.ini findes i /etc/php/conf.d/xdebug.ini i host versionen. skal dog aktiveres da alle linjer er kommenteret ud
- tilføj oprettelse af en index.php fil i /home/{user}/bin til brug for test af phpinfo
- php config filer /etc/php/php.ini
- der er tilsyneladende kun en config fil
- php-pdo??
- php-mysqli??
- php-mariadb??

Udestående installationer
=========================
- mongodb
- apache med php
- nginx
- afprøvning af mariadb
- evt intallation af mysql fra AUR

- apache config filer
- nginx config filer
- mongodb database og konfig

Afprøvninger
============
- javascript projekter
- php projekter
- docker

Tjek i linux PyCharm vejl for konfig oplysninger o.lign. under

- linux installation
- databaser
- udviklingsværktøjer
- webserver
- docker
