#!/bin/bash

MYSQL_PASSWD=${1}
DEFAULT_USER=${2}

if [[ -z "${MYSQL_PASSWD}" || -z "${DEFAULT_USER}" ]]; then
    echo "mysql password hhv user skal overføres"
    exit 1
fi

echo "default_password_lifetime = 0" >>/etc/mysql/mysql.conf.d/mysqld.cnf

echo "Configure MySQL Remote Access"
sed -i '/^bind-address/s/bind-address.*=.*/bind-address = 0.0.0.0/' /etc/mysql/mysql.conf.d/mysqld.cnf

mysql --user="root" --password="${MYSQL_PASSWD}" -e "CREATE USER 'root'@'0.0.0.0' IDENTIFIED BY '${MYSQL_PASSWD}';"
mysql --user="root" --password="${MYSQL_PASSWD}" -e "GRANT ALL PRIVILEGES ON *.* TO 'root'@'0.0.0.0' WITH GRANT OPTION;"

service mysql restart

echo "Configure user homestead"
mysql --user="root" --password="${MYSQL_PASSWD}" -e "CREATE USER 'homestead'@'0.0.0.0' IDENTIFIED BY '${MYSQL_PASSWD}';"
mysql --user="root" --password="${MYSQL_PASSWD}" -e "CREATE USER 'homestead'@'%' IDENTIFIED BY '${MYSQL_PASSWD}';"
mysql --user="root" --password="${MYSQL_PASSWD}" -e "GRANT ALL PRIVILEGES ON *.* TO 'homestead'@'0.0.0.0' WITH GRANT OPTION;"
mysql --user="root" --password="${MYSQL_PASSWD}" -e "GRANT ALL PRIVILEGES ON *.* TO 'homestead'@'%' WITH GRANT OPTION;"
mysql --user="root" --password="${MYSQL_PASSWD}" -e "FLUSH PRIVILEGES;"

echo "Opretter databaserne homestead bookstore og mystore"
mysql --user="root" --password="${MYSQL_PASSWD}" -e "CREATE DATABASE homestead character set UTF8mb4 collate utf8mb4_bin;"
mysql --user="root" --password="${MYSQL_PASSWD}" -e "CREATE DATABASE bookstore character set UTF8mb4 collate utf8mb4_bin;"
mysql --user="root" --password="${MYSQL_PASSWD}" -e "CREATE DATABASE mystore character set UTF8mb4 collate utf8mb4_bin;"

echo "opdaterer my.cnf"

tee /root/.my.cnf <<EOL
[client]
user = homestead
password = "${MYSQL_PASSWD}"
host = localhost

[mysqld]
character-set-server=utf8mb4
collation-server=utf8mb4_bin
EOL

tee /home/"$DEFAULT_USER"/.my.cnf <<EOL
[mysqld]
character-set-server=utf8mb4
collation-server=utf8mb4_bin
EOL