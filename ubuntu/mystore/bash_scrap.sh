#!/bin/bash

db_host="localhost"
db_name="homestead"
db_user="root"
db_pass="secret"

expect <<EOF
log_user 0
spawn mysqldump -h$db_host -u$db_user -p $db_name
expect "password:"
send "$db_pass\r"
log_user 1
expect eof
EOF


