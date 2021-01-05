ALTER USER 'root'@'localhost' IDENTIFIED BY '${MYSQL_PWD}';
DELETE FROM mysql.user WHERE user='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1');
DELETE FROM mysql.user WHERE user='';
DELETE FROM mysql.db WHERE Db='test' OR Db='test_%';
FLUSH PRIVILEGES;