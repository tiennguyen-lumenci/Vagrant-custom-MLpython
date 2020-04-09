#!/usr/bin/env bash
cd /vagrant
rm Min*
PATH=/opt/anaconda/bin:\$PATH
source activate base
conda env create -f env.yml 
echo "done"