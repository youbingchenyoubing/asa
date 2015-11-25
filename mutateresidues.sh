#!/bin/bash
cd /home/rosetta/asa/interface_analyzer/pdbdata
python mutate_model.py $1 $2 'ALA' $3
