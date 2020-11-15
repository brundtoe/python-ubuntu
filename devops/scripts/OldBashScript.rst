.. index:: Installation

.. _script-install:

.. important:: Denne gamle vejledning er bevaret for at kunne samle op på evt mangler i python-ubuntu og de nye scritps som er tilapsset at installation alane foregår på en Vagrant instans.

==========================
Ubuntu installationsscript
==========================
:sub:`Opdateret februar 2020`

.. note:: Opdateringerne fra februar 2020 vedr. installation på Kubuntu 19.10

Softwarepakker kan installeres manuelt, med bash script eller med en kombination af Packer (chef/bento template), Vagrant og Puppet som beskrevet i afsnittet :ref:`devops-vejledninger`.

.. seealso:: Installation med :ref:`Puppet Masterless <puppet-masterless>`

I denne vejledning beskrives installation med script på en fysisk maskine eller en virtuel maskine, der skal anvendes til softwareudvikling, hvor der anvendes Vagrant herunder Laravel/Homestead og Docker.

.. seealso:: Vejledning om :ref:`repositories anvendt til installation <installation-reporitories>`

Installationsvejledning og scripts findes på https://brundtoe@bitbucket.org/brundtoe/Komplett.git, hvorfra de kan clones under installation på en frisk maskine.

Repositoriet indeholder:

* Installationsscripts
* Installationsvejledning
* Eksempler på konfigurationsfiler

File .gitignore skal opdateres i takt med at programmer installerer shortcuts i mappen $HOME/bin

.. seealso::

   Installationen kan også udføres ved hjælp af Puppet.

   Se vejledning om installation af :ref:`Puppet masterless<puppet-masterless>` host.

Backup
======

- ny kopi af Firefox genveje
- Backup med FreeFileSync
- Gem Jetbrains værktøjernes settings online
- Tjek installationsvejledninger

Installation af operativsystem
==============================
Seneste udgave af den seneste Desktop Ubuntu LTS hentes på en Windows instans fra http://ubuntu.com/download/desktop og installers med https://rufus.ie på USB stick.

.. caution::

   Ubuntu installeres på maskinens Solid State Disk. **Øvrige diske er deaktiveret**.

   Der er kun een skærm aktiv under installationen!

Software & Updates
------------------

.. important:: Skifte til Nvidia driver foretages som det første for at undgå bøvl med træg skærmdialog ved login.

- Under *software og update* søges efter additional drivers (På Kubuntu via Muon Software updates)
- Skift til Nvidia drive metapackage
- Det installerer også appen NVIDIA X Server Settings

.. note:: Nu kan skærm nummer to aktiveres

Det tjekkes via faneblad Ubuntu Software, at **multiverse** er aktiveret. Det kan også aktiveres med::

   sudo add-apt-repository multiverse && sudo apt-get update

.. _mount-diske:

Clone repository Komplett fra Bitbucket
=======================================

- installer git

Konfiguration af git user::

        git config --global user.name Jackie
        git config --global user.email brundtoe@outlook.dk

 Den globale configuration for en bruger findes i **~/git/.gitconfig**

- repositoriet clones::

   mkdir ~/bin
   cd bin
   git clone https://bitbucket.org/brundtoe/Komplett .

Husk det afsluttende punktum!

Installation af softwarepakkerne
================================
Installationen foretages i et antal trin:

#. installation af Ubuntu basale softwarepakker
#. registrering af ekstra respositories
#. Installation af Docker
#. Installation af ekstra software pakker
#. Installation af php
#. Installation af Node.js og MongoDB

.. note:: Installation af en del software pakker bl.a. fra 04-install-extra.sh gør brug af Python 2.7.

   Observer når (K)Ubuntu 20.04 installeres om det fortsast er tilfældet, da Python 2.7. er depreciated pr. 1. januar 2020.

Scriptet 01-install.sh
----------------------
Det første script installerer:

* De basale softwarepakker installeres, hvis de ikke allerede findes
* Tidszonen indstilles til *Europe/Copenhagen*
* opretter mapperne /home/{data,projects,backup} (backup kun på Komplett)
* Opretter mapper::

   mkdir -p $wdmycloud/{dokumenter,GitDepot,software,virtualmachines,public}
   chown -R jackie:jackie $wdmycloud

* Forbindelse til wdmycloud oprettes i /etc/fstab
* Mappen $HOME/bin oprettes hvis den ikke findes

.. note:: En række software pakker er deaktiveret af hensyn til Kubuntu. Eksempelvis er GNOE specifikke pakker deaktiveret eksempelvis **Synaptic Package Manager** På Kubuntu anvendes i stedet den default installerede KDE **Muon Package Manager**

Herefter kan wdmycloud mountes med :command:`sudo mount -a`

Scriptet 02-install.sh
----------------------
Scriptet tilføjer repositories for at kunne anvende nyere versioner end de der er en del af den anvendte Ubuntu LTS:

* Puppet
* Node.js 12
* mongodb 4.2
* Virtualbox 6.x
* Nginx (deaktiveret)

Hvis der opstår problemer enten med repository keys eller sources.list, så kan

- Repository keys listes med **apt-key list**
- En nøgle fjernes med **sudo apt-key del 1234567890ABCDEF** hvor hex cifrene er de sidste fire gupper i en key.
- sources kan redigeres i Muon Package manager eller Ubuntu *Software and updates**

.. caution::

   Deaktiver Virtualbox repositoriet, hvis der er incompability med Vagrant plugin vbguest

   Kontrolleres på https://github.com/dotless-de/vagrant-vbguest

   brug en version af Virtualbox, som svarer til den der indgår i Vagrantboksen **laravel/homestead**

Alternativ installation af Virtualbox
-------------------------------------
Hent en ældre version med tilhørende guest additions

- https://www.virtualbox.org/wiki/Download_Old_Builds_6_0
- Installer virutalbox guest additions
- Tilføj brugeren jackie til group vboxusers

.. important:: Brugeren skal være medlem af vboxusers for bl.a. at kunne tilslutte en USB stick

Scriptet 03-install-docker.sh
-----------------------------
Scriptet tilføjer Docker repository og installerer docker, samt tilføjer brugeren jackie til gruppen *docker*.

.. note:: Ubuntu versionen er hardkodet, da docker kun leverer binære versioner til LTS udgave af (K)Ubuntu. Der anvendes den seneste LTS version også på efterfølgende ikke LTS versioner.

Scriptet 04-install-extra.sh
----------------------------
I dette script tilføjes softwarepakker, som er ud over basisinstallationen i 01-install.sh.

Det omfatter bl.a.:

* keepass2
* filezilla
* virtualbox
* mysql-workbench

Scriptet 05-install-php.sh
--------------------------
Scriptet installerer en basisversion af php samt composer. Det er nu muligt at anvende php på hosten, så udviking kan foretages uden Vagrant eller Docker instans.

Scriptet skal opdateres hver gang der installeres for at få seneste version af Composer.

Scriptet 06-nodejs_mongodb.sh
-----------------------------
Scriptet installerer Node.js, globale npm moduler og MongoDB til brug sammen med PhpStorm og WebStorm, da remote debug af Node.js applikationer ikke er mulig.

.. note:: De globale installationer af node moduler er deaktiveret.

Scriptet 07-npm-reset.sh
------------------------
Der kan når der er udført **sudo npm install** eller tilsvarende opstå problemer med rettighederne til **~/.config** og **~/.npm**

Installations af globale node moduler udføres med root adgang og derfor skal rettighederne til mapperne

- ~/.config
- ~/.npm

.. seealso:: :ref:`nodejs installationsvejledningen <npm-access-rights>`

Scriptet install-puppet-agent.sh
--------------------------------
Installerer puppet agent på hosten.

Efterfølgende manuelle opgaver
==============================
En række opgaver udføres manuelt, da der ikke er/kan udvikles script til løsning af opgaverne.

.. note:: Opgaverne udføres maskinelt hvis maskinen installeres som :ref:`puppet-masterless`.

Mounte de ekstra diske
----------------------

.. note:: På Kubuntu skal programmet **GNOME disks** installeres

Programmet Disks anvendes til at mounte diskene

- /dev/sda1 /home/projects
- /dev/sdb1 /home/data
- /dev/sdc1 /home/backup (kun Komplett)

En række programmer skal installeres manuelt, da de ikke findes i et repository.


Restore data fra backup
-----------------------

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

Docker er installeret af script
   * Tilføj brugeren jackie **sudo -G docker -a jackie**

Virtualbox installation
   * Repository er installeret med script
   * Installer med **sudo apt install -y virtualbox-6.0**
   * Tilføj bruger **sudo -G vboxusers -a jackie**
   * Virtualbox Extension Pack hentes fra https://virtualbox.org
   * Extension installers ved at dobbeltklikke på dne downloadede extension
   * Windows maskinerne tilføjes (add) fra /home/data/virtualbox/windows
   * Virtualbox konfigureres til at gemme maskinerne i **/home/projects/virtualbox**

Google Chrome Fra http://google.com/chrome
   Download Debian versionen og installer med GDebi

JetBrains Toolbox fra https://jetbrains.com
   * pak ud til /home/jackie/bin
   * Konfigurer så der ikke installeres scripts
   * IDE konfigurationer er gemt på kontoen. De kan evt. hentes fra backup.

Opret en ssh key
   Åben terminavindue og udfør::

      cd ~/.ssh
      ssh-keygen -b 2048
      ssh-add

   Nøglen tilføjes til bitbucket og github kontiene. Evt forældede nøgler fjernes.

   Husk at remote repository skal pege på ssh adgangen i stedet for https:

SmartGit fra https://syntevo.com
   * Download Debian versionen og installer med GDebi
   * Etabler forbindelse til Bitbucket og Github

Freefilesync fra https://freefilesync.org
   * Download Linux udgaven og pak ud til /home/jackie/programs
   * Kopier ~/programs/FreeFileSync/FreeFileSync.desktop til ~/Desktop
   * Åben ~/programs/FreeFileSync/FreeFileSync.desktop
   * Rediger så der peges på den valgte installations mappe

Visual Studio code fra https://code.visualstudio.com/
   * sudo snap install --classic code
   * Installer todo-tree
   * Kopier ~/bin/config/settings.json til ~/.config/code/User/settings.json

NoSQLBooster fra https://nosqlbooster.com
   * Download appimage
   * Kopieres til ~/bin
   * programmet gøres eksekverbart og startes
   * Etabler connection til localhost
   * aktiver med user brundtoe - se nøgle i ~/Documents
   * Åben terminalvindue i ~/Desktop
   * gnome-desktop-item-edit ~/Desktop/ --create-new
   * image findes i ~/bin/images/NoSQLBooster.jpeg
   * Kopier entry ~/Desktop til ~/local/share/applications

Desktop items
-------------
Desktop items oprettes med::

   gnome-desktop-item-edit --create-new ~/Desktop

Images til bl.a. NoSQLBooster4MongoDB findes i ~/bin/images

VMWare Workstation
------------------
Installation:

- login hos https://vmware.com og Download seneste version
- find også licensnøglen det er tallet nul (0) i licensnøglen ikke bogstaver OSCAR
- start Workstation med **sudo vmware**, ændre :command:`menu -> edit -> preferencer` swap all virtuel machines in memory.

Virtuelle Windows maskiner
--------------------------
Linux herunder vagrant boxe til Virtualbox og VMware Workstation konfigureres til standard at gemme på default locations under

- /home/projects/virtualbox
- /home/projects/vmware

Her gemmes de virtuelle linux maskiner.

Evt nye Windows maskiner placeres på **/home/data**

sourcecode
==========

Sourcecode til mine projekter findes på disken med **/home/projects**. Disken er ikke berørt af installationen og kan umiddelbart anvendes.


installer evt. mysql på hosten

- apt install -y mysql-server

Installationen udført for at kunne tjekke javascript applikationerne på hosten

- se vejledning :ref:`lampserver` for oprettelse af root password
- se vejledning :ref:`mysql-workbench` for oprettelse af user, da root ikke længerer har adgang til workbench

Backup systemet
===============
Backup systemet anvender FreeFilesync

Definitionerne findes i ~/Documents/BackupDefinitions

Den primære backup disk er mountet i /home/backup

/home/wdmycloud  er den sekundære backup

   - jackie/ubuntubackup
   - virtualmachines (windows maskinerne)

USB disken anvendes som offline backup

Editoren Vim
============
**$HOME/.vimrc** opdateres med::

  syntax enable
  set tabstop=2
  set softtabstop=2
  set expandtab

Python installation
===================
Fra og med Bionic Beaver indgår Python 2.7 ikke i default installationen. Den er dog fortsat nødvendig da eksemplevis node-gyp, der anvendes til at builde node moduler ikke understøtter python 3.

.. caution:: Fra og med 1. janaur 2020 udsendes der ikke længere sikkerhedsrettelser til Python 2.7


Vagrant og Packer
=================
* Vagrant
   * Hent seneste Debian pakke og installer den https://vagrantup.com
   * vagrant plugin install vagrant-vbguest
   * vagrant plugin install vagrant-hostmanager
   * vagrant plugin install vagrant-hostsupdater

* Packer
   * Hent Packer Linux 64 bit fra https://packer.io
   * Pak ud til /home/jackie/bin

Homestead
=========
Etablering af Homestead boksen med Laravel bookstore applikationen

- Klon bitbucket repository laravel-bookstore til sourcecode/homestead/bookstore
- Klon github  repository Homestead, som indeholder laravel/Homestead
- Tilføj upstream https://github.com/laravel/homestead til git config
- Installer vagrant boxen **vagrant box add laravel/homestead**

.. note:: Det kan være nødvendigt at kopiere .env fra :menuselection:`GitDepot --> sourcecode` da filen ikke gittes.

- det ændrede layout medførte ændringer i Homestead.yaml
- Laravel Bookstore applikationen fungerer

Homebox
=======

- Alt fungerer, når man blot husker

    - at opdatere .env filen til vagrant miljø
    - at oprette brugeren athlon38, importere databaserne og give athlon38 adgang
    - udføre npm install på hosten

- wordpress (fulgte installationsvejledningen - alt fungerer)

    - opdaterede til wp 5.2
    - tog en ny backup med duplicator

Projekt devops med Vagrant
==========================

.. seealso:: Installation som anfør i :ref:`devops-geninstallation`

Docker konfiguration
====================
Maskinen klargøres til at anvende docker konfigurationerne i de enkelte projekter.

Dockerfiles hentes fra https://github.com/brundtoe/docker_standard

Herefter buildes de enkelte images.

.. seealso::

   Vejledning om genskabelse af docker environment med images, networks og data volumes

   :ref:`docker-config`.

smartgit commit ændringer til alle projkter
===========================================

Ændringer der er foretaget under afprøvning af apps skal committes og pushes

Defragmenter og komprimer virtuelle maskiner
============================================

- Alle Windows maskinerne


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
