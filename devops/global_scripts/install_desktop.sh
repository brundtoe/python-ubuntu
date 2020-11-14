#!/usr/bin/env bash -eux

#Installation af programmer med GUI Ubuntu Desktop

if [ $(whoami) != "root" ]; then
        echo "Script must be run as user: root"
        exit -1
fi

export DEBIAN_FRONTEND=noninteractive

apt-get update
apt-get upgrade -y

apt-get install -y \
   gparted \
   synaptic \
   samba \
   system-config-samba \
   gnome-system-tools \

#config
sudo timedatectl set-timezone Europe/Copenhagen

# tilføj wdmycloud til /etc/fstab
wdmycloud=/home/wdmycloud
if ! [ -d $wdmycloud ] 
then
   mkdir $wdmycloud && sudo chown jackie:jackie $wdmycloud
fi
#Opdater /etc/fstab hvis wdmycloud ikke findes
wdmycloud=\/\/192.168.0.17\/dokumenter
filetable=/etc/fstab
line='//192.168.0.17/dokumenter /home/wdmycloud cifs credentials=/home/jackie/.smbcredentials,uid=1000,iocharset=utf8,sec=ntlmssp 0 0'
if ! grep -qe $wdmycloud $filetable
then
   printf "linjen findes IKKE og fstab opdateres\n"
   printf "\n$line\n" | sudo tee -a  $filetable
    
else
   printf "har fundet //192.168.0.17/dokumenter og fstab opdateres ikke\n"
fi
#Tilføj .smbcredentials hvis den ikke findes
smbcredentials=/home/jackie/.smbcredentials
if ! [ -e $smbcredentials ]
then
   printf "Opretter /home/jackie/.smbcredentials\n"
   printf 'user=jackie\npassword=oClDpHh9Hq8K' | tee $smbcredentials
   sudo chown jackie:jackie $smbcredentials && sudo chmod 660 $smbcredentials
fi

bindir=/home/jackie/bin
if ! [ -d $bindir ]
then
   printf "Opretter /home/jackie/bin"
   mkdir $bindir && sudo chown jackie:jackie $bindir
fi





