#__0x10-https_ssl
redirecting http to https

sudo apt update
sudo apt install snapd
sudo apt-get remove certbot
sudo apt-get install certbot
sudo service haproxy stop
sudo certbot certonly --standalone --preferred-challenges http --http-01-port 80 -d clayshub.tech
sudo ls /etc/letsencrypt/live/clayshub.tech
sudo mkdir -p /etc/haproxy/certs
DOMAIN='clayshub.com' sudo -E bash -c 'cat /etc/letsencrypt/live/$DOMAIN/fullchain.pem /etc/letsencrypt/live/$DOMAIN/privkey.pem > /etc/haproxy/certs/$DOMAIN.pem'
sudo chmod -R go-rwx /etc/haproxy/certs
sudo vi /etc/haproxy/haproxy.cfg
(make the edits here)
sudo service haproxy restart
