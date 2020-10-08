.. index: phpMyAdmin

.. _phpmyadmin:

=====================
phpMyAdmin på Manjaro
=====================
Opdateret oktober 2020

php myadmin kan installeres på Manjaro. 

Installation::

   sudo pacman -S phpmyadmin

Forudsætning

   serveren er installeret
   scriptet der opretter brugere samt databaserne bookstore og mystore er afviklet

Start httpd og php-fpm services::

   sudo systemctl start php-fpm
   sudo systemctl start httpd

Opret konfiguration **/etc/httpd/conf/extra/phpmyadmin.conf**::

   Alias /phpmyadmin "/usr/share/webapps/phpMyAdmin"
   <Directory "/usr/share/webapps/phpMyAdmin">
      DirectoryIndex index.php
      AllowOverride All
      Options FollowSymlinks
      Require all granted
   </Directory>

Tilføje nederst i **/etc/httpd/conf/httpd.conf**::

   #phpMyAdmin configuration
   Include conf/extra/phpmyadmin.conf

Genstart serveren::

   sudo systemctrl restart httpd

Opdater **/usr/share/webapps/config.inc.php**::

   $cfg['Servers'][$i]['host'] = 'localhost';

Ændres til:

   $cfg['Servers'][$i]['host'] = '127.0.0.1';

Browser http://localhost/phpmyadmin eller http://127.0.0.1/phpmyadmin
