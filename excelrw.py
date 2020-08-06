import xlwt
import xlrd
from xlrd.book import Book
from xlrd.sheet import Sheet
from xlrd.sheet import Cell
wb=xlwt.Workbook(encoding='ascii')
ws=wb.add_sheet('weng')
ws.write(0,0,label='日期')
ws.write(0,1,label='项目名称')
ws.write(0,2,label='项目花费')
wb.save('weng.xls')
