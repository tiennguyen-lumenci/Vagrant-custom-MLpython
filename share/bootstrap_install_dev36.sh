#!/usr/bin/env bash
cd /vagrant
PATH=/opt/anaconda/bin:\$PATH
source activate base
conda env create -f env.yml 
echo "done"