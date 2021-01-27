#!/usr/bin/env bash 

export DEBIAN_FRONTEND=noninteractive

set -e

if ! [ "$(id -u)" == 0 ]; then
  echo "Script must be run as user: root"
  exit 1
fi

OS=$(hostnamectl | grep 'Operating System' | awk '{print tolower($3)}')

if !  [[ $OS == "ubuntu" || $OS == "debian" ]]; then
  printf "scriptet kan ikke udføres på %s\n" "$OS"
  exit 1
fi

installPackages() {

  local packages=("$@")
  for package in "${packages[@]}"; do
    if ! { dpkg -l "${package}" | grep ii; } &>/dev/null; then
      apt-get install -y "$package"
    else
      echo "$package"
    fi
  done
}

apt-get update
apt-get upgrade -y

packages=(build-essential
  dkms
  nfs-common
  ssh
  software-properties-common
  apt-transport-https
  ca-certificates
  vim
  git
  python3-pip
  python3-setuptools
  python3-virtualenv
)

installPackages "${packages[@]}"

if [ "$OS" == "ubuntu" ]; then
  packages=(lsb-core linux-headers-generic)
  installPackages "${packages[@]}"
else
  installPackages "lsb-release"
fi


pip3 install -r requirements-global.txt

sed -Ei 's/^(#?)(PasswordAuthentication)(\s*no)/\2 yes/' /etc/ssh/sshd_config        
systemctl enable ssh
systemctl start ssh

apt-get update

echo "Installerede basis programmer"        
