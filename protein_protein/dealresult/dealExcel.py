import xdrlib,sys
import xlrd
import argparse
import math
#usage python dealExcel.py -f inputfile -s (optionnal if -c is xlsx it may be useful if your excel file is not Sheet1) -c if xlsx is deal excel file else deal otherfile
def open_excel(file):
    try:
        data=xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)
def excel_table_byName(excelfile,colonameindex=0,sheetindex=u'Sheet1'):
    data=open_excel(excelfile)
    table=data.sheet_by_name(sheetindex)
    nrows=table.nrows
    colnames=table.row_values(colonameindex)
    sum=0.0
    for rownum in xrange(1,nrows):
        row=table.row_values(rownum)
        if row:
            sum=sum+math.pow((float(row[0])-float(row[1])),2)
    print "count sum is %s "%str(nrows)
    return math.sqrt(sum)/nrows

def dealTextfile(filename,rate):
    sum=0.0
    file_result=open(filename,'r')
    loop=0
    for line in file_result:
        line=line.strip('\n')
        line=line.split(':')
        sum=sum+math.pow(((float(line[1])/0.58)*rate-float(line[2])),2)
        loop+=1
    print "count sum is %s"%str(loop)
    return math.sqrt(sum)/loop
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('-f', action='store', required=True, dest='excelfile',
                    help='excelfile is a textfile of name of xlsx')
    parser.add_argument('-s', action='store', required=False, dest='sheetName',
                    help='sheetName of excel ')
    parser.add_argument('-c', action='store', required=True, dest='choose',
                    help='list of choose function ')
    inputs=parser.parse_args()
    excelfile=inputs.excelfile
    sheetName=inputs.sheetName
    print "%s",sheetName
    if inputs.choose=='xlsx':
        result=excel_table_byName(excelfile,0,sheetName)
        print str(result)
    else:
        result1=dealTextfile(excelfile,1)
        print "%s:" %str(result1)
      
if __name__=="__main__":
    main()    
