# _*_ coding:utf-8 _*_
import  logging, os,time
from  Common import getPathInfo
from logging.handlers import TimedRotatingFileHandler
now=time.strftime("%Y%m%d%H%M%S")

class Logger(object):
    def __init__(self):
        self.resultPath = os.path.join(getPathInfo.get_Path(), 'Logs')  #存放log文件的路径
        if not os.path.exists(self.resultPath):                         #判断Logs路径是否存在
            os.mkdir(self.resultPath)                                   #创建Logs文件
        self.logger = logging.getLogger()
        logging.root.setLevel(logging.NOTSET)
        self.backup_count = 5                                           #最多存放日志的数量

        # 日志输出级别
        self.console_output_level = 'WARNING'
        self.file_output_level = 'DEBUG'

        # 日志输出格式
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def get_logger(self,logfile_name=now):
        """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回"""
        if not self.logger.handlers:                                    #避免重复日志
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)
            # 每天重新创建一个日志文件，最多保留backup_count份
            file_handler = TimedRotatingFileHandler(filename=os.path.join(self.resultPath, logfile_name+'.log'), when='D',
                                                    interval=1, backupCount=self.backup_count, delay=True,
                                                    encoding='utf-8')
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger

logger = Logger().get_logger()
