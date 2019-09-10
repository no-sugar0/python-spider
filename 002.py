import requests
import urllib.parse
import re
import lxml
from bs4 import BeautifulSoup
url='http://www.chinadaily.com.cn'
#url = 'https://maoyan.com'
#requests.Session()
headers = {}
headers['User-Agent'] = 'Mozilla/5.0 ' \
                          '(Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 ' \
                          '(KHTML, like Gecko) Version/5.1 Safari/534.50'
response = requests.get(url,headers=headers)
response.encoding='utf-8'
soup = BeautifulSoup(response.text,'lxml')
print(soup.title.string)
print(soup.title)
print(soup.p.string)
