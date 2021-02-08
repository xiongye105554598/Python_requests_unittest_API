# _*_ coding:utf-8 _*_

import json,requests
from  Common import readConfig

def get_token():
    "获取登录token"
    login=readConfig.Read_Config()                                        #类实例化
    login_url = login.get_info('Login', 'login_host')                     #获取登录url
    headers = json.loads(login.get_info('Login', 'login_headers'))        #登录headers
    data =json.loads(login.get_info('Login', 'login_account'))            #登录账号、密码
    r = requests.request('POST', login_url, json=data, headers=headers)   #登录接口请求
    return r.json()['access_token']                                       #返回登录token

def host_headers():
    headers={}
    headers['x-key-hash']=readConfig.Read_Config().get_info('HTTP', 'x-key-hash')   #获取x-key-hash
    headers['Content-Type']='application/json;charset=utf-8'                        #添加headers
    headers['Authorization']='Bearer '+get_token()                                  #添加headers
    return headers

if __name__ == '__main__':
    print(host_headers())
