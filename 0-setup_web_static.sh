#!/usr/bin/env bash
# Prepare your web servers
sudo apt-get update
sudo apt-get upgrade -y
sudo apt install -y nginx
#sudo rm -rf /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
echo "Hello World" > /data/web_static/releases/test/index.html
data="\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo sed -i "/server_name _;/ a \\$data" /etc/nginx/sites-available/default
sudo apt-get autoremove -y
sudo service nginx restart