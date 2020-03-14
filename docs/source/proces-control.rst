.. index:: !Process Control
.. _process-control:

==============
Proces kontrol
==============
Opdateret marts 2020

Procesmonitorerering og adminstration (standsning af processer) kan foretges med GUI eller med terminalen.

- På Gnome anvendes System Monitor
- PÅ KDe anvendes KSysGuard

Nedenfor beskrives hvordan det udføres med terminalen og GNU/Linux kommandoer.

Vis processerne
===============

Kommandoden *ps* anvendes til at vise de kørende proceser. Det er et snapshot der vises.

=====   =============================================
ps a    processer med terminalvindue for alle brugere
ps -A   alle processer
ps -T   alle processer i det aktuelle vindue
ps -x   alle processer uden tty
=====   =============================================

Via alle proceser med og uden tty og vis usernavn::

    ps -aux

Eller med flere detaljer herunder parent PID (PPID)::

    ps -lax

Command navne der vises som [kommando] er Linux kernens threads.

Vis kun for et enkelt program::

    ps -ax | grep pycharm

En hurtig oversigt til brug for at finde PID og slå en process ihjel::

    ps -e | grep firefox

Kommandoen **pgrep** er en kombination af ovenstående anvendelse af ps og grep::

    pgrep firefox

top og htop
===========
top og htop viser de proceser, der har det største ressourceforbrug.

De anvender hele terminalvinduet og opdateres en gang hvert andet sekund.

Output er opdelt i to dele. Headeren som viser sumarisk status og body, som viser en linje for hver proces. Det viset indhold svarer til **ps -aux**

top header er udelukkende tegnbaseret, medens htop header viser en grafik af systembelastningen.

top er installeret på alle distirbutioner, medens htop skal installeres på Ubuntu.

top visning af felter kan konfigureres ved at taste **f** eller **F**. Flere muligehder for konfiguration fremgår af https://www.computerhope.com/unix/top.htm

htop viser for neden en menulinje med valgmuligheder herunder konfiguration og help.

Det er i htop muligt med cursoren at vælge en linje og standse (kill) en process.

Se mere om htop http://hisham.hm/htop/

Signals
=======
Signals er process-level interupt requests som sendes til en proces fra en anden proces, typisk fra parent eller kernen/systemd.

De mest anvendte signaler er:

========    ================================================
Signal      Beskrivelse
========    ================================================
1   HUB     Anmodning om at standse
2   INT     Anmodning om at standse sendt med CTRL + C
3   QUIT    svarer til TERM og producerer et core dump
9   KILL    Det ultimatives signal for at standse en process
15  TERM    En anmodning om at afslutte og rydde op.
18  CONT    Fortsæt processen.
19  STOP    Stands processen indtil CONT modtages
========    ================================================

Der anvendes ofte en notationen med prefix SIG eksempelvis SIGKILL

Vis alle signaler::

    kill -l

Send kill signal
----------------

En proces standses ved at anvende dens PID eller JOB nummer ::

    sudo kill -n 9 PID
    sudo kill -s SIGKILL PID


jobs vises med kommandoen jobs

En process kan også standses med dens procesnavn::

    sudo killall httpd

foreground og background processer
==================================
På et Linux system kører proceser i forgrunden og i baggrunden. Forgrundsprocesser kan sendes i bagrunden og hentes frem igen. Processer der er startet i baggrunden forbliver normalt her.

Forgrundsproceser, der kører i et terminalvindue kan styres med::

    CTRL + C  -> sender en SIGINT og programmet standses
    CTRL + D  -> sender en SIGQUIT og
    CTRL + Z  -> Sender programmet til baggrunden selvom der på skærmen står af det er stopped.


Kommandoen **ps** viser at processen stadig eksisterer

Kommandoen **jobs** viser processen som et stopped job.

Bring jobbets output frem i forgrunden::

    bg

Det kører fortsat i baggrunden og kan ikke afsluttes med **CTRL + C**. Kommanoden **ps** vil vise at det stadig kører.

Bring jobbet frem i forgrunden med::

    fg

Nu kan jobbet standses med CTRL + C

Start et program i baggrunden ved at tilføje en enkelt **&** (ampersand) til en kommando.

Kommandoen **job l** viser jobnummeret og procesnummer. Proigrammet standses med::

    kill %jobnummer  # eller
    kill -n PID

Nogle programmer har en parameter som starter programmet i baggrunden eksempelvis::

    docker-compose up -d

.. caution::

    Modellen med **ampersand medfører bivirkninger** hvis den anvendes således::

        docker-compose up &

    Processen kører som et job i baggrunden med output sendes fortsat til stdout. og kan bringes frem i forgrunden med CTRL + C.

    **Procesen kan kun standses med **kill %1** hvor %1 er jobnummeret





- https://www.howtogeek.com/440848/how-to-run-and-control-background-processes-on-linux/


starte en daemon eksempelvis docker::

    docker-compose up -d

