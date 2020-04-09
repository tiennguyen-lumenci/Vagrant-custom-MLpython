#!/usr/bin/env bash
apt-get install git -y
apt-get update
apt-get upgrade -y

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