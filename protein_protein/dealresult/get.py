import xdrlib,sys
import xlrd
import argparse
import math
#usage python get.py -f 3.xlsx -s Sheet1
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
    file_observed=open('result.txt','w')
    #sum=0.0
    for rownum in xrange(1,nrows):
        row=table.row_values(rownum)
        if row:
            #file_observed.write(row[0]+':'+row[1]+':'+int(row[2])+':'+row[3])
            file_observed.write(str(row[0].encode('utf-8'))+':'+str(row[1].encode('utf-8'))+':'+str(int(row[2]))+':'+str(row[3].encode('utf-8')))
            #file_observed.write(str(row[0])+':'+str(row[1]))
            #strline=str(row[0])+':'+str(row[1])+':'+str(row[2])+':'+str(row[3])
            #file_observed.write(strline)
            file_observed.write('\n')
    file_observed.close()


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('-f', action='store', required=True, dest='excelfile',
                    help='excelfile is a textfile of name of xlsx')
    parser.add_argument('-s', action='store', required=False, dest='sheetName',
                    help='sheetName of excel ')
    inputs=parser.parse_args()
    excelfile=inputs.excelfile
    sheetName=inputs.sheetName
    print "%s",sheetName
    excel_table_byName(excelfile,0,sheetName)
      
if __name__=="__main__":
    main()    
