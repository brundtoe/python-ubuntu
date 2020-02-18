# Installation og konfiguration af ubuntu

Enkeltstående scripts til brug ved konfiguration af et Ubuntu eller Kubuntu image.

Efterfølgende skal de laves som en helhed

## ParseConfig

Der anvendes ExtendedInterpolation i moduler/fetch_config

# Forbered installationen

- Der oprettes i mappen infile filen **.env** med password til** wdmycloud**
- filen infile/config.ini her opdateres alle elementer i afsnittene 

    - Common
    - ekstra.programs

Der anvendes extended parsing, da definitioner fra afsnit Common anvendes i øvrige afsnit.

# Udfør installationen

    sudo apt install -y python3-pip
    sudo pip install request
    cd directory med instalationsscriptet
    sudo ./install_kubuntu.py
    
Herefter kan følgende installeres  

**Med root access**

- vbox_ext_pack.py 
- groups.py
- chown.py (ændrer rettigheder rekursivt for et directory)

**Uden root access**

- install_jetbrains.py
- install_vagrant.py
- install_packer.py
- install_postman.py
- install_freefilesync.py


   
# opgaver som pt udføres manuelt

følgende er ikke indarbejdet i **install_kubuntu.py**

<table>
<tr>
<td>vbox_ext_pack.py</td>
<td>installerer vbox extension pack</td>
</tr>
<tr>
<td>groups.py</td>
<td>tilføj user til group (docker og vboxusers)</td>
</tr>

<tr><td></td><td></td></tr>
<tr><td></td><td></td></tr>
<tr><td></td><td></td></tr>
</table>

