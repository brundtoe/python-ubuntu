#!/usr/bin/expect --

set db_host "localhost"
set db_name "homestead"
set db_user "root"
set db_pass "secret"

log_user 0

spawn mysql -h$db_host -u$db_user -p -e "source mystore_authors.sql"

expect "password:"
# 
send "$db_pass\r"

log_user 1

expect eof



