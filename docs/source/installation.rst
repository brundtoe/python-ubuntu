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

   Alm systemopdatering medførte sort skærm med driveren nvidia-driver-450

   Installation skal derfor foregå uden tredjeparts drivere og minimal installation

Backup
======

Forberedelser:

- ny kopi af Firefox genveje
- Backup med FreeFileSync
- Postman via settings -> Data  **download only my data**
- Tjek installationsvejledninger

logout for at frigøre licenser:

- nosqlbooster og kopi af programmet, da jeg kun har licens til verison 5.x
- jetbrains

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

Software & Updates
------------------

.. important:: Skifte til Nvidia driver foretages som det første for at undgå bøvl med træg skærmdialog ved login.

   På Kubuntu finder installationen selv NVIDIA driverne

- Under *software og update* søges efter additional drivers (På Kubuntu via Muon Software updates)
- Skift til Nvidia drive metapackage
- Det installerer også appen NVIDIA X Server Settings

.. note:: Nu kan skærm nummer to aktiveres

Det tjekkes via faneblad Ubuntu Software, at **multiverse** er aktiveret. Det kan også aktiveres med::

   sudo add-apt-repository multiverse && sudo apt-get update

Valg af font
------------
Som font i terminal og kate

- **Noto Sans Mono** alternativ **DejaVu Sans Mono** font size 11 pt

Tilslut øvrige harddiske (fysisk maskine)
=========================================

.. important:: Installation af **Gnome Disks** for at kunne attache diskene

   Programmet findes i Discover under system settings

- 1 TB SSD mountes på /home/projects og har serienummer S3Z9NY0M409052E og
- 2 TB HDD mountes på home/data og har serienummer  Z4ZC9EBT

  - UUID 3865c960-e586-4b04-8745-fb1ccabaf412

- 2 TB HDD mountes på /home/backup og har serienummer Z4Z8X6FA

   - UUID b6af222b-5148-4d63-b8f2-9acc1591207f

Clone repository fra Github
===========================

Installer git med::

    sudo apt install -y git vim

Tilføj ssh key::

    cd ~/.ssh
    ssh-keygen -b 4096
    ssh-add

Tilføj public key til GitHub og Bitbucket konti.

Konfiguration af git user::

   git config --global user.name Jackie
   git config --global user.email brundtoe@outlook.dk
   git config --global core.editor vim

Den globale configuration for en bruger findes i **~/git/.gitconfig**

Repositoriet clones på **virtuelle maskiner**::

   mkdir ~/sourcecode
   cd sourcecode
   git clone git@github.com:brundtoe/python-ubuntu.git


Python moduler installeres::

   cd python-ubuntu
   sudo apt install -y python3-pip
   sudo pip3 install -r requirements.txt

.. note:: Installation foretages med systemets default python installation.

   Programudvikling foretages med virtuelle environments.

Opdatering af konfigurationsfilen
=================================
Filen **config/config.ini** indeholder konfigurationsoplysninger, som anvendes i de enkelte scripts. Config.ini indlæses med Python modulet Configparser.

Opdater konfigurationen i forhold til den anvendte hardware og opdater evt til aktuelle versioner af softwaren. Følgende afsnit i config.ini opdateres som minimum.

* [Common] med user, host og seneste software versioner
* [extra.programs] Justeres i forhold til maskinens anvendelse

.. caution:: Opdater **config/.env_devlop** med password til **wdmycloud**

Installation med python scripts
===============================
Installationen udføres i et antal trin::

   cd ~/sourcecode/python-ubuntu/source

* 01_prepare_install.py
* 02_install_requirements
* 03_install_repositories
* 04_install_extra

.. note:: Alle scripts udføres med root access!

Scriptet 01_prepare_install-py
------------------------------
Scriptet foretager den grundlægende konfiguration som betår af:

* Definition af timezone
* Oprettelse af mount points for interne diske
* Oprettelse af mount points for wdmycloud
* Opdatering af fstab med mount points til wdmycloud
* /etc/sysctl.d/99-local.conf opdatres med fs.inotify.max_user_watches
* Oprettelse af

   * mappen /home/{user}/bin
   * mappen /home/ {user}/programs
   * filen .vimrc
   * images som anvendes af desktop entries koppieres til ~/bin/images

* opdatering af Linux

Scriptet 02_install_requirements.py
-----------------------------------
Scriptet installerer en række basale programmer, som defineret i config.ini. alle programmer er uden GUI.

Scriptet 03_intall_requirements.py
----------------------------------
Scriptet opretter en række software repositories, som er en forudsætning for installation af den seneste udgave af software, der normalt findes i ældre udgaver på en Ubuntu/Kubuntu/Debian installation.

* MongoDB
* VirtualBox
* Docker
* Google Chrome
* Puppet
* Node.js

Scriptet 04_install_extra.py
----------------------------
Scriptet indeholder installation af en række ekstra programmer.

.. note:: Husk afsnittet [extra.programs] skal tilpases den aktuelle maskines anvendelse.

Supplerende installationer
==========================

.. note:: På fysisk maskine kan  FreeFileSync, JetBrains toolbox, Postman, Smartgit og NoSQLBooster restores fra backup /home/jackie/Programs

.. caution:: installationen nedenfor placerer nosqlbooster i mappen /home/Jackie/Applications

   Ret efter installationen backup med FreeFileSync så den tager backup af denne mappe

Afhængig af maskinens anvendelse kan følgende udføres

**med root access**

- install_php.py inkl. konfig af xdbug og php.ini
- install_vagrant.py
- install_mysql_workbench.py (indstillet grundet Python 2 krav)

**Uden root access**:

- install_jetbrains.py (genvej til taskbar oprettes først gang programmet afvikles)
- install_freefilesync.py inkl. desktopfile
- install_nosqlbooster.py inkl. desktopfile
- install_smartgit ubuntu inkl. desktopfile
- install_postman.py inkl desktopfile
- install_packer.py

**med root efter ovenstående**

- vbox_ext_pack.py (Hvis VirtualBox er installeret)
- groups.py
- chown.py (ændrer rettigheder rekursivt for directories i /home{user}/programs)

.. important:: Husk at logge ud og defter ind for at få gruppetildelingen aktiveret

   Kontroller i terminalvindue med **groups**

Aktivering af wdmycloud/dokumenter
==================================
Alle mount point til wdmycloud er oprettet med option **noauto**.

Det ændres for //192.168.0.17/dokumenter til **auto**

Restore data (fysisk maskine)
=============================
Data fra backup af Home/jackie restores

- Documents
- dumps
- Pictures
- .thunderbird
- Firefox favoritter
- log på Postman og importer evt fra dumps/Postman

.. note:: JetBrains tools

   - Log på i Toolbox
   - Installer de anvendte tools
   - start de enkelte tools
   - synkroniser plugins
   - scraps fra .config/JetBrains/ respektive IDE. Husk først efter først start af et tool

Øvrige data findes på de øvrige diske og skal ikke restores

.. caution:: Det kan for Node.js og PHP projekter være nødvendigt at genskabe de downloadede moduler med npm install og composer.

Mysql-server og Workbench
=========================
mysql-server
------------
Service startes og enables automatisk under installation

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
-------
Service bliver ikke startet efter installationen fordi den er disabled

der skal udføres::

    sudo systemctl enable mongod #enabler autostart ved boot
    sudo systemctl start mongod

.. note:: Ovenstående udføres normalt i **04_install_extra.py**

   kopiering af mongod.conf inden serveren startes unødvendigt

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







