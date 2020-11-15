#!/usr/bin/expect --
spawn mysql_secure_installation


expect "Would you like to setup VALIDATE PASSWORD plugin?"
send "n\r"

#expect "Enter current password for root (enter for none):"
#send "secret\r"

expect "New password:"
send "secret\r"

expect "Re-enter new password:"
send "secret\r"

expect "Remove anonymous users?"
send "y\r"

expect "Disallow root login remotely?"
send "y\r"

expect "Remove test database and access to it?"
send "y\r"

expect "Reload privilege tables now?"
send "y\r"

puts "Ended expect script."