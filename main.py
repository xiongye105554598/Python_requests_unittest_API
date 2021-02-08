# _*_ coding:utf-8 _*_
import unittest, os, time
from Common import getPathInfo, readConfig, HTMLTestRunnerCN_py3,log,sendemail
#from tomorrow import threads

nowtime = time.strftime("%Y%m%d%H%M%S")
log_info = log.Logger().get_logger()
on_off=readConfig.Read_Config().get_info('Email','on_off')

class All_Test(object):
    def __init__(self):
        global report_path
        path=getPathInfo.get_Path()
        report_path = os.path.join(path, 'Report')               #测试报告存放路径
        if not os.path.exists(report_path):                      #判断Logs路径是否存在
            os.mkdir(report_path)                                #创建Logs文件
        self.caselist_path = os.path.join(path, "caselist.txt")  #配置执行哪些测试文件的配置文件路径
        self.casepath = os.path.join(path, "TestCase")           #测试用例路径
        self.caselist = []                                       #定义一个空列表

    def get_caselist(self):
        '''
        读取caselist.txt文件中的用例名称，并添加到caselist元素组
        '''
        fb = open(self.caselist_path)                            #打开文件
        for value in fb.readlines():                             #遍历fb所有数据
            if value != '' and not value.startswith('#'):        #如果data非空且不以#开头
                self.caselist.append(value.replace('\n', ''))    #读取每行数据会将换行转换为\n，去掉每行数据中的\n
        fb.close()                                               #关闭文件
        return self.caselist                                     #返回caselist

    def add_case(self):
        '''
        添加测试用例
        '''
        self.get_caselist()                                      #获得testcase列表
        suite = unittest.TestSuite()                             #创建测试套件
        suite_module = []                                        #定义一个列表
        for case in self.caselist:
            discover = unittest.defaultTestLoader.discover(self.casepath, pattern=case + '.py',top_level_dir=None)  # 加载测试用例
            suite_module.append(discover)                        #将测试用例添加到列表中
        if len(suite_module) > 0:                                #判断suite_module是否存在元素,列表才能判断长度，suite不能判断
            for i in suite_module:                               #如果存在，循环取出元素组内容，命名为suite
                for j in i:
                    suite.addTest(j)                             #取出suite_module，使用addTest添加到测试集
            return suite                                         #返回测试集
        else:
            return None

    def send_report(self):
        "#发送报告到邮件"
        report_list=os.listdir(report_path)                                     #获得目录所有文件
        report_list.sort(key=lambda fn: os.path.getmtime(report_path+"\\"+fn))  #按时间顺序排序
        file_new=os.path.join(report_path+'\\'+report_list[-1])                 #找到最新生成的文件
        sendemail.send_mail(file_new)                                               #调用email参数

    #@threads(6)
    def run_case(self):
        '''执行所有的用例, 并把结果写入测试报告'''
        log_info.info("********************TEST START********************")
        try:
            all_case = self.add_case()                                                      #调用add_case获取suite
            if all_case != None:
                test_name = readConfig.Read_Config().get_info('Report', 'test_name')        #获取测试人员姓名
                report_title = readConfig.Read_Config().get_info('Report', 'report_title')  #获取测试报告名称
                fp = open(report_path + '\\' + report_title + nowtime + '.html','wb')       #定义一个文件对象，给后面的HTMLTestRunner生成测试报告用，注意打开方式必须是wb
                runner = HTMLTestRunnerCN_py3.HTMLTestRunner(stream=fp, title=report_title, description="用例测试情况",tester=test_name)  #生成HTML报告
                runner.run(all_case)      #执行用例
                fp.close()
            else:
                log_info.info('---测试套件为空---')

        except Exception as ex:
            log_info.error(str(ex))

        finally:
            log_info.info("*********************TEST END*********************")

        # 判断邮件发送的开关
        if on_off == 'on':
            self.send_report()                       #发送测试报告
        else:
            print("邮件发送开关关闭")

if __name__ == '__main__':
    result=All_Test()
    result.run_case()

