#!/usr/bin/env bash
add-apt-repository ppa:webupd8team/java
add-apt-repository ppa:openjdk-r/ppa 
apt-get install -y git 
apt-get update
apt-get upgrade -y
apt-get install -y pdf2htmlex libmagickwand-dev unzip openjdk-8-jre-headless

miniconda=Miniconda3-py37_4.8.2-Linux-x86_64.sh
cd /vagrant
if [[ ! -f $miniconda ]]; then
    wget --quiet https://repo.continuum.io/miniconda/$miniconda
fi
chmod +x $miniconda
./$miniconda -b -p /opt/anaconda
rm -R pdf2htmlEX-0.16.0-poppler-0.62.0-ubuntu-18.04

cat >> /home/vagrant/.bashrc << END
PATH=/opt/anaconda/bin:\$PATH
source activate base
conda init --all
END