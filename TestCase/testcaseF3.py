# _*_ coding:utf-8 _*_
import unittest,paramunittest,json
from  Common import configHttp,readExcel,readConfig,getheader,getrandom,log

excel= readExcel.readExcel('API_TestCase.xlsx')                   #获取excel文件
names=excel.get_sheetnames()                                      #获取sheel
testcase=excel.get_xlsx(names[2])                                 #获取指定shell的case
baseurl = readConfig.Read_Config().get_info('HTTP','baseurl')     #获取配置文件的baseurl
headers= getheader.host_headers()                                  #获取heders
log_info =log.logger                                              #导入log系统

@paramunittest.parametrized(*testcase)
class testUserLogin(unittest.TestCase):
    def setParameters(self,NO,case_name, method,path, data,code):
        """
        从 excel 中获取用例
        :param NO: 用例序号
        :param case_name: 用例名称
        :param method: HTTP方法
        :param path: 路径
        :param data: 参数
        :param code: 响应
        """
        self.case_name =NO
        self.case_name = str(case_name)
        self.method = str(method)
        self.path = baseurl+str(path)
        self.data = json.loads(data)
        self.code=int(code)                              #字符串转字典类型

    def setUp(self):                                                   #每个case执行前执行
        log_info.info('---%s %s 测试开始---' % (names[2],self.case_name))

    def testcaseF3(self):
        self._testMethodName = self.case_name                           #当前函数方法+测试用例测试函数名称
        #self._testMethodDoc= self.case_name                            #测试函数文档
        if self.case_name in ['更新设备名称','deviceid不存在']:
            data = {}
            data['displayname'] = getrandom.randomstr()
            info = configHttp.req(self.method, self.path, json=data)#调用http请求方法
            #print(info.json())
            if self.case_name in ['更新设备名称']:
                self.assertEqual(info.status_code, self.code,('%s 断言失败' % self.case_name))#断言
            else:
                self.assertEqual(info.json()['code'], self.code, ('%s 断言失败' % self.case_name))#断言
        else:
            info = configHttp.req(self.method, self.path, json=self.data)
            #print(info.json())
            self.assertEqual(info.json()['code'], self.code,('%s 断言失败' % self.case_name))#断言

    def tearDown(self):                                 #每个case执行后执行
        log_info.info('---%s %s 测试结束---' % (names[2],self.case_name))

if __name__ == '__main__':
    suite = unittest.TestSuite()                        #创建测试套件对象
    suite.addTest(unittest.makeSuite(testUserLogin))    #添加测试用例到套件中
    runner = unittest.TextTestRunner()                  #使用TextTestRunner创建一个运行器
    runner.run(suite)                                   #执行用例



