import argparse
import math
import os
def getdict(filename,filename1):
    loop=0
    dirname=os.getcwd()+'/'+filename  #filename is the result of my porgram and filename1 is the basis of paper
    file_mutate=open(dirname)
    dict1={}
    for line in file_mutate:
        loop+=1
        if loop!=1:
            line=line.strip('\n')
            line=line.split(':')
            dict1[line[0]]=line[2]
    file_mutate.close()
    dirname=os.getcwd()+'/'+filename1
    file_observed=open(dirname)
    file_result=open(filename,'w')
    for line in file_observed:
        line=line.strip('\n')
        line=line.split(':')
        searchName=line[0]+'ALA'+line[1]+line[2]+'.pdb'
        if dict1.has_key(searchName):
            file_result.write(searchName+':'+str(dict1[searchName])+':'+str(float(line[3])))
            file_result.write('\n')
    file_observed.close()
    file_result.close()


def main():
    parser=argparse.ArgumentParser() 
    parser.add_argument('-f1', action='store', required=True, dest='filename1',
                    help='name of file of mutated')
    parser.add_argument('-f2', action='store', required=True, dest='filename2',
                    help='name of file of observed')
    inputs=parser.parse_args()
    getdict(inputs.filename1,inputs.filename2)


if __name__=="__main__":
    main()




