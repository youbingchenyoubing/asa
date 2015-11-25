import os
import sys
import math



 
def dealTextfile(filename,rate,rate1):
    sum=0.0
    file_result=open(filename,'r')
    loop=0
    result=0.0
    for line in file_result:
        line=line.strip('\n')
        line=line.split(':')
        #sum=sum+math.pow(((float(line[1])/0.58)*rate-float(line[2])+rate1),2)
        #sum=sum+math.pow(math.log10(math.fabs((float(line[1])/0.58)))*rate+rate1-float(line[2]),2)
        sum=sum+math.pow(rate*math.sqrt(math.fabs(float(line[1])/0.58))+rate1-float(line[2]),2)
        loop+=1
    result=math.sqrt(sum)/loop
    print "count sum is %s,the power is %s "%(str(loop),str(result))
    return result

