.. index: Manjaro
    :pair: Manjaro; Python

==========================
Transformation til Manjaro
==========================

Manjaro anvendes i virtuelle maskiner (VMWare og VirtualBox) men ej på host

VMware er ikke supporteret på Manjaro

På Manjaro virtuelle maskiner anvendes kun Docker ej VirtualBox med Vagrant.

Alternativet er at anvende den virtuelle maskine med Manajro som host.

Installation Pacman
===================

Et programs dependencies findes i appen, der anvendes til program administration og på archlinux.org/packages

**Hent og udfør opdateringer**::

    pacman -Syu

.. important:: Systemet skal opdateres før enhver installation af sw packages!

**Installation af en package**::

    pacman -S <packagename>

**Installation af uden bekræftelse**::

    pacman -S --noconfirm <packagename>

**vis detaljeret info om en package**::

    pacman Si <packagename>

Hvis pacman Si returnerer 1 så findes pakken ikke

**Vis alle de explicit installerede packages**::

    pacman -Qe [packagename]

Hvis en pakke ikke er installeret returnerer pacman -Qe statuskode 1

Installation fra AUR
====================
AUR packages er brugergenererede BUILDS.

Appen **Pamac Manager** eller pamac CLI anvendes ved installation af AUR packages

Installation via script
=======================

Se Se filerne bash programs.sh og php.sh for hvilke programmer, der skal installeres

MongoDB findes grundet licens issues ikke i de officielle repositories men kun i **AUR**
    - https://stackoverflow.com/questions/59455725/install-mongodb-on-manjaro

Python scripts
==============
Manjaro er en rullende Linux distibution, som opdateres med de nyeste frigivnde versioner af software packages.

Python scripts, som anvendes til installation på Ubuntu/Kubuntu er i hovedsagen overflødige, da disse scripts anvendes for at registrere repositories for at hente nyere programversioner.

**config/config.ini**

    - afsnit [debian] hhv. [archlinux] angiver afsnit, som kun anvendes på respektive distributioner.

01-prepare
    - pacman anvendes i stedet for apt update && apt upgrade
    - /home/{user}/bin tilføjes til PATH

02-installation
    - bash scriptet programs.sh anvendes
03-install repositories
    - ej relevant for Manjaro
04-install-extra
    - ej relevant for Manjaro

**Følgende Findes i AUR alternativ download**

- FreeFileSync
- jetbrains toolbox
- postman
- nosqlbooster
- virtualbox extension Pack anvendes på hosten med Virtualbox
- (se vscode på Komplett for installation af guest additions i en Vbox manjaro gæst)
- mysql-server er blot mysql (Der anvendes i stedet mariadb fra extra repositoriet)
- openresty
- hplip findes på extra i en minimal version

Hvad anvendes - hvis nødvendigt - i stedet for nedenstående:

- g++
- build-essential
- gdebi (Ikke relevant da det er debian pakke værktøj=)
- libsqlite-dev
- libmysqlclient-dev=
- apt-transport-http (er det til nodejs download som er overflødig)
- software-properties-common




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
- php.ini (der er kun en inifil)
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

- aktivering af moduler se wiki.archlinux.org

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

Apache
======
- Det er standard installationen fra https://httpd.apache.org
- Installationen findes i /etc/httpd hvor der er et sæt konfigurationsfiler
- standard docroot er i /srv/http
- serveren skal enables og startes

    sudo systemctl enable httpd
    sudo systemctl start httpd

- hvis man undlader enable så kan installationen leve ved siden af nginx som heller ikke må enables    

.. todo: apache med php

Nginx
=====
- konfig filer i /etc/nginx
- docroot: /usr/share/nginx/html
- php-fpm konfig findes i /etc/php

.. todo: nginx med php

mariadb og mysql-workbench
==========================
- mariadb skal startes med::

    sudo systemctl start mariadb
    sudo systemctl enable mariadb

- Hvad er default password for root?

PHP
===
- php-ini
- xdebug.ini

MongoDB
=======
- installeres fra AUR

Docker
======
- er installeret
- skal startes med

    sudo systemctl start docker
    sudo sysdtemctl enable docker

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

Problem module har ikke en parent
=================================
ImportError: attempted relative import with no known parent package

problemet opstår ikke i PyCharm, når run configuration tilføjer projektet til PYTHONPATH

https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time

http://www.programmersought.com/article/5866305471/

Fra https://docs.python.org/3.7/tutorial/modules.html#packages

"Note that relative imports are based on the name of the current module. Since the name of the main module is always "__main__", modules intended for use as the main module of a Python application must always use absolute imports."

