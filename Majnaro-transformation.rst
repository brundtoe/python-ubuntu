.. index:: Manjaro
    :pair: Manjaro; Python

==========================
Transformation til Manjaro
==========================

Manjaro anvendes i virtuelle maskiner (VMWare og VirtualBox) men ej på host

vmware er ikke supporteret på Manjaro

På Manjaro virtuelle maskiner anvendes kun docker ej virtualbox med vagrant. 

Alternativet er at anvende den virutelle maskine med Manajro som host.

installation af sw foretages med Pacman


Hvad hedder det i Manjaro
- apt policy
- apt get 
- apt install
- hvordan tjekkes om et program er installeret


Følgende findes i nye versioner på Manjaro

- MongoDB findes grundet licens issues ikke i repository
    - https://stackoverflow.com/questions/59455725/install-mongodb-on-manjaro

- VirtualBox 
- Docker ce er blot Docker
- docker-compose
- Chromium
- Puppet
- Node.js
- Apache
- Nginx
- Ansible
- Vagrant
- Packer
- php modulerne er uden versionsnummer pt er det 7.4
- php-xdebug er blot xdebug
- sqlite3 er blot sqlite
- python3 er blot python
- pyton3-pip er blot python-pip
- vscode

Findes i AUR alternativ download

- FreeFileSync
- jetbrains toolbox
- postman
- nosqlbooster
- virtualbox extension Pack
- hplip
- mysql-server er blot mysql (mariadb findes i repo extra)
- openresty


Hvad anvendes i stedet for hvis nødvendigt

- g++
- build-essential
- gdebi
- libsqlite-dev
- libmysqlclient-dev=
- apt-transport-http (er det til nodejs download som er overflødig)
- software-properties-common


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
