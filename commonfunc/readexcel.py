# coding:utf-8

'''
Created on 2014-8-13

@author: tjp
'''

import xlrd
import xlwt

class OperExcel():
    #读取Excel表
    def rExcel(self,inEfile,outfile):
        rfile = xlrd.open_workbook(inEfile)
        #创建索引顺序获取一个工作表
        table = rfile.sheet_by_index(0)
        #其他方式
        #table = rfile.sheets()[0]
        #table = rfile.sheet_by_name(u'Sheet1')
    
        #获取整行，整列的值
        table.row_values(0)
        table.col_values(0)
    
        #获取行数和列数
        nrows = table.nrows - 1
        ncols = table.ncols
    
        #循环获取列表的数据
        #for i in range(nrows):
        #  print table.row_values(i)
        wfile = open(outfile,'w')
        #获取第一列中的所有值
        for i in range(nrows):
            #table.cell(i,0).value获取某一单元格的值
            wfile.write(table.cell(i,0).value.encode('utf8') + '\n')
        wfile.close()

    #将数据写入Excel表
    def wExcel(self,infile,outEfile):
        rfile = open(infile,'r')
        buf = rfile.read().split('\n')
        rfile.close()

        w = xlwt.Workbook()
        sheet = w.add_sheet('sheet1')
        for i in range(len(buf)):
            print buf[i]
            sheet.write(i,0,buf[i].decode('utf8'))
        w.save(outEfile)

'''if __name__ == '__main__':
    t = OperExcel()
    t.rExcel('test.xls','test.txt')
    t.wExcel('test.txt','1.xls')'''
    
# 第二种

def open_excel(file= 'D:\lazproj\dataup\excel\supplier.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)
        
#根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_index：表的索引
def excel_table_byindex(file= 'D:\lazproj\dataup\excel\codelist.xls',colnameindex=0,by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    colnames =  table.row_values(colnameindex) #某一行数据 
    list =[]
    for rownum in range(1,nrows):

         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i] 
             list.append(app)
    return list

#根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
def excel_table_byname(file= 'D:\lazproj\dataup\excel\supplier.xls',colnameindex=0,by_name=u'supplier'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows #行数 
    colnames =  table.row_values(colnameindex) #某一行数据 
    list =[]
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i]
             list.append(app)
    return list

'''
def main():
   tables = excel_table_byindex()
   for row in tables:
       print row

   tables = excel_table_byname()
   for row in tables:
       print row

if __name__=="__main__":
    main()   ''' 