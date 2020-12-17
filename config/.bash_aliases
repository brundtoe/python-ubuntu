alias ..="cd .."
alias ...="cd ../.."

alias h='cd ~'
alias c='clear'

alias xoff='sudo phpdismod -s cli xdebug'
alias xon='sudo phpenmod -s cli xdebug'

function ssh_pwd_off() {
    sudo sed -Ei 's/^#?PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
    sudo systemctl restart ssh
}

function ssh_pwd_on() {
    sudo sed -Ei 's/^#?PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
    sudo systemctl restart ssh
}

function flip() {
      if ! [ "$(id -u)" = 0 ]; then
        echo "function profile: must be run as user: root"
        return
      fi

      if [[ "$(id un 33)" == "www-data" ]]; then
        web_service="apache2"
      else
        web_service="httpd"
      fi

      if pgrep "$web_service" > /dev/null; then
        echo "Skifter fra Apache til Nginx"
        service "$web_service" stop > /dev/null
        echo "Apache stopped"
        service nginx start > /dev/null
        echo "Nginx started"
      else
        echo "Skifter fra Nginx til Apache"
        service nginx stop > /dev/null
        echo "Nginx stopped"
        service "$web_service" start > /dev/null
        echo "Apache started"
      fi

}
