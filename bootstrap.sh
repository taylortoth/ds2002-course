#!/bin/bash

/usr/bin/apt update -y
/usr/bin/apt upgrade -y
/usr/bin/apt install -y git 
/usr/bin/apt install -y python3
/usr/bin/apt install -y nginx

aws ec2 run-instances --security-group-ids sg-0ad6307cb868702b7 --image-id ami-0c101f26f147fa7fd --key-name id_rsa --count 1 --instance-type t2.micro --user-data file://bootstrap.sh
ssh -i ~/.ssh/id_rsa ec2-user@54.226.184.143
