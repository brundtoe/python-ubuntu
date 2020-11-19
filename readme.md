# Installation og konfiguration af Ubuntu

Enkeltstående scripts til brug ved konfiguration af et Ubuntu eller Kubuntu image.

## Forbered installationen

- Der oprettes i mappen **infile** filen **.env.develop** med password til**wdmycloud**
- filen **infile/config.ini** her opdateres alle elementer i afsnittene 

    - Common (her findes parametre som anvendes i de efterfølgende afsnit)
    - ekstra.programs

## Python requirements

requirements.local.txt anvendes for installationsscripts og installeres i det lokale environment

requirements-global.txt anvnedes til Sphix kompilering af dokumentationen

## Struktur

mappen:

- config konfigurationsfiler
- common scripts som anvendes til installation på Kubuntu og Manjaro
- manjaro scripts til installation på Manjaro
- moduler scripts, der importeres som moduler i øvrige scripts mapper
- source scripts til installation på Kubuntu/Ubuntu
- devops indeholder gamle bash scripts
- outfile er demoscripts output directory

## Installationen

Forudsætning
    Vejledningen om aktivering af det virtuelle environment samt registrering af modulerne skal udføres, ellers fejler installationen  

Detaljer fremgår af dokumentationen i mappen docs

- source/installation.rst for Kubuntu
- source/manjaro.rst for Manjaro


