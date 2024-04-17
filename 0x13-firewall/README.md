0x13-firewall

telnet web-02.clayshub.tech 22
netstat -lpn
grep listen /etc/nginx/sites-enabled/default

Configure ufw so that it blocks all incoming traffic, except the following TCP ports:
22 (SSH)
443 (HTTPS SSL)
80 (HTTP)

#configures web-01 so that the firewall redirects port 8080/TCP to port 80/TCP.
*nat
:PREROUTING ACCEPT [0:0]
-A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80
COMMIT

After adding this line of code to the file, reload the firewall by running
sudo ufw reload

test on the web-02 by running 
curl -sI web-01.clayshub.tech:80

curl -sI web-01.clayshub.tech:8080
