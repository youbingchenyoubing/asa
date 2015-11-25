#!/bin/bash
idealize.default.linuxgccdebug -database /home/rosetta/asa/rosetta_database -in::file::s $1.pdb  -fast -o idl -no_optH 
mv $1_0001.pdb $1.pdb



