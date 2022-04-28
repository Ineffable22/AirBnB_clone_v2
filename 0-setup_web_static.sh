#!/usr/bin/env bash
# Prepare your web servers

## Update server
sudo apt-get -y update

## Install NGINX
sudo apt-get install -y nginx

## Creates directories
sudo mkdir -p /data/web_static/shared /data/web_static/releases/test

## Create Symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

## Change owner and group like ubuntu
sudo chown -R ubuntu:ubuntu /data

## Write Hello World in index
echo "Hello World" > /data/web_static/releases/test/index.html

## Add new configuration to NGINX
data="\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo sed -i "/server_name _;/ a \\$data" /etc/nginx/sites-available/default

## Restart NGINX
sudo service nginx restart
