.. index:: Ubuntu Installation
.. _kubuntu-installation:

======================================
Ubuntu installation med Python Scripts
======================================
Opdateret oktober 2020

.. note:: Scripts er anvendt på Kubuntu 2004 (LTS) Fysisk maskine Komplett
   Scripts findes i repositoriet https://github.com/brundtoe/python-demo

    Script er omlagt til at runne som package i devlopment mode

I denne vejledning beskrives installation med script på en fysisk maskine eller en virtuel maskine, der skal anvendes til softwareudvikling.

.. caution:: Problemer med grafikkortet NVIDIA GTX 1060

   Alm systemopdatering medførte sort skærm med driveren nvidia-driver-450.
   Installation skal derfor foregå uden tredjeparts drivere og minimal installation

.. seealso:: Vejledning :ref:`Forberedelser`

   Når en ny clone af en virtuel master skal etableres springes til :ref:`etablering af python miljø <virtual-clone>`.

Installation af operativsystem
==============================
Den seneste udgave af Desktop Ubuntu LTS eller Kubuntu hentes på en Windows instans fra http://ubuntu.com/download/desktop og installers med Linux programmet Disks på en USB stick

Valg under installationen:

- Tastatur Dansk uden dead keys
- Minimal installation
- Fravælg trejdeparts programmer

.. caution::

   Ubuntu installeres på maskinens Solid State Disk. **Øvrige diske er deaktiveret**.
   Med Ubuntu er kun een skærm aktiv under installationen!

Nvidia Skærmdriver
------------------
.. warning:: Kan give sort skærm.

   **Kun Ubuntu**: Skifte til Nvidia driver foretages som det første for at undgå bøvl med træg skærmdialog ved login.

Software & Updates
------------------
Det tjekkes via faneblad Ubuntu Software, at **multiverse** er aktiveret. Det kan også aktiveres med::

   sudo add-apt-repository multiverse && sudo apt-get update && sudo apt-get upgrade


.. note:: Udfør opgaverne i :ref:`prepare-scripts`

.. _kubuntu-scripts:

Installation med python scripts
===============================
.. important:: Skal udføres med det virtuelle environment

Installationen udføres i et antal trin::

   cd python-demo
   source venv/bin/activate
   cd ~/sourcecode/python-demo/source

Med sudo udføres::

   cd python-demo/source
   sudo ./01_prepare_install.py
   sudo ./02_install_requirements
   sudo ./03_install_repositories
   sudo ./04_install_extra

.. seealso:: Se vejledning om :ref:`ubuntu-scripts`

.. seealso:: udfør opgaverne i vejledningen :ref:`ekstra-diske`

Supplerende installationer
==========================

Afhængig af maskinens anvendelse kan følgende udføres

- med root access::

   sudo ./install_php.py # inkl. konfig af xdbug og php.ini
   sudo ./install_vagrant.py
   sudo ./install_mysql_workbench.py (indstillet grundet Python 2 krav)

- Uden root access::

   cd python-demo/common
   python3 install_jetbrains.py (genvej til taskbar oprettes først gang programmet afvikles)
   python3 install_freefilesync.py inkl. desktopfile
   python3 install_nosqlbooster.py (se også [1]_)
   python3 install_smartgit ubuntu inkl. desktopfile (virker kun med seneste version - opdater config.ini)
   python3 install_postman.py inkl desktopfile
   python3 install_packer.py

- med root efter ovenstående::

   cd python-demo/common
   sudo ./vbox_ext_pack.py (Hvis VirtualBox er installeret)
   sudo ./groups.py
   sudo ./chown.py (ændrer rettigheder rekursivt for directories i /home{user}/programs)

.. important:: Husk at logge ud og defter ind for at få gruppetildelingen aktiveret

   Kontroller i terminalvindue med **groups**

Restore data fra backup
=======================

Data er placeret på de ekstra diske er der kun behov for at retablere data fra **/home/jackie** omfattende mapperne:

- Documents
- dumps
- Pictures
- .thunderbird

Thunderbird Konfiguration
   * Start med **thunderbird -ProfileManager**
   * Vælg at der altid skal startes med default profilen
   * Start Thunderbird og fjern add on **lightning**
   * installer **sudo apt install -y xul-ext-lightning**

   Sidste bullit er en forudsætning for kalender og tasks på Ubuntu

.. note:: Manuel Installation og konfiguration

KeePass2
   * Start KeePass2 og connect til database og keyfilen.




NoSQLBooster
============
NoSQLBooster installeres i **$HOME/Applications**. Første gang programmet startes promptes for integration med systemmenuen.

- Desktop item oprettes fra System menuen
- Programmet fjernes fra systemmenuen. Højreklik på programmet og vælg Remove AppImage from System.


.. caution:: Det kan for Node.js og PHP projekter være nødvendigt at genskabe de downloadede moduler med npm install og composer.

MongoDB
=======
Service bliver ikke startet efter installationen fordi den er disabled

der skal udføres

.. code-block:: bash

    sudo systemctl enable mongod #enabler autostart ved boot
    sudo systemctl start mongod

.. note:: Kopiering af mongod.conf inden serveren startes er ikke nødvendigt

Mysql-server og Workbench
=========================
mysql-server
------------
Service startes og enables automatisk under installation.

Instansens sikkerhedsopsætning konfigureres med::

   sudo mysl_secure_installation

.. caution:: Husk fravælg password validering for at kunne anvende de sædvanlige password alternativt skal det være LOW

På Ubuntu skal login med CLI foretages med **sudo mysql -u root -p** medens alm brugere kan logge ind med **mysql -u root -p**

.. caution:: Husk at opdatere passwords for jackie og athlon38

   Ændringen restores med **git restore** så den ikke kommer med i repositoriet.

**Initiering og oprettelse af user jackie**::

    $ sudo mysql -u root -p < /home/jackie/dumps/mysqlbackup/create_users.sql;

Dataload kan foretages med::

   cd python-demo/common
   python mysql_data.py

Filen config/config.ini skal have parameteren [Common][distribution]=ubuntu

mysql-workbench
---------------
.. important:: Gnome-keyring skal installeres på KDE distributioner. Det indgår default i gnome baserede distributioner.

   Det virker ikke på Kubuntu 20.04

   Installationen kan aktiveres i scriptet **04_install_extra.py**

PhpMyAdmin
==========
PhpMyAdmin installeres::

  sudo apt install -y phpmyadmin

Konfiguration - tilføj i  **/etc/apache2/apache2.conf**

   Include /etc/phpmyadmin/apache.conf

- Genstart apache og browse http://localhost/phpmyadmin
- Installationen findes i **/usr/share/phpmyadmin**

Docker konfiguration
====================
Docker network, data volume og images oprettes med scripts, der findes i projekt docker_standard:

.. seealso:: Vejledning :ref:`docker`


VMWare Workstation
==================
Der udføres følgende:

- Installation download fra https://vmware.com
- Tilknyt alle virtuelle maskiner
- Konfig af default folder /home/projects/vmware
- Start med sudo
   - vælg preferencer -> memory -> alle maskiner i host RAM

Virtualbox
==========
Der udføres følgende:

- Tilknyt alle virtuelle maskiner
- Konfig af default folder /home/projects/virtualbox

JetBrains
=========
Der udføres følgende

- Opret desktop items fra ~ /.local/applications/
- Installer de sædvanlige IDE
- Start de enkelte tools
- Synkroniser installation af plugins
- Editor font Noto Sans Mono 15 line spacing 1.2
- DataGrip projekter findes i ~ /.config/JetBrains/DataGrip
- Importer mysql databaserne bookstore og mystore med DataGrip user jackie
- scraps fra .config/JetBrains/ respektive IDE.

Vagrant/Homestead
=================
Afprøvning kan foretages uden opgradering af Homestead eller Laravel

.. code-block:: bash

   vagrant plugin install vagrant-vbguest
   vagrant plugin install vagrant-hostmanager
   vagrant plugin install vagrant-hostsupdater

   vagrant box add laravel/homestead

   cd /home/projects/laravel/Homestead
   vagrant up
   vagrant ssh
   cd /home/vagrant/code/bookstore
   composer install (undlad indledningsvis at opdatere laravel)
   php artisan optimize:clear (sletter alle caches)
   php artisan migrate
   php artisan db:seed
   php vendor/bin/phpunit

- Tjek appen på http://bookstore.test
- Alm bruger jens@mail.dk
- Admin bruger marial@mail.com
- Passwords for databasen jf. Homestead.yaml

webservere
==========

.. important:: Når apache2 og nginx installeres afsluttet med at standse og disable serverne for at undgå konflikter. De startes når de skal anvendes.

   Husk at udføre **install_php.py** før webserverne installeres

Script install_apache.py
------------------------
Scriptet udfører en default installation af Apache2 med php support.

Docroot er **/var/www/html**

**Herudover:**

- opdatering af servename i **apache2.conf**
- rewrite enables
- index.php generes til at vise phpinfo(), til brug for tjek af installationen
- serverens autostart disables.
- serveren standses

Script install_nginx.py
-----------------------
Scriptet udfører en default installation af Nginx.

Docroot er **/var/www/html** derfor vises Apaches startside, når Apache også er installeret.

**Herudover:**

- genreres fra templates/nginx-ubuntu.jinja en site definition med php support fra config/nginx.conf til sites-available. template anvendes, da php versionen er dynamisk.
- php7.4-fpm default konfig anvendes
- serverens autostart disables
- serveren standses

openjdk-x-jdk
=============
Java JDK (SE) installere som udgangspunkt ikke, da bl.a. JetBrains produkterne leveres med en indbygget java jre.

.. note:: Vælg den version af jre og jdk som svarer til den version, der anvendes af JetBrains tools (december 2019 jre 11)

   Hvis xml værktøjerne saxonhe, basex eller existdb skal anvendes så vælg den version som de pågældende versioner anbefaler. Saxon er pt (december 2019) den eneste som anbefaler jre 8. Øvrige kræver blot jre 8 eller nyere.

Bionic beaver repository indeholder version 8 og 11.

- apt install - y openjdk-11-jdk (ved JavaScript og java udvikling)
- apt install - y openjdk-11-jre (kan undværes ved java udvikling)

Ved installation undersøg da hvilken version der bør installeres.

Den skal fungere sammen med:

* IntelliJ IDEA
* Den valgte java applikationsserver (glasfish, Wildfly Tomcat, TomEE)

* Bionic beaver indeholder
   * Glassfish-javaee -> Java EE5
   * Tomcat 8 og 9 (kun Servlet og jsp)







