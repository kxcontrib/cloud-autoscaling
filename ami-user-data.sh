#!/bin/bash -x

## script to be run as root ##

# install yum packages
sudo yum update -y
sudo yum install -y amazon-efs-utils
sudo yum install -y git

# set up conda
sudo -i -u ec2-user \
    wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh \
    -O /home/ec2-user/conda.sh
chmod 777 /opt
sudo -i -u ec2-user bash /home/ec2-user/conda.sh -b -p /opt/miniconda
echo -e "\nsource /opt/miniconda/etc/profile.d/conda.sh\nconda activate\n" \
    >> /home/ec2-user/.bash_profile
source /home/ec2-user/.bash_profile

# set up kdb
sudo -i -u ec2-user conda install kdb -c kx -y
sudo -i -u ec2-user \
    git clone https://github.com/jackstapleton/rdb-autoscaling.git /opt/rdb-autoscaling

# configure aws cli
mkdir -p /home/ec2-user/.aws
AZ=$(ec2-metadata -z | cut -d ' ' -f 2)
echo -e "[default]\nregion=${AZ::-1}\noutput=json" >> /home/ec2-user/.aws/config
chown -R ec2-user:ec2-user /home/ec2-user/.aws

# create ami
INSTANCEID=$(ec2-metadata -i | cut -d ' ' -f 2)
AMIDATE=$(date +%Y%m%dD%H%M%S)
AMINAME=${AZ::-1}-kdb-ec2.ami-$AMIDATE
sudo -i -u ec2-user aws ec2 create-image --instance-id $INSTANCEID --name $AMINAME
