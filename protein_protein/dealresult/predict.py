import os
import sys
import math
import argparse
def predictPrecision(filename):
    f_predict=open(filename,'r')
    TP=0.0
    FP=0.0
    TN=0.0
    FN=0.0
    loop=0.0
    for line in f_predict:
        line=line.strip('\n')
        line=line.split(':')
        loop=loop+1
        #pre_value=float(line[0])*0.58
        #pre_value=math.log10(math.fabs(float(line[0])))*0.58+1.09
        if pre_value >=2.0 and line[1]=='Y':
            TP=TP+1
        elif pre_value<2.0 and line[1]=='N':
            TN=TN+1
        elif pre_value>=2.0 and line[1]=='N':
            FP=FP+1
        else:
            FN=FN+1
    #TPR=TP/(TP+FN)      #true positive rate  sensitivity
    #FPR=FP/(FP+TN)      #false poitive rate   
    print('TP=%f,FP=%f,TN=%f,FN=%f' %(TP,FP,TN,FN))
    ACC=(TP+TN)/loop   # accuracy
    #Pre=TP/(TP+FP)    #precison
    #Recall=TP/(TP+TN)
    MCC=((TP*TN)-(FP*FN))/math.sqrt((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN))
    print('ACC=%f,MCC=%f'%(ACC,MCC))
def main():
    parser=argparse.ArgumentParser() 
    parser.add_argument('-f', action='store', required=True, dest='filename',
                    help='name of file of mutated')
    inputs=parser.parse_args()
    predictPrecision(inputs.filename)
if __name__=="__main__":
    main()
