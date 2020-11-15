# globale scripts

Opdateret november 2020

Mappen indeholder en række globale scripts som anvendes til installation af php, nginx, nodejs og mongodb i en Vagrant instans.

scripts er baseret på user **Vagrant**

## global_settings.sh
Omfatter opdatering af:

- tidszone
- /etc/fstab

## install_basis.sh
Installation af de grundlæggende pakker på en udviklingsmaskine. Alle pakkerne er uden GUI.

## install_desktop.sh
Installation af udvalgte desktop programmer med GUI. 

## install_nodejs.sh
Omfatter:

- registrering af node.js repository til aktuel lts version 
- installation af Node.js
- installation af globale npm moduler (nodemon, json-server og pm2)

## install_mongodb.sh & mongod.conf
Omfatter

- registrering af mongodb repository til seneste Ubuntu LTS 
- installation af mongodb 
- kopiering af mongodb konfig filen mongod.conf, som opretter en mappe pr. database

## install_php.sh
Installer og konfigurerer 

- php herunder php-fpm
- nginx

##install_mysql.sh
Omfatter

- installation af mysql og opdatering af pwd for user roor
- oprettelse af brugeren homestead
- oprettelse af databaserne homestead, bookstore og mystore

scriptet anvender debconf-util til at opdatere debconf databasen, som anvendes til at levere input til progrma installation.

## mysql_secure.sh
Et ikke anvendt interaktivt script som konfigurerer mysql password for root. 

scriptet demonstrerer anvendelsen af **expect** i interaktive scripts