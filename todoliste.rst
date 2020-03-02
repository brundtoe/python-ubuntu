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
    
Udestående opgaver
==================

Opgaver som afventer at der bliver behov for scripts

   - mysql-server konfiguration af root med pwd og en ny user (19.10 er skiftet til version 8.x)
   - laravel/homestead
   - visual studio code
   - docker konfiguration (build af images og provisionering af databaser)

Testcases med unittest
======================

https://www.lambdatest.com/blog/top-5-python-frameworks-for-test-automation-in-2019/

med PyCharm support

- Pytest https://docs.pytest.org/en/latest/
- UnitTest (PyUnit) - Standard library https://docs.python.org/3.7/library/unittest.html
- Django har sit eget testframework
- flask dokumentationen viser PyTest eksempler
