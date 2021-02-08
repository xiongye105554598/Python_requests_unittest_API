# _*_ coding:utf-8 _*_

import os

def get_Path():
    '#返回上级目录的绝对路径'
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':
    print(get_Path())