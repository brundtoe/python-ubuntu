#!/usr/bin/env bash 

set -e

if ! [ "$(id -u)" == 0 ]; then
  echo "Script must be run as user: root"
  exit 1
fi

OS=$(hostnamectl | grep 'Operating System' | awk '{print tolower($3)}')

if !  [[ $OS == "manjaro" ]]; then
  printf "scriptet kan ikke udføres på %s\n" "$OS"
  exit 1
fi

pacman-mirrors --country Germany,France,Denmark,Sweden,Belgium
pacman -Syyu --noconfirm

installPackages() {

  local packages=("$@")
  for package in "${packages[@]}"; do
    if ! { pacman -Qi "$package"  &>/dev/null; } then
      pacman -S --noconfirm "$package"
    else
      echo "$package"
    fi
  done
}

packages=(base-devel
gcc
dkms
gtk2
gtkmm
make
perl
vim
nfs-utils
git
openssh
linux-headers
python-pip
python-setuptools
python-virtualenv
)

installPackages "${packages[@]}"

virtualization=$(hostnamectl | grep Virtualization | awk '{print tolower($2)}')

sed -Ei 's/^(#?)(PasswordAuthentication)(\s*no)/\2 yes/' /etc/ssh/sshd_config        
systemctl enable sshd
systemctl start sshd

mkdir -p /nfs/{ansible-demo,bash-demo,python-demo}


echo "Installerede basis programmer"        
