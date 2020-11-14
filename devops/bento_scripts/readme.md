# globale scripts

Opdateret august 2018

Mappen indeholder en række globale scripts som anvendes til installation af php, nginx, nodejs og mongodb på en Ubuntu Desktop.

## install_desktop.sh
Installation af 

* De grundlæggende pakker
* PHP og nginx
* Tilslutning af wdmycloud

## install_nodejs_mongodb.sh 
Installation af 

* Nodejs
* globale npm module
* yarn package manager
* mongodb
* konfigurationsfil til mongod som i forhold til standardudgaven tilføjer at databaserne skal placeres i hver sin mappe.

## mongod.conf
den tilrettede udgave af mongod.conf.

## anvendelse på Ubuntu server

Ved anvendelse på Ubuntu server skal programmer med GUI fjernes

* synaptic
* gparted
* system-config-samba
* gnome-system-tools

## mysql_secure.sh
interaktivt script som konfigurerer mysql password for root. 