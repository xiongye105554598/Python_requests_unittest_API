# _*_ coding:utf-8 _*_
import configparser,os
from Common import getPathInfo

#获取配置文件信息
class Read_Config(object):
    def __init__(self):
        path = getPathInfo.get_Path()                       #获得上级目录路径
        config_path=os.path.join(path,'config.ini')         #路径拼接
        self.config = configparser.ConfigParser()           #调用配置文件方法
        self.config.read(config_path)                       #读取配置文件

    def get_info(self,session,key):
        "读取配置文件config中指定段的键值"
        return self.config.get(session,key)


if __name__ == '__main__':
    print(Read_Config().get_info('Login','login_host'))    #测试一下，我们读取配置文件的方法是否可用
