#!python3
# -*- coding: utf-8 -*-

"""
批量下载豆瓣首页的图片
采用伪装浏览器的方式爬取豆瓣网首页的图片，保存到指定路径文件夹下
"""

#导入所需的库
import urllib.request, socket, re, sys, os

#定义文件保存路径
filePath = "C:\\Users\\temp\\Desktop\\find_image"

def savefile(path):
    #检测当前路径的有效性
    if not os.path.isdir(filePath):
        os.mkdir(filePath)
    
    #设置每个图片的路径
    pos = path.rindex('/')
    savePath = os.path.join(filePath, path[pos+1: ])
    
    return savePath
    
url = "http://www.douban.com/"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                '(KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
req = urllib.request.Request(url = url, headers = headers)
res = urllib.request.urlopen(req)
data = res.read()
for link, t in set(re.findall(r'(https:[^s]*?(jpg|png|gif))', str(data))):
    print(link)
    try:
        urllib.request.urlretrieve(link, savefile(link))
    except:
        print("失败")
