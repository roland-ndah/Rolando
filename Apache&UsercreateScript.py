#!/bin/bash
sudo yum update -y && sudo yum install httpd -y && sudo systemctl start httpd && sudo systemctl enable httpd && sudo sed -i "/^[^#]*PasswordAuthentication[[:space:]]no/c\PasswordAuthentication yes" /etc/ssh/sshd_config && sudo systemctl restart sshd && sudo useradd Admin && sudo usermod -G wheel Admin && echo 'Admin:Passw0rd123!' | chpasswd
