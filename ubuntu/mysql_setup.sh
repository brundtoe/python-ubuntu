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

cat > /root/.my.cnf <<EOL
[client]
user = homestead
password = "${MYSQL_PASSWD}"
host = localhost

[mysqld]
character-set-server=utf8mb4
collation-server=utf8mb4_bin
EOL

cat > /home/"$DEFAULT_USER"/.my.cnf <<EOL
[mysqld]
character-set-server=utf8mb4
collation-server=utf8mb4_bin
EOL