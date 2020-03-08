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
    - ej relevant for Manjaro indgår i scriptet programs.sh

Øvrige anvendte scripts
    - install_freeefilesync
    - install_jetbrains_toolbox
    - install_nosqlbooster
    - install_postman
    - desktopfile

**Følgende Findes i AUR alternativ download**

- FreeFileSync
- jetbrains toolbox
- postman
- nosqlbooster
- smartgit
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

Afsluttende konfig
==================
- groups
- chown
- vbox_ext_pack kun relevant for host ej for virtuel maskine

PHP Konfiguration
=================
Der er på Manjaro kun en enkelt php.ini fil og php versionen er ikke en del af filstien til konfigurationsfilerne

- /etc/php/php.ini
- /etc/php/conf.d/xdebug.ini

ref. https://wiki.archlinux.org/index.php/PHP#Configuration

Aktivering moduler ved at fjerne kommentarerne for::

    extension=pdo_mysql
    extension=mysqli
    extension=pdo_sqlite
    extension=sqlite3
    extension=intl
    extension=xsl

Udestående installationer
=========================
- afprøvning af mariadb
- apache med php
- nginx
- mongodb

mariadb og mysql-workbench
==========================
MariaDB blev skabt som en fork af mysql, da Oracle opkøbte Sun Microsystems. MariaDB fungerer i hovedsagen som mysql.

Indens mariadb service startes udføres::

    sudo mariadb-install-db --user=mysql --basedir=/usr --datadir=/var/lib/mysql


MariaDB skal startes med::

    sudo systemctl start mariadb

Hvis MariaDB skal starte når systemet booter::

    sudo systemctl enable mariadb

Anbefalet sikkerhed::

    mysql_secure_installation

.. note:: MariaDB prompter ikke for valideringsniveau for passwords, dvs. plugin validate_password findes ikke på MariaBD

Initiering og oprettelse af user::

    $ mysql -u root -p
    ------------------
    MariaDB> CREATE USER 'jackie'@'localhost' IDENTIFIED BY 'some_pass';
    MariaDB> GRANT ALL PRIVILEGES ON *.* TO 'jackie'@'localhost';
    MariaDB> FLUSH PRIVILEGES;
    MariaDB> quit

.. caution:: Det kan ikke forventes, at **mysql-workbench** virker sammen med MariaDB. Dv anvendelsen are begrænseet til Docker containere og Vagrant maskiner med en Debian like installation.

    I stedet anvendes på Manjaro Database View i JetBrains værktøjerne.

.. todo php.ini konfigureres med et bash script, der anvender sed i stedet for det bøvlede python script

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

