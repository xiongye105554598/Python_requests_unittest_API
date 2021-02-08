# _*_ coding:utf-8 _*_
from Common import getPathInfo
import xlrd,os

class readExcel(object):
    def __init__(self,xlsx_name):
        path = getPathInfo.get_Path()                               #获得上级目录路径
        self.xlsPath = os.path.join(path, 'TestData', xlsx_name)    #获取用例文件路径
        self.file = xlrd.open_workbook(self.xlsPath)                #打开用例Excel

    def get_sheetnames(self):
        "返回所有sheet名称"
        names=self.file.sheet_names()
        return names

    def get_xlsx(self,sheet):
        "获取Excel中测试用例相关信息"
        list = []                                                   #定义一个空列表
        sheet = self.file.sheet_by_name(sheet)                      #获得指定sheet数据
        row_value1 = sheet.row_values(0)                            #获取第1行的标题
        nrows = sheet.nrows                                         #获取当前sheet行数
        ncols = sheet.ncols                                         #获取当前sheet列数
        for i in range(1, nrows):                                   #从第2行遍历当前sheet
            row = sheet.row_values(i)                               #获取行数据
            dict = {}                                               #创建空字典
            for j in range(0, ncols):                               #遍历sheet列，组成字典
                if row_value1[j] == 'NO.' or row_value1[j] == 'code':
                    dict[row_value1[j]] = int(row[j])               #NO和code值取int
                else:
                    dict[row_value1[j]] = row[j]                    #从第一列开始，将每一列的数据与第1行的数据组成一个键值对，形成字典
            list.append(dict)                                       #将字典添加list中
        return list                                                 #返回列表

if __name__ == '__main__':                       #测试一下方法是否可用
    x=readExcel('API_TestCase.xlsx')
    print(x.get_sheetnames())
    print(x.get_xlsx('F1'))