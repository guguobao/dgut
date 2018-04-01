#!coding:utf-8
import requests
import re

#东莞理工学院登陆窗口模拟登陆


if __name__=='__main__':
    user=raw_input("请输入学号：")
    password=raw_input("请输入密码：")
    data={
        'DDDDD':user,
        'upass':password,
        '0MKKey':'123456',
    }
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3141.7 Safari/537.36',
        'Referer':'http://172.31.252.71/a70.htm?wlanuserip=172.27.169.186&wlanacip=null&wlanacname=null&vlanid=0&ip=172.27.169.186&ssid=null&areaID=null&mac=00-00-00-00-00-11m'

    }
    req=requests.post('http://172.31.252.71:801/eportal/?c=ACSetting&a=Login&protocol=http:&hostname=172.31.252.71&iTermType=1&wlanuserip=172.27.169.186&wlanacip=null&wlanacname=null&mac=cc-2d-e0-6a-dc-72&ip=172.27.169.186&enAdvert=0&queryACIP=0&loginMethod=1',data=data,headers=headers)
    #print(req.text)
    ret=re.findall(r'<title>(.*)</title>',req.text)
    ret=ret[0]
    print(ret.encode('utf-8'))


