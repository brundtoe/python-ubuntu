Opgaveliste
===========

nodejs
------
Bliver ikke installeret i den nyere udgave fordi nodejs allerede er installeret på Kubuntu.

- kan løses ved som afslutning på installationen at udføre en apt update && apt upgrade scriptet **apt_update.py**

mongodb
-------
service bliver ikke startet efter installationen fordi den er disabled

der skal udføres::

   - kopiering af mongod.conf inden serveren startes

    sudo systemctl enabled mongod #enabler autostart ved boot
    sudo systemctl start mongod

mysql-server
------------
service startes og enables automatisk under installation

   sudo mysl_secure_installation

Husk fravælg password validering for at kunne anvende de sædvanlige password alternativt skal det være LOW

På Ubuntu skal login med CLI foretages med **sudo mysql -u root -p** medens alm brugere kan logge ind med **mysql -u root -p**

Initiering og oprettelse af user::

    $ mysql -u root -p
    ------------------
    mysql> CREATE USER 'jackie'@'localhost' IDENTIFIED BY 'some_pass';
    mysql> GRANT ALL PRIVILEGES ON *.* TO 'jackie'@'localhost';
    mysql> FLUSH PRIVILEGES;
    mysql> quit

mysql-workbench
---------------
Gnome-keyring skal installeres på KDE distributioner. Det indgår default i gnome baserede distributioner.

Installeres med Muon Package Manager eller

   sudo apt install -y gnome-keyring

.. note:: det er indsat i config.ini

webservere
==========

.. note:: Når apache2 og nignx installeres afsluttet med at standse og disable serverne for at undgå konflikter. De startes når de skal anvendes.

.. note:: Apache anvender default konfig

   Nginx anvendes med php-fpm, en standard konfig php-fpm og en opdateret udgave af /etc/nginx/sites-available/default.

Opdatering af dokumentationen
=============================

.. todo opdater docs installation.rst med ovenstående. modellen i bør være den samme som for manjaro

Udestående på Manjaro
=====================

installation af gnome-keyring og test mysql-workbench

Ret installation af pgm der kræver desktop item svarende til kubuntu versionen.

**xdebug.ini** Install_php skal opdateres så generering af xdebug.ini og kopiering til destinationen foregår på samme måde som for Kubuntu

php_manjaro.ini skal erstattes af php_config.ini da opdatering af php.ini er ens på de to miljøer

apache http server hvordan enables rewrite? kan det ses i phpinfo()

Kubuntu og Manjaro Docker afprøvning
====================================

Docker konfiguration (build af images og provisionering af databaser)

Kubuntu og manjaro systemd
==========================

Hvordan fungerer systemd. eksempelvis **sudo systemctl enable apache2**

- hvor er den fil der anvendes når en service enables
- hvordan er den struktureret
- systemd og Linux daemon

Kubuntu Apache2 site definition
===============================
en apache site konfiguration med
   - opdatering af hosts
   - en site konfig til /etc/apache2/sites-available
   - enable med a2ensite <filnavn>

ref. file:///home/jackie/SphinxDoc/source/webserver/Apache.html#oprettelse-af-virtuel-host

Kubuntu nginx site konfiguration
================================
Se eksempel i mappen devops-files

Manjaro http site konfiguration
===============================
Se eksempel i mappen devops-files og evt. i docker_standard

Manjaro nginx site konfiguration
================================
Se eksempel i mappen devops-files og evt. i docker_standard

Udenstående efterfølgende på Komplett eller Esprimo
===================================================

   - vagrant
   - laravel/homestead

Udestående ubuntu gnome
=======================
ubuntu 18.03 indeholder en gammel version af composer (1.6.3)

Testcases med unittest
======================

https://www.lambdatest.com/blog/top-5-python-frameworks-for-test-automation-in-2019/

med PyCharm support

- Pytest https://docs.pytest.org/en/latest/
- UnitTest (PyUnit) - Standard library https://docs.python.org/3.7/library/unittest.html
- Django har sit eget testframework
- flask dokumentationen viser PyTest eksempler
