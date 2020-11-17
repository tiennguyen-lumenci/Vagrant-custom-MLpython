#!/usr/bin/env bash
add-apt-repository ppa:webupd8team/java
add-apt-repository ppa:openjdk-r/ppa 
apt-get install git -y
apt-get update
apt-get upgrade -y
apt-get install libmagickwand-dev -y
apt-get install openjdk-8-jdk -y

miniconda=Miniconda3-py37_4.8.2-Linux-x86_64.sh
cd /vagrant
if [[ ! -f $miniconda ]]; then
    wget --quiet https://repo.continuum.io/miniconda/$miniconda
fi
chmod +x $miniconda
./$miniconda -b -p /opt/anaconda

cat >> /home/vagrant/.bashrc << END
PATH=/opt/anaconda/bin:\$PATH
source activate base
conda init --all
END