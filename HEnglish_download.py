import requests
from bs4 import BeautifulSoup
from requests.exceptions import  RequestException
global i
i =0
global urls
urls = []
def get_one_page(url):
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 ' \
                              '(Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 ' \
                              '(KHTML, like Gecko) Version/5.1 Safari/534.50'
    try:
        response = requests.get('http:'+url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def get_all_mainurls(html):
    i = 0
    soup = BeautifulSoup(html, 'lxml')
    result = soup.select('.dropdown > li > a')
    hrefs = []
    for item in result:
        if '//' in item.get('href') and 'http' not in item.get('href') and 'html' not in item.get('href'):
            hrefs.append(item.get('href'))
            i = i + 1
    result = soup.select('a')
    for item in result:
        ss = item.get('href')
        if ss and '2019' in ss and 'html' in ss and 'http' not in ss and ss not in urls:
            hrefs.append(ss)
            i = i + 1
            if i >= 200:
                break


    print(hrefs)
    return hrefs

def get_all_urls(hrefs):
    global urls
    for url in hrefs:
        html = get_one_page(url)
        if html == None:
            break
        soup = BeautifulSoup(html, 'lxml')
        result = soup.select('a')
        global i
        for item in result:
            ss = item.get('href')
            if ss and '2019' in ss and 'html' in ss and 'http' not in ss and ss not in urls:
                urls.append(ss)
                i = i + 1

def write_to_files(urls):
    num = 0
    for url in urls:
        html = get_one_page(url)
        with open(r'English_download//'+str(num)+'.txt','w',encoding='utf-8') as f:
            if html:
                num = num + 1
                f.write(html)


def main():
    url = '//www.chinadaily.com.cn/'
    html = get_one_page(url)
    mainurls = get_all_mainurls(html)
    get_all_urls(mainurls)
    write_to_files(urls)

if __name__ == '__main__':
    main()
