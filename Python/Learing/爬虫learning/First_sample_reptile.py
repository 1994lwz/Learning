"""
第一个示例：简单的网页爬虫，爬取百度首页
"""
import urllib.request

url = "http://www.baidu.com/" #网址
request = urllib.request.Request(url) #请求
response = urllib.request.urlopen(request) #爬取结果
data = response.read().decode('utf-8') #设置解码方式

#print(data)
#打印爬取网页的各类信息
print(type(response))
#print(response.geturl())
print(response.info())
#print(response.getcode())
