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

    sudo systemctl enabled mongod #enabler autostart ved boot
    sudo systemctl start mongod
    
Udestående opgaver Kubuntu
==========================
   - juster program instal, som skal have desktopfile, så den etableres sammen med program installationen.

   - mysql-server (det er version 8) aktivering

.. note:: husk apache og nginx skal ikke være enabled

   - Apache og php tilføjelserne samt konfig
   - php-fpm konfig og enable service php-fpm
   - Nginx samt konfig

Udestående Kubuntu og Manjaro
=============================

   - docker konfiguration (build af images og provisionering af databaser)

Udenstående efterfølgende på Komplett eller Esprimo

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
