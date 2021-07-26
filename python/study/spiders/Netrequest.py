'''Friendly url : http://httpbin.org'''
import requests
url = 'https://www.bilibili.com'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41'}
res = requests.get( url = url  , headers = headers)
print(bytes(str(res.content) , encoding = 'utf8'))


'''注意反爬虫设置'''
