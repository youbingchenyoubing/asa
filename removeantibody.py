import sys
import os
import argparse
import __main__
__main__.pymol_argv=['pymol','-rqkc'] #pymol quiet and no GUI
try :
    import pymol
    del pymol
except ImportError :
    print "pymol has not been installed on this system.Please install it from the following link:"
    print "http://www.pymol.org/"
    sys.exit(1)
    pass

import pymol
from pymol import cmd,stored,math


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('-p', action='store', required=True, dest='pdbfile',
                    help='pathfile is a textfile of name of pdb')
    parser.add_argument('-l', action='store', required=True, dest='loop',
                    help='loop is an int number')
    inputs=parser.parse_args()
    pdbfile=inputs.pdbfile
    loop=int(inputs.loop)
    print "loop is %s "% loop
    dirname=os.getcwd()+'/interface_analyzer/pdbdata/'+pdbfile
    pdbfileselect=pdbfile.split('.')
    savefile=os.getcwd()+'/interface_analyzer/pdbdata/'+pdbfileselect[0]+'_antigen.pdb'
    print "remove antibody of complex,so can caculate the value of antigen sasa "
    pymol.finish_launching()
    if loop!=0:
        pymol.cmd.reinitialize()
    cmd.load(dirname)
    cmd.remove('hetatm')
    cmd.select('target1',pdbfileselect[0])
    cmd.save(dirname,(('target1')))
    cmd.delete('target1')
    cmd.remove('solvent')
    cmd.remove('hydrogens')
    cmd.remove('chain L+H')
    cmd.select('target',pdbfileselect[0])
    cmd.save(savefile,(('target')))
    cmd.delete(all)
    cmd.sync()
    cmd.quit()
    print "remove the antibody of complex have done"

#def renamechain(pdbfile,chainbefore,chainafter):
   # dirname=os.getcwd()+'/interface_analyzer/'+pdbfile
    #pdbfileselect=pdbfile.split('.')
    #print "rename the chain name of pdb i order to make antibody'chain is H ro L"
   # pymol.finish_launching()
    #pymol.cmd.load(dirname)
    #pymol.cmd.alter((chainbefore),chain=chainafter)
    #pymol.cmd.save(dirname,((pdbfileselect[0]))) 
    #pymol.cmd.delete('all')
    #print "rename name of chain has been done"
    
#def removesolvent(pdbfile):
    #dirname=os.getcwd()+'/interface_analyzer/pdbdata/'+pdbfile
    #pdbfileselect=pdbfile.split('.')
    #print "remove solvent for pdb"
    #pymol.finish_launching()
    #pymol.cmd.load(dirname)
    #pymol.cmd.remove('solvent')
    #pymol.cmd.select('target',pdbfileselect[0])
    #pymol.cmd.save(dirname,(('target')))
    #pymol.cmd.delete('all')
    #pymol.cmd.quit()'
       
if __name__=="__main__":
    print "in removeantibody" 
    main()
