.. index: Manjaro
    :pair: Manjaro; Python

====================
Manjaro Installation
====================

Manjaro anvendes i virtuelle maskiner (VMWare og VirtualBox) men ej på host

VMware er ikke supporteret på Manjaro

På Manjaro virtuelle maskiner anvendes kun Docker ej VirtualBox med Vagrant.

Alternativet er at anvende den virtuelle maskine med Manajro som host.

Manjaro er en rullende Linux distibution, som opdateres med de nyeste frigivne versioner af software packages.

Python scripts, som anvendes til installation på Ubuntu/Kubuntu er i hovedsagen overflødige, da disse scripts anvendes for at registrere repositories for at hente nyere programversioner.

.. seealso:: Vejledning :ref:`pacman`

Installation på VMware image
============================

Forbered installationen:
    - kontroller indstillingerne i config/manjaro.ini
    - udfør 01-prepare.py

Installation af software foretages med bash scripts:
    - programs.sh
    - php.sh
    - php_config.py
    - webserver.sh

Denne ændring fra Ubuntu/Debian varianten anvendes fordi Manjaro/Arch Linux kommer med opdaterede softwarepakker.

MongoDB findes grundet licens issues ikke i de officielle repositories men kun i **AUR**
    - https://stackoverflow.com/questions/59455725/install-mongodb-on-manjaro

Installation af sw som downloades og pakkes ud i mappen **programs**
    - install_freeefilesync
    - install_jetbrains_toolbox
    - install_nosqlbooster
    - install_postman
    - desktopfile

**Følgende findes i AUR som alternativ til download**
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

Afsluttende konfig
==================
Efter behov udføres:
    - groups
    - chown
    - vbox_ext_pack kun relevant for host ej for virtuel maskine

PHP Konfiguration
=================
Konfigurationen udføres med::
    - php_config.py

Der er på Manjaro kun en enkelt php.ini fil og php versionen er ikke en del af filstien til konfigurationsfilerne

- /etc/php/php.ini
- /etc/php/conf.d/xdebug.ini

ref. https://wiki.archlinux.org/index.php/PHP#Configuration



Der anvender konfigurationen i **config/php_config.ini**

Aktivering moduler ved med **sed** at fjerne kommentarerne for::

    extension=pdo_mysql
    extension=mysqli
    extension=pdo_sqlite
    extension=sqlite3
    extension=intl
    extension=xsl

Da php installeres af et bash script er konfig omlagt til at anvende GNU/Linux kommandoen **sed**, som forenkler opdateringen i forhold til Ubuntu/Debian udgaven.

MariaDB og mysql-workbench
==========================
MariaDB blev skabt som en fork af mysql, da Oracle opkøbte Sun Microsystems. MariaDB fungerer i hovedsagen som mysql.

Inden mariadb service startes udføres::

    sudo mariadb-install-db --user=mysql --basedir=/usr --datadir=/var/lib/mysql


MariaDB skal startes med::

    sudo systemctl start mariadb

Hvis MariaDB skal starte når systemet booter::

    sudo systemctl enable mariadb

Anbefalet sikkerhed::

    sudo mysql_secure_installation

.. note:: MariaDB prompter ikke for valideringsniveau for passwords, dvs. plugin validate_password findes ikke på MariaBD

Initiering og oprettelse af user::

    $ mysql -u root -p
    ------------------
    MariaDB> CREATE USER 'jackie'@'localhost' IDENTIFIED BY 'some_pass';
    MariaDB> GRANT ALL PRIVILEGES ON *.* TO 'jackie'@'localhost';
    MariaDB> FLUSH PRIVILEGES;
    MariaDB> quit

.. caution:: Det kan ikke forventes, at **mysql-workbench** virker sammen med MariaDB.

    mysql-workbench kræver at gnome-keyring er installeret, da det er her passwords gemmes.

    Opstår der for meget bøvl så kan databaseværktøjerne i JetBrains IDE anvendes.


PHP-FPM
=======
Standard konfigurationen anvendes.

php-fpm startes med::

    sudo systemctl start php-fpm

php-fpm kan enables til at starte, når maskinen booter::

    sudo systemctl enable php-fpm

Installation af webservere
==========================
Scriptet **webserver.py** installerer og udfører konfiguration af Apache, Nginx.

Der anvendes følgende konfigurationsfiler:
    - httpd.conf
    - php-fpm.conf
    - nginx.conf
    - index.html
    - installationen opretter index.php

Apache httpd server
===================
Ref.

- https://wiki.archlinux.org/index.php/Apache_HTTP_Server
- Det er standard installationen fra https://httpd.apache.org

Installationen findes i /etc/httpd
    - /etc/httpd/modules indeholder httpd moduler
    - /etc/httpd/conf/httpd.conf er den primære konfigurationssfil, som (kan) inkludere de øvrige konfigurationsfiler

Standard docroot er i **/srv/http**

Serveren skal startes::

    sudo systemctl start httpd

Hvis serveren skal køre når maskinen booter så udføres::

    sudo systemctl enable httpd

.. caution:: Husk at enten anvendes Apache eller også anvendes Nginx

Konfigurationen i **/etc/httpd/conf/httpd.conf** aktiverer::

    ServerName 127.0.0.1:80

    LoadModule proxy_module modules/mod_proxy.so
    LoadModule proxy_fcgi_module modules/mod_proxy_fcgi.so

i bunden af filen indsættes::

    Include conf/extra/php-fpm.conf

Filen **config/php-fpm.conf** kopieres til /etc/httpd/conf/extra/php-fpm.conf::

    DirectoryIndex index.php index.html
    <FilesMatch \.php$>
        SetHandler "proxy:unix:/run/php-fpm/php-fpm.sock|fcgi://localhost/"
    </FilesMatch>

Genstart::

    sudo systemctl start php-fpm
    sudo systemctl restart apache

Browser på http://localhost

Nginx
=====
- Konfig filer i /etc/nginx
- Den primære konfig fil er /etc/nginx/nginx.conf
- docroot: /usr/share/nginx/html
- php-fpm konfig findes i /etc/php.

php-fpm aktiveres ved at kopiere **config/ningx.conf** til /etc/nginx/nginx.conf

nginx startes med::

    sudo systemctl start nignx

nginx kan enables til at starte, når maskinen booter::

    sudo systemctl enable nignx

Browser på http://localhost

MongoDB
=======
MongoDB skal installeres fra AUR. Der er to muligheder:

- mongodb og mongodb-tools
- mongodb-bin og mongodb-tools-bin

Daemon startes med::

    sudo systemctl start mongodb

Det letteste er at gøre det fra Pamac Manager (GUI) til installation, opdatering og fjernelse af software

import og export funktionerne er fra mongoDB 4.x flyttet til en selvstændig pakke **mongodb-tools**

den første model

- indebærer at sourcekoden downloades og derefter buildes og testes inden der promptes for password og installationen af den buildede pakke.
- build og test trinnet tager op imod to timer

Den anden model anvender en debian package som blot installeres.

installation fra Terminal
=========================
Der anvendes kommandoen::

    pamac install mongodb-bin

Der skal interaktivt svares på en atnal spørgsmål.

.. important:: Svar ja til om build filen skal redigeres.

    Her kontrolleres scriptet for hvad downlodes og hvad foretages under installationen










Docker
======
- er installeret

Docker stares med::

    sudo systemctl start docker

Hvis docker skal starte når maskinen booter::

    sudo sysdtemctl enable docker

Afprøvninger
============
- javascript projekter
- php projekter
- docker

Problem module har ikke en parent
=================================
ImportError: attempted relative import with no known parent package

problemet opstår ikke i PyCharm, når run configuration tilføjer projektet til PYTHONPATH

https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time

http://www.programmersought.com/article/5866305471/

Fra https://docs.python.org/3.7/tutorial/modules.html#packages

"Note that relative imports are based on the name of the current module. Since the name of the main module is always "__main__", **modules intended for use as the main module of a Python application must always use absolute imports.**"

