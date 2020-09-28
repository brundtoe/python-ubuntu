.. index:: Ubuntu Installation
.. _installation:

======================================
Ubuntu installation med Python Scripts
======================================
Opdateret september 2020

.. note:: Scripts er anvendt på Kubuntu 2004 (LTS) Fysisk maskine Komplett
   Scripts findes i repositoriet https://github.com/brundtoe/python-ubuntu

I denne vejledning beskrives installation med script på en fysisk maskine eller en virtuel maskine, der skal anvendes til softwareudvikling.

.. caution:: Problemer med grafikkortet NVIDIA GTX 1060

   Alm systemopdatering medførte sort skærm med driveren nvidia-driver-450.
   Installation skal derfor foregå uden tredjeparts drivere og minimal installation

Backup
======

Forberedelser:

- ny kopi af Firefox genveje
- Backup med FreeFileSync
- Postman via settings -> Data  **download only my data**
- Tjek installationsvejledninger

Logout for at frigøre licenser:

- nosqlbooster og kopi af programmet, da jeg kun har licens til version 5.x
- jetbrains

.. note:: Installationen kan forenkles ved med **FreeFileSync** at overføre projekt php-ubuntu til en USB stick og anvende indholdet herfra. Det muliggør scripting af alle dele af installationen.

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
.. important:: Kan give sort skærm.

   **Kun Ubuntu**: Skifte til Nvidia driver foretages som det første for at undgå bøvl med træg skærmdialog ved login.

Software & Updates
------------------
Det tjekkes via faneblad Ubuntu Software, at **multiverse** er aktiveret. Det kan også aktiveres med::

   sudo add-apt-repository multiverse && sudo apt-get update

Klargøring til installations med scripts
========================================
Font i terminal og kate::

   Noto Sans Mono** alternativ **DejaVu Sans Mono** font size 11 pt


Installer git og vim med::

    sudo apt install -y git vim

Konfiguration af git user::

   git config --global user.name Jackie
   git config --global user.email brundtoe@outlook.dk
   git config --global core.editor vim

Tilføj ssh key::

    cd ~/.ssh
    ssh-keygen -b 4096
    ssh-add

Tilføj public key til GitHub og Bitbucket konti.

Installation af Visual Studio code::

   sudo snap install --classic code

- Installer Python extension
- Installer TODO extension
- Kopier settings fra Hosten ~/.config/Code/User/settings.json

Clone repository fra Github (uden USB stick)
============================================
Repositoriet clones på **virtuelle maskiner**::

   mkdir ~/sourcecode
   cd sourcecode
   git clone git@github.com:brundtoe/python-ubuntu.git


.. note:: Udfør derefter :ref:`ovenstående scripts <kubuntu_scripts>`

Klargøring til Script installation
==================================
Indholdet fra USB stick kopieres til /home/jackie/sourcecode/python-ubuntu eller repositoriet clones fra GitHub.

.. code-block:: bash

   cd python-ubuntu
   sudo apt install -y python3-pip python3-venv python3-setuptools
   sudo pip3 install -r requirements.txt
   python3 -m venv venv
   python3 setup.py develop

.. important:: Installation skal foretages med de globale environment, og python-ubuntu skal være installeret i development mode.

   requirements skal installeres globalt, da sudo anvender det globale environment selvom et virtuelt environment er aktiveret

Opdatering af konfigurationsfilen
=================================
Filen **config/config.ini** indeholder konfigurationsoplysninger, som anvendes i de enkelte scripts. Config.ini indlæses med Python modulet Configparser.

Opdater konfigurationen i forhold til den anvendte hardware og opdater evt til aktuelle versioner af softwaren. Følgende afsnit i config.ini opdateres som minimum.

* [Common] med user, host og seneste software versioner
* [extra.programs] Justeres i forhold til maskinens anvendelse

.. caution:: Husk at opdatere **config/.env_devlop** med password til **wdmycloud**

.. _kubuntu_scripts:

Installation med python scripts
===============================
.. important:: Skal udføres med det globale environment

Installationen udføres i et antal trin::

   cd python-ubuntu
   cd ~/sourcecode/python-ubuntu/source

Med sudo udføres:

* 01_prepare_install.py
* 02_install_requirements
* 03_install_repositories
* 04_install_extra

.. seealso:: Se vejledning om :ref:`ubuntu-scripts`

Tilslut øvrige harddiske (fysisk maskine)
=========================================
Mount points er oprettet i scriptet 01_prepare_install.

.. important:: Manuel installation kræver anvendelse af af **Gnome Disks** 
   Programmet findes i Discover under system settings

- 1 TB SSD mountes på /home/projects
   - serienummer S3Z9NY0M409052E
   - UUID dde1bf8b-3552-4709-a6d7-5f3605d966a3

- 2 TB HDD mountes på home/data
   - serienummer  Z4ZC9EBT
   - UUID 3865c960-e586-4b04-8745-fb1ccabaf412

- 2 TB HDD mountes på /home/backup
   - serienummer Z4Z8X6FA
   - UUID b6af222b-5148-4d63-b8f2-9acc1591207f

Udfør::

   sudo ./extra-diske.py

Tilslut wdmycloud
==================
Mount points er oprettet i 01_prepare_install.py

Udfør::

   sudo ./wdmycloud.py


Supplerende installationer
==========================

.. caution:: installationen nedenfor placerer nosqlbooster i mappen /home/Jackie/Applications

   Ret efter installationen backup med FreeFileSync, så den tager backup af denne mappe

Afhængig af maskinens anvendelse kan følgende udføres

- med root access
   - install_php.py inkl. konfig af xdbug og php.ini
   - install_vagrant.py
   - install_mysql_workbench.py (indstillet grundet Python 2 krav)

- Uden root access
   - install_jetbrains.py (genvej til taskbar oprettes først gang programmet afvikles)
   - install_freefilesync.py inkl. desktopfile
   - install_nosqlbooster.py inkl. desktopfile
   - install_smartgit ubuntu inkl. desktopfile
   - install_postman.py inkl desktopfile
   - install_packer.py

- med root efter ovenstående

   - vbox_ext_pack.py (Hvis VirtualBox er installeret)
   - groups.py
   - chown.py (ændrer rettigheder rekursivt for directories i /home{user}/programs)

.. important:: Husk at logge ud og defter ind for at få gruppetildelingen aktiveret

   Kontroller i terminalvindue med **groups**


Administation af users and groups
=================================
Administration af users og groups kan udføres med **lxqt-admin**.

**Installation**::

   sudo apt install -y lxqt-admin

Der oprettes ikke automatisk desktop items til startmenuen. Desktop items findes i **/usr/share/applications** og kan herfra kopieres til ~/Desktop

Ref. https://github.com/lxqt/lxqt/wiki

Visual Code installation
========================
**Installation**::

    snap install -- classic code
       
- Installation af plugin TODO tree
- Genskab konfig filen fra en backup /home/jackie/.config/Code/User/settings.json

Restore data (fysisk maskine)
=============================
- Data fra backup af Home/jackie restores
   - Documents
   - dumps
   - Pictures
   - .thunderbird
   - Firefox favoritter
   - log på Postman og importer evt fra dumps/Postman

Øvrige data findes på de øvrige diske og skal ikke restores

.. caution:: Det kan for Node.js og PHP projekter være nødvendigt at genskabe de downloadede moduler med npm install og composer.

Mysql-server og Workbench
=========================
mysql-server
------------
Service startes og enables automatisk under installation.

Instansens sikkerhedsopsætning konfigureres med::

   sudo mysl_secure_installation

.. caution:: Husk fravælg password validering for at kunne anvende de sædvanlige password alternativt skal det være LOW

På Ubuntu skal login med CLI foretages med **sudo mysql -u root -p** medens alm brugere kan logge ind med **mysql -u root -p**

**Initiering og oprettelse af usere og databaser**::

    $ sudo mysql -u root -p < /home/jackie/dumps/mysqlbackup/create_users.sql;

Opretter brugerne jackie og athlon38 samt databaserne bookstore og mystore

mysql-workbench
---------------
.. important:: Installationen foretages kun på virtuelle maskiner, hvis JetBrains Datagrip ikke anvendes

   Gnome-keyring skal installeres på KDE distributioner. Det indgår default i gnome baserede distributioner.

   Installationen kan aktiveres i scriptet **04_install_extra.py**

MongoDB
=======
Service bliver ikke startet efter installationen fordi den er disabled

der skal udføres

.. code-block:: bash

    sudo systemctl enable mongod #enabler autostart ved boot
    sudo systemctl start mongod

.. note:: Kopiering af mongod.conf inden serveren startes er ikke nødvendigt

Docker konfiguration
====================
Docker network, data volume og images oprettes med scripts, der findes i projekt docker_standard:

- docker-data.sh
- docker-build.sh

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
- serveren standses
- serverens autostart under Linux boot disables.

Script install_nginx.py
-----------------------
Scriptet udfører en default installation af Nginx.

Docroot er **/var/www/html** derfor vises Apaches startside, når Apache også er installeret.

**Herudover:**

- genreres fra templates/nginx-ubuntu.jinja en site definition med php support fra config/nginx.conf til sites-available. template anvendes, da php versionen er dynamisk.
- php-fpm default konfig anvendes
- serverens autostart disables







