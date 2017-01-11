# -*- coding: utf-8 -*-
import urllib
import urllib2
import json
import sys,os,time

# media_dir = os.path.join(os.path.dirname(__file__),'./media/data_example/')

def http_post(url,data):
    data = json.dumps(data)
    req = urllib2.Request(url)                 #返回一个请求
    try:
        res = urllib2.urlopen(req,data)        #返回一个响应实例
    except urllib2.URLError as e:                #以下几句是异常捕捉
        if hasattr(e, 'reason'):
            print('Reason: ', e.reason)
        elif hasattr(e, 'code'):
            print('Error code: ', e.code)
        else:
            print("other erro")
        return {"errmsg":"erro happens"}

    ret_json = res.read()  #可以把返回的实例当做文件对象操作 可读可写
    ret_python = json.loads(ret_json)
    return ret_python

def http_get(url,data):
    urldata = urllib.urlencode(data)
    url = url + '?' + urldata
    response = urllib2.urlopen(url)
    content = response.read()
    #print("content = ",content)
    content = json.loads(content) 
    return content

if __name__ == '__main__':
   myurl = 'http://tongjilab.cn:7788/mylogin/'
   data = {"username":"admin","password":"ilove2017"}
   ret = http_get(myurl,data)
   print("data = ",data)
  
   myurl = "http://123.206.216.23:7788/lesson/"
   data2 = {"name":""}
   ret2 = http_get(myurl,data2)
   print("ret2 = ",ret)
