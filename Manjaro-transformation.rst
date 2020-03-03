.. index:: Manjaro
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

Konfigurationsfiler
===================

hvor findes

- php config filer
- apache config filer
- nginx config filer
- mongodb database og konfig

Tjek i linux PyCharm vejl for konfig oplysninger o.lign. under

- linux installation
- databaser
- udviklingsværktøjer
- webserver
- docker
