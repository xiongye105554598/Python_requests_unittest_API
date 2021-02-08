# _*_ coding:utf-8 _*_

import requests
from Common import getheader
from requests import exceptions

def req(method,url,**kwargs):
    "封装http请求方法"
    headers = getheader.host_headers()             #调用header方法
    try:
        result = requests.request(method,url,headers=headers,**kwargs)    #调用request方法
        return result
    except exceptions.Timeout:
        return {"请求超时"}
    except exceptions.InvalidURL:
        return {"非法url"}
    except exceptions.HTTPError:
        return {"http请求错误"}
    except Exception as e:
        return {"错误原因:%s" % e}

if __name__ == '__main__':
    url='服务器地址'
    params={"jobid":""}
    r=req('GET',url,params=params)
    print(r.json())
