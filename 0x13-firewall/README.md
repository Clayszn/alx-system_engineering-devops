0x13-firewall

telnet web-02.clayshub.tech 22
netstat -lpn
grep listen /etc/nginx/sites-enabled/default

Configure ufw so that it blocks all incoming traffic, except the following TCP ports:
22 (SSH)
443 (HTTPS SSL)
80 (HTTP)
