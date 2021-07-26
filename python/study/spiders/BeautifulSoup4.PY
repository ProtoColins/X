from bs4 import BeautifulSoup
import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41'}
html = requests.get( 'https://www.bilibili.com',headers = headers)

print( BeautifulSoup( html.content ,from_encoding= 'gbk', exclude_encodings='unicode',features='lxml'))

