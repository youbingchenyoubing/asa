import argparse
import math
import os
#usage python dealallresult.py -f1 result(input file) -O outputfilename
def getallresult(filename1,filename2):
    file_oneresult=open(filename1)
    file_allresult=open(filename2,'r+')
    file_allresult.read()
    for line in file_oneresult: 
        file_allresult.write(line)
    file_oneresult.close()
    file_allresult.close()

def main():
    parser=argparse.ArgumentParser() 
    parser.add_argument('-f1', action='store', required=True, dest='filename1',
                    help='name of file of mutated')
    parser.add_argument('-O', action='store', required=True, dest='filename2',
                    help='the file to store all result')
    inputs=parser.parse_args()
    getallresult(inputs.filename1,inputs.filename2)

if __name__=="__main__":
    main()




