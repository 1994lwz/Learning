"""伪装浏览器"""

import urllib.request
import ssl

#定义保存函数
def saveFile(date):
    path = "C:\\Users\\cnvli021\\Desktop\\reptile.out"
    with open(path, 'wb') as f:
        f.write(data)
    
#网址
url = "http://www.douban.com/"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}
req = urllib.request.Request(url = url, headers = headers)
res = urllib.request.urlopen(req)
data = res.read()
saveFile(data)
data = data.decode('utf-8')
print(data)
