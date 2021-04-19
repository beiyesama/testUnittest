# coding:utf-8
import xlrd

'''
data = xlrd.open_workbook("test.xlsx") #打开excel表格，参数是文件路径

table = data.sheets()[0]  #通过索引顺序获取
table = data.sheet_by_index(0) #通过索引顺序获取
table = data.sheet_by_name(u"sheet1") #通过名称获取

nrows = table.nrows #获取总行数
ncols = table.ncols #获取总列数

print(table.row_values(0)) #获取第一行的值
print(table.col_values(0)) #获取第一列的值
'''
class ExcelUtil():
    def __init__(self,excelPath,sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        #获取第一行作为key值
        self.keys = self.table.row_values(0)
        #获取总行数
        self.nrows = self.table.nrows
        #获取总列数
        self.ncols = self.table.ncols
    def dict_excel(self):
        if self.nrows <= 1:
            print("总行数小于等于1")
        else:
            r = []
            for i in range(self.nrows-1): #range是一个范围，它是左闭右开区间，第3个参数代表步长，可以不设置，默认为1；
                                          # i的取值就是：大于等于第一个参数，小于第二个参数
                values = self.table.row_values(i+1) #values是一个列表list
                s = {}
                for x in range(self.ncols):
                    s[self.keys[x]] = values[x]
                r.append(s)
            return r
if __name__ == "__main__":
    path = r"A:\testUnittest\unittest_study\test.xlsx"
    name = "Sheet1"
    data = ExcelUtil(path,name)
    print(data.dict_excel())

