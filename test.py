'''
import requests
import re
from bs4 import BeautifulSoup
content =content = requests.get('http://book.douban.com/').text
pattern = re.compile('<li.*?cover.*?href="(.*?)".?title="(.*?)".*?author">(.*?)</div>.*?year">(.*?)</span>',re.S)
results = re.findall(pattern,content)
for result in results:
    url,name,author,date = result
    print(url.strip(),name.strip(),author.strip(),date.strip())
'''
import re
import requests
import json
from requests.exceptions import  RequestException
from multiprocessing import Pool
def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield{
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'sccore':item[5]+item[6]
        }

def main(offset):
    url = 'https://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)
    parse_one_page(html)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

def write_to_file(content):
    with open('C:\\Users\\10193\\Desktop\\1\\result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        f.close()

if __name__ == '__main__':
    pool = Pool()
    pool.map(main,[i*10 for i in range(10)])


