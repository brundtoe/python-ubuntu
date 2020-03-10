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

Udestående opgaver Kubuntu
==========================

.. note:: husk apache og nginx skal ikke være enabled

   - Apache og php tilføjelserne samt konfig
   - php-fpm konfig og enable service php-fpm
   - Nginx samt konfig

Udestående på Manjaro
=====================

installation af gnome-keyring og test mysql-workbench

Ret installation af pgm der kræver desktop item svarende til kubuntu versionen.

php_manjaro.ini skal erstattes af php_config.ini da opdatering af php.ini er ens på de to miljøer

Udestående alle mastere
=======================

der er en fejl i .env_develop første tegn skal være et lille o (OSCAR)

Udestående Kubuntu og Manjaro
=============================


   - docker konfiguration (build af images og provisionering af databaser)

Udenstående efterfølgende på Komplett eller Esprimo
===================================================

   - vagrant
   - laravel/homestead

Testcases med unittest
======================

https://www.lambdatest.com/blog/top-5-python-frameworks-for-test-automation-in-2019/

med PyCharm support

- Pytest https://docs.pytest.org/en/latest/
- UnitTest (PyUnit) - Standard library https://docs.python.org/3.7/library/unittest.html
- Django har sit eget testframework
- flask dokumentationen viser PyTest eksempler
