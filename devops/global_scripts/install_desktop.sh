#!/usr/bin/env bash
#basic installationsscript anvendes pt kun på Ubuntu Desktop

sudo apt-get update
sudo apt-get upgrade -y
# dpkg skal installeres, da den anvendes senre i scriptet
sudo apt-get -y install dpkg

# Installer pakkerne, hvis de ikke allerede er installeret
PACKAGES="linux-headers-$(uname -r) build-essential dkms
vim curl wget git cifs-utils
expect
gparted synaptic
samba system-config-samba gnome-system-tools
php7.2-cli og php7.2-cgi
php7.2-fpm nginx
php7.2-cgi php7.2-sqlite php7.2-xsl php7.2-intl
php7.2-common php-7.2-mysql php7.2-zip php7.2-mbstring
php7.2-curl php7.2-json php-xml php-xdebug
python2.7 python-dev python2.7-dev 
sqlite3 libsqlite3-dev
unixodbc unixodbc-dev
libssl-dev libmysqlclient-dev
patch ruby-dev
zlib1g-dev liblzma-dev libkrb5-dev libkrb5-dbg 
"

for package in $PACKAGES
do
   dpkg -s $package &> /dev/null
   if [ $? -ne 0 ]; then
      sudo apt-get -y install $package
   else
      printf "Package $package is installed!\n"
   fi
done

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





