drop user if exists 'homestead'@'0.0.0.0';
create user 'homestead'@'0.0.0.0' identified by 'secret';
grant all privileges on *.* to 'homestead'@'0.0.0.0' with grant option;
drop user if exists 'homestead'@'%';
create user 'homestead'@'%' identified by 'secret';
grant all privileges on *.* to 'homestead'@'%' with grant option;
drop database if exists homestead;
create database homestead character set UTF8mb4 collate utf8mb4_bin;
flush privileges;
drop user if exists 'athlon38'@'localhost';
create user 'athlon38'@'localhost' identified by 'trine-73-glf';
drop database if exists mystore;
create database mystore character set UTF8mb4 collate utf8mb4_bin;
grant all privileges on mystore.* to 'athlon38'@'localhost';
flush privileges;
drop database if exists bookstore;
create database bookstore character set UTF8mb4 collate utf8mb4_bin;
grant all privileges on bookstore.* to 'athlon38'@'localhost';
flush privileges;

