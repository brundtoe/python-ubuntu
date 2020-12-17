.. index: Docker
.. _docker:

====================
Docker konfiguration
====================
Opdateret oktober 2020

Docker images, network og datavolumes kan oprettes ved at anvende scripts fra projektet **docker_standard**

Docker stares med::

    sudo systemctl start docker

Hvis docker skal starte når maskinen booter::

    sudo systemctl enable docker

build images::

   cd /home/projects
   mkdir -p sourcecode/docker 
   cd sourcecode/docker
   git clone git@github.com:brundtoe/docker_standard
   cd docker_standard
   ./docker-build.sh 

.. note:: Der er forældede dependencies i @vue/cli og mongo-express

Hent data fra Github

   cd /home/jackie
   git clone git@github.com:brundtoe/dumps

opret network og data volumes (Manjaro)

   cd/home/projects/sourcecode/docker/docker_standard
   sudo systemctl start httpd
   sudo ./docker-data.sh

.. note:: På kubuntu er det sudo systemctl start apache2



