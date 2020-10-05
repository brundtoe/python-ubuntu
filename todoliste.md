## Opgaveliste

## phpMyAdmin

DONE PHPMYADMIN på Manjaro

Forudsætning

   serveren er installeret
   scriptet der opretter brugere samt databaserne bookstore og mystore er afviklet


Start servere

   sudo systemctl start php-fpm
   sudo systemctl start httpd


/etc/httpd/conf/extra/phpmyadmin.conf

Alias /phpmyadmin "/usr/share/webapps/phpMyAdmin"
<Directory "/usr/share/webapps/phpMyAdmin">
    DirectoryIndex index.php
    AllowOverride All
    Options FollowSymlinks
    Require all granted
</Directory>

/etc/httpd/conf/httpd.conf

# phpMyAdmin configuration
Include conf/extra/phpmyadmin.conf

sudo systemctrl restart httpd

Opdater /usr/share/webapps/config.inc.php::

   $cfg['Servers'][$i]['host'] = 'localhost';

Ændres til:

   $cfg['Servers'][$i]['host'] = '127.0.0.1';

Browser http://localhost/phpmyadmin


TODO installer phpmyadmin på Kubuntu

skal downloades fra phpmyadmin.net

DONE dataload

Den nemme måde uden phpmyadmin er at runne scripts fra mappen /home/jackie/dumps


## automatisering af input til scripts

**Input til bash scripts** kan automatiseres med echo optionen -e er for at enable anvendelsen af backlash for at kunne sende \\n::

   echo -e "olsen\n\n\n" | ssh-keygen
   echo -e "password\n" | sudo mysql -u root < mystore_authors.sql; 

mere kompleks input kan foretages med en fil som pipes

   cat pwd.txt | sudo mysql -u root < mystore_authors.sql;

**input til python script med subprocess**

subprocess.run('ssh-keygen',input=b"olsen\n\n\n")


TODO scripting af mysql

   - brugeroprettelse og
   - opdatering med aktuelle data




## dokumentationen refaktoreres

kan konfig efter installation forenkles ved at ekstrahere fra installation.rst og manjaro.rst. Der er en stor fællesmængde og mindre forskelle.


## web sesrver site definitioner

Kubuntu Apache2 site definition
===============================
en apache site konfiguration med
   - opdatering af hosts
   - en site konfig til /etc/apache2/sites-available
   - enable med a2ensite <filnavn>

ref. file:///home/jackie/SphinxDoc/source/webserver/Apache.html#oprettelse-af-virtuel-host

## Kubuntu nginx site konfiguration

Se eksempel i mappen devops-files


## Manjaro http site konfiguration

Se eksempel i mappen devops-files og evt. i docker_standard

## Manjaro nginx site konfiguration

Se eksempel i mappen devops-files og evt. i docker_standard

## Udenstående efterfølgende på Komplett eller Esprimo

   - laravel/homestead

## Testcases med unittest

https://www.lambdatest.com/blog/top-5-python-frameworks-for-test-automation-in-2019/

med PyCharm support

- Pytest https://docs.pytest.org/en/latest/
- UnitTest (PyUnit) - Standard library https://docs.python.org/3.7/library/unittest.html
- Django har sit eget testframework
- flask dokumentationen viser PyTest eksempler
