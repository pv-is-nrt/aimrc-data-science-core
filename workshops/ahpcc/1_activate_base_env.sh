#!/bin/bash

module load python/3.10-anaconda
echo "Successfully loaded python/3.10-anaconda module"

echo "The following python version is loaded:"
which python

source /share/apps/bin/conda-3.10.sh
echo "Successfully activated base environment"

# (optional) change pwd to the desired directory
cd ~/Downloads